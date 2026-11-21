"""Verify the actual offline text artifact in fresh Python processes."""
import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent


class ArtifactTests(unittest.TestCase):
    def test_candidate_lengths(self):
        files = sorted((ROOT / "candidates").glob("*.txt"))
        self.assertGreaterEqual(len(files), 5)
        self.assertLessEqual(len(files), 8)
        for path in files:
            value = path.read_bytes().decode("utf-8")
            with self.subTest(candidate=path.name):
                self.assertTrue(value.strip())
                self.assertLessEqual(len(value), 280)
                print(path.name, len(value), "code points")

    def test_entry_writes_one_deterministic_utf8_text(self):
        self.assertTrue((ROOT / "main.py").is_file(), "The entrypoint is not implemented")
        outputs = []
        for seed in ("0", "971"):
            with tempfile.TemporaryDirectory(dir=ROOT.parent) as directory:
                environment = dict(os.environ, MAKEFUN_OUTPUT_DIR=directory, PYTHONHASHSEED=seed)
                subprocess.run([sys.executable, "-I", "-B", str(ROOT / "main.py")],
                               cwd=ROOT.parent, env=environment, check=True, timeout=10)
                files = list(Path(directory).iterdir())
                self.assertEqual([file.name for file in files], ["entry.txt"])
                data = files[0].read_bytes()
                value = data.decode("utf-8")
                self.assertTrue(value.strip())
                self.assertTrue(1 <= len(value) <= 280)
                self.assertFalse(data.startswith(b"\xef\xbb\xbf"))
                outputs.append(data)
        self.assertEqual(outputs[0], outputs[1])
        print("OUTPUT", outputs[0].decode("utf-8"))
        print("CODE POINTS", len(outputs[0].decode("utf-8")))
        print("SHA256", hashlib.sha256(outputs[0]).hexdigest())


if __name__ == "__main__":
    unittest.main(verbosity=2)
