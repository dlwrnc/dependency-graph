import os
import json


class DependencyGraph:

    def __init__(self, json_filepath):
        if not os.path.exists(json_filepath):
            raise Exception(f'JSON file {json_filepath}'
                            f' does not exist on this system.')
        self.json = self.read_json(json_filepath)
        for package in list(self.json.keys()):
            self.print_graph(package)

    def read_json(self, json_filepath):
        with open(json_filepath) as json_file:
            data = json.load(json_file)
        return data

    def print_graph(self, package, indent=0, visited=None):
        if visited is None:
            visited = set()
        if package in visited:
            raise Exception('CIRCULAR DEPENDENCY DETECTED')
        print(" " * indent, f"- {package}")
        visited.add(package)
        if package in self.json:
            dependency_list = self.json[package]
            for item in dependency_list:
                self.print_graph(item, indent+4, visited)
                visited.remove(item)


if __name__ == '__main__':
    d = DependencyGraph('/Users/deborahlawrence/Code/dependency-graph/test_files/example.json')
