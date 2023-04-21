import unittest


class TestDepGraph(unittest.TestCase):

    test_jsons = [
        'complicated_cycle.json',
        'cycle.json',
        'example.json'
    ]

    def test_basic_example(self):
        pass


if __name__ == '__main__':
    unittest.main()
