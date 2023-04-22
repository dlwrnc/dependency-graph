import unittest
from dep_graph import DependencyGraph, CyclicalDependencyException


class TestDepGraph(unittest.TestCase):

    def test_basic_example(self):
        d = DependencyGraph('test_files/example.json')
        d.print_graph()

    def test_cycle_raises(self):
        d = DependencyGraph('test_files/cycle.json')
        with self.assertRaises(CyclicalDependencyException):
            d.print_graph()

    def test_complicated_cycle_raises(self):
        d = DependencyGraph('test_files/complicated_cycle.json')
        with self.assertRaises(CyclicalDependencyException):
            d.print_graph()

    def test_bad_file(self):
        with self.assertRaises(FileNotFoundError):
            # pound is not a legal filename character
            d = DependencyGraph('bad_file#')


if __name__ == '__main__':
    unittest.main()
