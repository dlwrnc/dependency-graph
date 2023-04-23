# dependency-graph

Simple module to traverse a dependency graph and print the fully-traversed graph as a bulletpoint, indented list.

Example files can be viewed in the test_files directory.

The code can be run by doing the following:

```python -m dep_graph```

In this case, dep_graph will run against the default test_files/example.json.

If you want to change this, you can either edit the code on line 68, or you can provide your target file as a positional
argument when running the code. For example:

```python -m dep_graph test_files/example.json```