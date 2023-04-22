import os
import json


class CyclicalDependencyException(Exception):
    """Exception raised when a cyclical dependency is detected"""
    pass


class DependencyGraph:

    def __init__(self, json_filepath):
        if not os.path.exists(json_filepath):
            raise FileNotFoundError(f'JSON file {json_filepath} '
                                    f'does not exist on this system.')
        self.graph = self.read_json(json_filepath) # graph as an adjacent list

    @staticmethod
    def read_json(json_filepath):
        with open(json_filepath) as json_file:
            data = json.load(json_file)
        return data

    def print_graph(self):
        for package in list(self.graph.keys()):
            self.traverse_dependencies(package)

    def traverse_dependencies(self, package, indent=0, visited=None):
        if visited is None:
            visited = set()
        if package in visited:
            raise CyclicalDependencyException('CIRCULAR DEPENDENCY DETECTED')
        print(" " * indent, f"- {package}")
        visited.add(package)
        if package in self.graph:
            dependency_list = self.graph[package]
            for item in dependency_list:
                self.traverse_dependencies(item, indent+4, visited)
                visited.remove(item)


if __name__ == '__main__':
    d = DependencyGraph('test_files/example.json')
    d.print_graph()
