from queue import PriorityQueue
from collections import defaultdict
from functools import cache

class Node:
    def __init__(self, location: tuple, direction: tuple, count: int) -> None:
        self.loc = location
        self.dir = direction
        self.count = count
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return False
        return self.loc == other.loc and self.dir == other.dir and self.count == other.count
    
    def __hash__(self) -> int:
        return hash((self.loc, self.dir, self.count))
    
    def __lt__(self, other) -> bool:
        return self.count < other.count

with open('17/input.txt', 'r') as f:
    board = f.read().split('\n')

def get_adjacent(node: Node, min_move: int, max_move: int) -> list[Node]:
    adjacent = []
    for dir in [(0,1),(0,-1),(1,0),(-1,0)]:
        if node.count < min_move and dir != node.dir and node.count != 0:
            continue
        if node.count == max_move and dir == node.dir:
            continue
        if node.dir == (-dir[0],-dir[1]):
            continue
        new_tile = (node.loc[0]+dir[0],node.loc[1]+dir[1])
        if 0 <= new_tile[0] < len(board) and 0 <= new_tile[1] < len(board[0]):
            new_node = Node(new_tile, dir, node.count+1 if node.dir == dir else 1)
            adjacent.append(new_node)
    return adjacent

def dijkstra(min_move = 0, max_move = 3):
    queue = PriorityQueue()
    distances = defaultdict(lambda: 10000000)

    start_node = Node((0,0), (1,0), 0)
    queue.put((0, start_node))
    distances[start_node] = 0

    while not queue.empty():
        node = queue.get()[1]
        for neighbour in get_adjacent(node, min_move, max_move):
            i,j = neighbour.loc
            if distances[neighbour] > distances[node] + int(board[i][j]):
                distances[neighbour] = distances[node] + int(board[i][j])
                queue.put((distances[neighbour], neighbour))
    
    end = (len(board)-1, len(board[0])-1)
    minimum = 1000000000
    for dir in [(0,1),(0,-1),(1,0),(-1,0)]:
        for count in range(min_move,max_move+1):
            node = Node(end, dir, count)
            if distances[node] < minimum:
                minimum = distances[node]
    return minimum


sol1 = dijkstra()
print(sol1)
sol2 = dijkstra(min_move=4,max_move=10)
print(sol2)





    