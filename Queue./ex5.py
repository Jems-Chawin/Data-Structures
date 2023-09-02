class Queue():
    def __init__(self):
        self.__queue = []

    def enqueue(self, data):
        self.__queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.__queue.pop(0)

    def is_empty(self):
        return len(self.__queue) == 0
    
    def size(self):
        return len(self.__queue)
    
    @property
    def queue(self):
        return self.__queue
    
class Room():
    def __init__(self, width, height):
        self.queue = Queue()
        self.width = width
        self.height = height
        self.map = []
        self.maze = []
        self.start_pos = None

    def create_map(self, room_string):
        room_lines = room_string.split(',')

        if len(room_lines) != self.height:
            return 'Invalid map input.'
        
        for line in room_lines:
            if len(line) != self.width:
                return 'Invalid map input.'
            self.map.append(line)

    def find_start_pos(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.map[i][j] == 'F':
                    self.start_pos = (j, i)
                    self.queue.enqueue(self.start_pos)
                    self.maze.append(self.start_pos)
                    break
            if self.start_pos != None:
                break
        if self.start_pos == None:
            return 'Invalid map input.'

    def find_portal(self):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        while not self.queue.is_empty():
            print(f'Queue: {self.queue.queue}')

            x, y = self.queue.dequeue()

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if 0 <= new_x < self.width and 0 <= new_y < self.height:
                    pos = self.map[new_y][new_x]
                    if pos == 'O':
                        return 'Found the exit portal.'
                    elif pos == '_' and (new_x, new_y) not in self.maze:
                        self.maze.append((new_x, new_y))
                        self.queue.enqueue((new_x, new_y))

        return 'Cannot reach the exit portal.'

input_str = input('Enter width, height, and room: ')
width, height, room = input_str.split()
room_obj = Room(int(width), int(height))
temp = room_obj.create_map(room)
if temp != None:
    print(temp)
else:
    temp2 = room_obj.find_start_pos()
    if temp2 != None:
        print(temp2)
    else:
        print(room_obj.find_portal())

'''
example test cases

Enter width, height, and room: 6 4 F__###,##_###,##__##,###__O
Queue: [(0, 0)]
Queue: [(1, 0)]
Queue: [(2, 0)]
Queue: [(2, 1)]
Queue: [(2, 2)]
Queue: [(3, 2)]
Queue: [(3, 3)]
Queue: [(4, 3)]
Found the exit portal.

Enter width, height, and room: 8 6 ########,##___###,##_F_###,##____##,##_##_O_,##______
Queue: [(3, 2)]
Queue: [(3, 1), (4, 2), (3, 3), (2, 2)]
Queue: [(4, 2), (3, 3), (2, 2), (4, 1), (2, 1)]
Queue: [(3, 3), (2, 2), (4, 1), (2, 1), (4, 3)]
Queue: [(2, 2), (4, 1), (2, 1), (4, 3), (2, 3)]
Queue: [(4, 1), (2, 1), (4, 3), (2, 3)]
Queue: [(2, 1), (4, 3), (2, 3)]
Queue: [(4, 3), (2, 3)]
Queue: [(2, 3), (5, 3)]
Queue: [(5, 3), (2, 4)]
Queue: [(2, 4), (5, 4)]
Queue: [(5, 4), (2, 5)]
Found the exit portal.

Enter width, height, and room: 1 1 F
Queue: [(0, 0)]
Cannot reach the exit portal.

Enter width, height, and room: 3 3 F__,##_,O_
Invalid map input.
'''
