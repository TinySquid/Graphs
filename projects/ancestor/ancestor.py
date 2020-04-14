import sys

sys.path.append("../graph")

from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for ancestor in ancestors:
        """
        Go through provided ancestors and build a graph
        Add vertices
        Add edges
        """
        # Add vertices
        if not graph.vertex_exists(ancestor[0]):
            graph.add_vertex(ancestor[0])
        if not graph.vertex_exists(ancestor[1]):
            graph.add_vertex(ancestor[1])

        # Add edges (flipped)
        graph.add_edge(ancestor[1], ancestor[0])
    # Return earliest connected vertex from starting_node
    # -1 if node has no parents
    return graph.dft_ancestor(starting_node)


# DEBUG
# test_ancestors = [
#     (1, 3),
#     (2, 3),
#     (3, 6),
#     (5, 6),
#     (5, 7),
#     (4, 5),
#     (4, 8),
#     (8, 9),
#     (11, 8),
#     (10, 1),
# ]

# print(earliest_ancestor(test_ancestors, 1))
# print(earliest_ancestor(test_ancestors, 2))
# print(earliest_ancestor(test_ancestors, 3))
# print(earliest_ancestor(test_ancestors, 4))
# print(earliest_ancestor(test_ancestors, 5))
# print(earliest_ancestor(test_ancestors, 6))
# print(earliest_ancestor(test_ancestors, 7))
# print(earliest_ancestor(test_ancestors, 8))
# print(earliest_ancestor(test_ancestors, 9))
# print(earliest_ancestor(test_ancestors, 10))
# print(earliest_ancestor(test_ancestors, 11))
