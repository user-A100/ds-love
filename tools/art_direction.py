"""Validated, text-anchored art cues shared by the importer and art installer."""
import json
from pathlib import Path


def load_direction(root, events):
    data = json.loads((Path(root) / 'story/art_direction.json').read_text(encoding='utf-8'))
    by_anchor = {}
    for entry in data['scenes']:
        for cue in [entry, *entry.get('cues', [])]:
            anchor = cue['anchor']
            matches = [e for e in events if e.kind == 'say' and e.chapter == anchor['chapter']
                       and e.speaker == anchor['speaker'] and e.text == anchor['text']]
            occurrence = anchor.get('occurrence', 1)
            if len(matches) < occurrence:
                raise ValueError('Art anchor missing: {} / {}'.format(entry['id'], anchor['text']))
            event = matches[occurrence - 1]
            by_anchor.setdefault(event, []).append((entry, cue))
    for key, asset in data['assets'].items():
        source = Path(root) / asset['source']
        if not source.is_file():
            raise FileNotFoundError(source)
        if asset['kind'] not in ('background', 'cg', 'sprite', 'prop'):
            raise ValueError('Invalid asset kind: ' + key)
    for entry in data['scenes']:
        if entry.get('bgm') and not (Path(root) / 'game' / entry['bgm']).is_file():
            raise FileNotFoundError(entry['bgm'])
        refs = [entry['background'], *entry.get('characters', {}).values()]
        for cue in entry.get('cues', []):
            refs += [cue[k] for k in ('cg', 'background', 'prop') if cue.get(k)]
            refs += list(cue.get('show', {}).values())
        for ref in refs:
            if ref not in data['assets']:
                raise ValueError('Unknown art reference: ' + ref)
    return data, by_anchor


def image_name(key):
    return 'art_' + key.replace('.', '_').replace('-', '_')


class ArtDirector:
    def __init__(self, root, events, emit):
        self.data, self.cues = load_direction(root, events)
        self.emit = emit
        self.profiles = {}
        self.shown = set()
        self.background = None
        self.full_cg = False
        self.positions = {'ds': 'left', 'cl': 'center', 'gp': 'right'}

    def scene(self, background):
        self.emit('scene {} with trans_dissolve'.format(image_name(background)))
        self.shown.clear()
        self.full_cg = False

    def show(self, who, asset):
        self.profiles[who] = asset
        self.emit('show {} as {} at sprite_pos_{} with trans_dissolve'.format(
            image_name(asset), who, self.positions[who]))
        self.shown.add(who)

    def before(self, event, speaker):
        event_cues = self.cues.get(event, [])
        next_cg = any(cue.get('cg') for _, cue in event_cues)
        for entry, cue in event_cues:
            if cue is entry:
                if entry.get('bgm'):
                    self.emit('play music {} fadeout 1.0 fadein 1.0 if_changed'.format(json.dumps(entry['bgm'])))
                self.emit('## 美术分景 {} · {}'.format(entry['id'], entry['title']))
                self.background = entry['background']
                self.profiles = dict(entry.get('characters', {}))
                self.scene(self.background)
            else:
                if cue.get('background'):
                    self.background = cue['background']
                    self.scene(self.background)
                if cue.get('restore') and not next_cg:
                    self.scene(self.background)
                if cue.get('cg'):
                    self.scene(cue['cg'])
                    self.full_cg = True
                for who in cue.get('hide', []):
                    self.emit('hide {} with trans_dissolve'.format(who))
                    self.shown.discard(who)
                    # Prevent the automatic dialogue entrance from undoing an exit.
                    self.profiles.pop(who, None)
                if cue.get('clear_prop'):
                    self.emit('hide story_prop with trans_dissolve')
                if cue.get('prop'):
                    asset = self.data['assets'][cue['prop']]
                    if asset['kind'] in ('cg', 'background'):
                        display = 'expression Transform("{}", xysize=(420, 236))'.format(asset['runtime'])
                    else:
                        display = image_name(cue['prop'])
                    self.emit('show {} as story_prop at story_prop_pos with trans_dissolve'.format(display))
                for who, asset in cue.get('show', {}).items():
                    self.show(who, asset)
        who = 'ds' if speaker == 'mystery' else speaker
        if not self.full_cg and who in self.profiles and who not in self.shown:
            self.show(who, self.profiles[who])

    def definitions(self):
        lines = []
        for key, asset in self.data['assets'].items():
            path = asset['runtime']
            if asset['kind'] in ('background', 'cg'):
                display = 'Transform("{}", xysize=(config.screen_width, config.screen_height))'.format(path)
            elif asset['kind'] == 'sprite':
                display = 'Transform("{}", zoom={:.6f})'.format(path, 700 / asset['height'])
            else:
                display = 'Transform("{}", zoom={:.6f})'.format(path, min(420 / asset['width'], 290 / asset['height']))
            lines.append('image {} = {}'.format(image_name(key), display))
        return lines
