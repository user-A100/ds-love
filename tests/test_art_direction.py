"""Regression checks for art placement, off-screen speakers, and CG isolation."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from import_story import Importer
from art_direction import ArtDirector, load_direction


class ArtDirectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.importer = Importer()
        cls.importer.parse()
        cls.data, cls.cues = load_direction(ROOT, cls.importer.events)

    def test_every_chapter_has_a_background_before_its_first_dialogue(self):
        rendered = self.importer.render()
        for chapter in self.importer.chapter_order:
            lines = rendered[chapter + '.rpy'].splitlines()
            first_say = next(i for i, line in enumerate(lines) if ' id story_' in line)
            self.assertTrue(any('scene art_' in line for line in lines[:first_say]), chapter)

    def test_cg_has_no_automatic_standing_sprite_and_restores_cleanly(self):
        output = []
        director = ArtDirector(ROOT, self.importer.events, output.append)
        for event in self.importer.events:
            if event.chapter != 'ch00' or event.kind != 'say':
                continue
            director.before(event, 'mystery' if event.speaker == '？？？' else 'u')
            if event.text == '我还没来得及反应，就被撞得坐在地上。':
                self.assertTrue(director.full_cg)
                self.assertFalse(director.shown)
            if event.text == '你没事吧？！':
                self.assertFalse(director.full_cg)
                self.assertIn('ds', director.shown)

    def test_phone_messages_never_show_remote_characters(self):
        remote = ['C4-10', 'C4-13', 'C4-14', 'C5-04', 'C5-07A', 'C5-07B', 'C5-07C', 'DS-01']
        for scene in self.data['scenes']:
            if scene['id'] in remote:
                self.assertFalse(scene['characters'], scene['id'])

    def test_college_spring_gap_never_uses_school_or_mature_costumes(self):
        for scene in self.data['scenes']:
            if scene['id'] in ['DS-06', 'DS-07', 'DS-08', 'DS-09']:
                self.assertFalse(scene['characters'])
                self.assertTrue(scene['notes'])
                self.assertFalse(any('show' in c or 'cg' in c for c in scene['cues']))

    def test_unmatched_anchor_fails_instead_of_silently_misplacing_art(self):
        from dataclasses import replace
        events = [replace(e, text='changed') if e.text == self.data['scenes'][0]['anchor']['text'] else e
                  for e in self.importer.events]
        with self.assertRaisesRegex(ValueError, 'Art anchor missing'):
            load_direction(ROOT, events)


if __name__ == '__main__':
    unittest.main()
