import unittest
from dep_graph import DependencyGraph, CyclicalDependencyException
from io import StringIO
from unittest.mock import patch


class TestDepGraph(unittest.TestCase):
    """Unit tests for depgraph module."""

    def test_json_load(self):
        """Tests that the json is properly loaded into adjacency
        list format."""
        target = {
            "pkg1": ["pkg2", "pkg3"],
            "pkg2": ["pkg3"],
            "pkg3": []
        }
        data = DependencyGraph.read_json('test_files/example.json')
        assert target == data

    def test_basic_example(self):
        """Tests that the example provided traverses and prints as expected."""
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
        """Tests that a no-dependency file traverses and prints as expected."""
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
        """Tests that a two-package-cycle raises the expected error."""
        d = DependencyGraph('test_files/cycle.json')
        with self.assertRaises(CyclicalDependencyException):
            d.print_graph()

    def test_complicated_cycle_raises(self):
        """Tests that a three-package-cycle raises the expected error."""
        d = DependencyGraph('test_files/complicated_cycle.json')
        with self.assertRaises(CyclicalDependencyException):
            d.print_graph()

    def test_bad_file(self):
        """Tests that a nonexistent file raises the expected error."""
        with self.assertRaises(FileNotFoundError):
            # pound is not a legal filename character
            DependencyGraph('bad_file#')

    def test_non_json(self):
        """Tests that a non-json file raises the expected error."""
        with self.assertRaises(TypeError):
            DependencyGraph('test_files/not_json')


if __name__ == '__main__':
    unittest.main()
