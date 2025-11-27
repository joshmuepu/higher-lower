import os
import tempfile
import unittest
from pathlib import Path
import main


class TestHighScorePersistence(unittest.TestCase):
    def test_high_score_load_save_cycle(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "hs.json"
            # Initial load should yield 0
            self.assertEqual(main.load_high_score(path), 0)
            # Save a score
            main.save_high_score(7, path)
            self.assertTrue(path.exists())
            # Load again should yield 7
            self.assertEqual(main.load_high_score(path), 7)
            # Overwrite higher
            main.save_high_score(15, path)
            self.assertEqual(main.load_high_score(path), 15)

    def test_corrupt_file_graceful(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "hs.json"
            path.write_text("{corrupt}")
            # Should return 0 on corrupt content
            val = main.load_high_score(path)
            self.assertEqual(val, 0)


if __name__ == '__main__':
    unittest.main()
