from ast import literal_eval
import random
from room import Room
from player import Player
from world import World


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() != 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

visited = {}
starting_room_id = player.current_room.id

# Create a queue to store unexplored rooms
stack = Stack()
traversal_path = []
opposites_path = []

# Store the room in the queue
stack.push(starting_room_id)
opposites = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# While there are rooms left to be explored...
while stack.size() > 0:
    # Get the room_id of the unexplored room
    room_id = stack.pop()

    if room_id not in visited:
        visited[room_id] = {'n': '?', 's': '?', 'e': '?', 'w': '?'}

    # Get all room exits
    room_exits = player.current_room.get_exits()
    all_rooms_explored = True

    # Check all room exits, seeing if they have been tried already
    for d in room_exits:
        if visited[room_id][d] == '?':
            direction_choice = d
            all_rooms_explored = False

    # If there are any unexlpored rooms, travel in new direction
    if all_rooms_explored == False:
        player.travel(direction_choice)
        traversal_path.append(direction_choice)
        opposites_path.append(opposites[direction_choice])

        visited[room_id][direction_choice] = player.current_room.id

        if player.current_room.id not in visited:
            visited[player.current_room.id] = {
                'n': '?', 's': '?', 'e': '?', 'w': '?'}

        visited[player.current_room.id][opposites[direction_choice]] = room_id
        stack.push(player.current_room.id)

    # If all connected rooms have been explored, backtrack and add new room to the stack
    else:
        if len(opposites_path) > 0:
            opposite_direction = opposites_path.pop()
            player.travel(opposite_direction)
            traversal_path.append(opposite_direction)
            stack.push(player.current_room.id)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
