import unittest
from dep_graph import DependencyGraph, CyclicalDependencyException
from io import StringIO
from unittest.mock import patch


class TestDepGraph(unittest.TestCase):

    def test_basic_example(self):

        target_outp = [
            '- pkg1',
            '  - pkg2',
            '    - pkg3',
            '  - pkg3',
            '- pkg2',
            '  - pkg3',
            '- pkg3',
            ''  # we get an extra blank from the split
        ]

        with patch('sys.stdout', new=StringIO()) as outp:
            d = DependencyGraph('test_files/example.json')
            d.print_graph()
        actual_outp = outp.getvalue().split('\n')
        assert target_outp == actual_outp

    def test_no_dependencies(self):
        target_outp = [
            '- pkg1',
            '- pkg2',
            '- pkg3',
            ''  # we get an extra blank from the split
        ]

        with patch('sys.stdout', new=StringIO()) as outp:
            d = DependencyGraph('test_files/no_dependencies.json')
            d.print_graph()
        actual_outp = outp.getvalue().split('\n')
        assert target_outp == actual_outp

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
            DependencyGraph('bad_file#')


if __name__ == '__main__':
    unittest.main()
