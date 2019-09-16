# given a 2-D grid map, a start node, and an end node,
# return the shortest path from the start to the end.

# the allowed directions in which one can move from a node
# to a neighboring node
direction = [[1,0],[-1,0],[0,1],[0,-1],
             [1,1],[-1,1],[1,-1],[-1,-1]]

class Node():

    def __init__(self, parent = None, position = [0,0]):
        self.parent = parent
        self.position = position
        self.f = 0
        self.g = 0
        self.h = 0


    # define the equivalence function for the node to be compared to another node
    def __eq__(self, node):
        return self.position == node.position

def my_astar(map = [], start = [0,0], end = [0,0]):
    openSet = []
    closedSet = []

    openSet.append(start)

    while len(openSet)>0:
        # find the node in the open set that has the smallest f value
        current_node = openSet[0]
        current_node_openSet_ind = 0
        for ind, openSet_node in enumerate(openSet):
            if openSet_node.f < current_node.f:
                current_node_openSet_ind = ind
                current_node = openSet_node
        # move the chosen node from the open set to the closed set
        openSet.pop(current_node_openSet_ind)
        closedSet.append(current_node)


        if current_node == end: # the shortest path is found
            path = [] # the path from start to end
            path.append(current_node.position)
            temp = current_node.parent
            while temp is not None:
                path.append(temp.position)
                temp = temp.parent
            path = path [::-1]
            return path

        else:

            for dir_index, dir in enumerate(direction):

                child_node = Node(parent=None, position=[0,0])
                child_node.position[0] = current_node.position[0] + dir[0]
                child_node.position[1] = current_node.position[1] + dir[1]


                child_node.parent = current_node

                # if the child node is outside the map, then the shortest path shall not go through it
                if (child_node.position[0] < 0
                 or child_node.position[0] > (len(map)-1)
                 or child_node.position[1] < 0
                 or child_node.position[1] > (len(map)-1)):
                    continue

                # if an obstacle is at a node, then the shortest path shall not go through it
                if map[child_node.position[0]][child_node.position[1]] == 1:
                    continue

                for closed_node in closedSet:
                    if child_node == closed_node:
                        continue

                child_node.g = current_node.g + 1
                child_node.h = (end.position[0] - child_node.position[0])**2 + (end.position[1] - child_node.position[1])**2
                child_node.f = child_node.g + child_node.h

                # check if child_node is already in the open set and has f value smaller than the
                # f value just computed
                for node in openSet:
                    if child_node == node and (child_node.g > node.g):
                        continue

                openSet.append(child_node)



# driver
def main():

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

if __name__ == '__main__':
    main()

