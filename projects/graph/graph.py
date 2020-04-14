"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue to get the 'breadth-first' functionality
        # Create a dict to remember which nodes we've visited
        # Enqueue starting_vertex
        # From current vertex, enqueue connected vertices
        # Mark current vertex and children as visited
        # Repeat

        visited = {}
        queue = Queue()

        # Enqueue starting vertex (root of traversal)
        queue.enqueue(starting_vertex)
        # Mark as visited
        visited[starting_vertex] = True

        # Continue until queue is empty (meaning the whole graph has been traversed)
        while queue.size() != 0:
            # Peek queue head
            current_vertex = queue.queue[0]
            # Enqueue connected vertices
            for vertex in self.vertices[current_vertex]:
                if not visited.get(vertex):
                    # Add to queue if not already visited
                    queue.enqueue(vertex)
                    # Set as visited to prevent further enqueueing of same vertex
                    visited[vertex] = True

            # Dequeue current vertex
            queue.dequeue()
            # Do work on current vertex
            print(current_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Maintain list of visited nodes
        # Dive in till deepest node reached
        # Then back out to previous node
        # Repeat

        # Setup
        visited = {}
        stack = Stack()
        # Put root on top of stack
        stack.push(starting_vertex)
        # Mark visited
        visited[starting_vertex] = True

        while stack.size() > 0:
            # Pointer to current vertex
            current_vertex = stack.pop()

            for vertex in self.vertices[current_vertex]:
                if not visited.get(vertex):
                    # Push vertex
                    stack.push(vertex)
                    # Mark visited
                    visited[vertex] = True

            # Do work on vertex
            print(current_vertex)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Base case
        # If vertex visited, return

        # Setup
        visited = {starting_vertex: True}

        # Recursion helper
        def dive(current_vertex, visited):
            # Do work on vertex
            print(current_vertex)

            # Go thru neighbors and dive if not visited
            for vertex in self.get_neighbors(current_vertex):
                if not visited.get(vertex):
                    # Mark visited
                    visited[vertex] = True
                    # DIVE!!!
                    dive(vertex, visited)

        # Start recursion
        dive(starting_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    # graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    # graph.dft(1)
    graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
