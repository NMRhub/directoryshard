from pathlib import Path
from unittest import TestCase

from directoryshard import shardprefix, sharded, ShardedDirectory

#
# Regression test
#

VALUES = {'correct':'4x','horse':'6g','battery':'ed','staple':'2k'}
class Test(TestCase):

    def test_shardprefix(self):
        for name, prefix in VALUES.items():
            self.assertEqual(shardprefix(name),prefix)

    def test_path(self):
        for name, prefix in VALUES.items():
            pname = Path(name)
            pprefix = Path(prefix)
            self.assertEqual(sharded(pname), pprefix / name)
            self.assertEqual(sharded(name), pprefix / name)

    def test_dir(self):
        sd = ShardedDirectory('/tmp')
        ptmp = Path('/tmp')
        for name, prefix in VALUES.items():
            spath = sd.filepath(name)
            spath.relative_to(ptmp) # raise ValueError if not subdirectory
            self.assertTrue(prefix in spath.parts)
            self.assertTrue(spath.is_absolute())
        print(sd.filepath('python'))

