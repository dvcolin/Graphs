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
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print('Vertex does not exist')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()

        # Add the starting vertex_id to queue
        q.enqueue(starting_vertex)

        # Create an empty set to store visited nodes
        visited = set()

        # While the queue is not empty
        while q.size() > 0:
            # Dequeue, the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it has not been visited...
            # Mark it as visited
            if v not in visited:
                visited.add(v)
                print(v)
            # Then add all neighbors to the back of the queue
                for n in self.get_neighbors(v):
                    q.enqueue(n)
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()

        # Add the starting vertex_id to stack
        s.push(starting_vertex)

        # Create an empty set to store visited nodes
        visited = set()

        # While the stack is not empty
        while s.size() > 0:
            # Pop, the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it has not been visited...
            # Mark it as visited
            if v not in visited:
                visited.add(v)
                print(v)
            # Then add all neighbors to the stack
                for n in self.get_neighbors(v):
                    s.push(n)

    def dft_recursive(self, vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
    ​
        This should be done using recursion.
        """
        # Check if the node is visited
        # Hint: https://docs.python-guide.org/writing/gotchas/
        # If not...
        # Mark it as visited
        # Print
        # Call DFT_Recursive on each child
        if visited == None:
            visited = set()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            for n in self.get_neighbors(vertex):
                self.dft_recursive(n, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # Add A PATH TO the starting vertex_id to the queue
        q.enqueue([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH
            path = q.dequeue()
        # GRAB THE LAST VERTEX FROM THE PATH
            last_vertex = path[-1]
            # CHECK IF IT'S THE TARGET
            if last_vertex == destination_vertex:
                # IF SO, RETURN THE PATH
                return path
            # Check if it's been visited
            if last_vertex not in visited:
                # If it has not been visited...
                visited.add(last_vertex)
            # Mark it as visited
            # Then add A PATH TO all neighbors to the back of the queue
                for n in self.get_neighbors(last_vertex):
                    new_path = path.copy()
                    new_path.append(n)
                    q.enqueue(new_path)
            # (Make a copy of the path before adding)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack
        s = Stack()
        # Add A PATH TO the starting vertex_id to the queue
        s.push([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
                # Dequeue, the first PATH
            path = s.pop()
            # GRAB THE LAST VERTEX FROM THE PATH
            last_vertex = path[-1]
            # CHECK IF IT'S THE TARGET
            if last_vertex == destination_vertex:
                    # IF SO, RETURN THE PATH
                return path
            # Check if it's been visited
            if last_vertex not in visited:
                # If it has not been visited...
                visited.add(last_vertex)
            # Mark it as visited
            # Then add A PATH TO all neighbors to the back of the queue
                for n in self.get_neighbors(last_vertex):
                    new_path = path.copy()
                    new_path.append(n)
                    s.push(new_path)
            # (Make a copy of the path before adding)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
    ​
        This should be done using recursion.
        """
        if visited == None:
            visited = set()
        if path == None:
            path = []
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)

            if starting_vertex == destination_vertex:
                return path_copy

            for n in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(
                    n, destination_vertex, path_copy, visited)

                if new_path != None:
                    return new_path


if __name__ == '__main__':
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

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
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
    '''
    graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    graph.dft(1)
    graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6, [1]))
