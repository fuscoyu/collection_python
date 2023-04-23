import unittest

from .. import switch_hugepages


class Test_Switch_Hugepages(unittest.TestCase):
    def test_run_cmd(self):
        CMD = ''
        _, result = switch_hugepages.run_cmd(CMD)

    def test_compute_osd_memory_mb(self):
        pass

    def test_compute_reserved_hugepage_memory_count(self):
        pass

    def test_cleanup(self):
        pass


if __name__ == '__main__':
    unittest.main()
