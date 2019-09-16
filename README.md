# a_star_algorithm
Given a 2-D grid map, a start node, and an end node,  return the shortest path from the start to the end.

For example, given

    map = [ [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]

    start = Node(parent=None, position=[7,1])
    end = Node(parent=None, position=[1,8])

    path = my_astar(map, start, end)
    print(path)
    
and the returned path is
    [[7, 1], [8, 2], [7, 3], [6, 3], [5, 4], [4, 5], [3, 6], [3, 7], [2, 8], [1, 8]]
