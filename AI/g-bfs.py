from random import randint


class grid:
    def __init__(self):
        print("Grid environment construction initialized. Only binary values allowed, 0 represents blocked and 1 "
              "represents free grid.")
        row, col = map(int, input("Enter no.of rows and columns: ").split())
        self.graph = []
        for i in range(row):
            self.graph.append(list(map(int, input("Enter " + str(i) + " row: ").split())))
        print(self.graph)
        print("Input the coordinates of starting grid and goal grid")
        self.start = tuple(map(int, input("Enter start grid coordinates: ").split()))
        self.goal = tuple(map(int, input("Enter goal grid coordinates: ").split()))
        self.prev = None
        self.path_cost = {}
        self.cost()

    def info(self, coordinates: tuple) -> bool:
        try:
            if self.graph[coordinates[0]][coordinates[1]] == 1 and coordinates[0] > -1 and coordinates[1] > -1:
                return True
            else:
                return False
        except IndexError:
            print("Invalid Coordinates", coordinates)
            return False

    def cost(self):
        rows = len(self.graph)
        col = len(self.graph[0])
        linear = []
        for i in range(rows):
            for j in range(col):
                linear.append((i, j))
        k = 0
        for i in linear:
            self.path_cost[i] = randint(5, 55 - k) if i != self.goal else 0
            k += 1

    def get_cost(self, frm: tuple) -> int:
        return self.path_cost[frm]


class Utility:
    def __init__(self, grid_obj: grid):
        self.current = ()
        self.cost = 0
        self.pathTracker = {}
        self.grid_obj = grid_obj
        self.closed = []
        self.open = [self.grid_obj.start]
        # self.prev = self.current

    def next_move(self, current: tuple) -> tuple:
        x, y = self.current = current
        temp = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
                (x + 1, y + 1)]
        valid_moves = []

        for i in temp:
            if i != self.grid_obj.prev and self.grid_obj.info(i) and i not in self.closed:
                valid_moves.append(i)

            if i == self.grid_obj.goal:
                self.open.append(i)
                print("Goal Reached")
                return i

        if not valid_moves:
            if self.closed:
                last_move = self.closed[-1]
                self.closed.pop()
                return last_move
            else:
                print("No valid moves left.")
                return current

        next_step = ()
        min_cost = 100
        for i in valid_moves:
            if self.grid_obj.get_cost(i) < min_cost:
                next_step = i
                min_cost = self.grid_obj.get_cost(i)
        self.closed.append(current)
        print("prev", self.grid_obj.prev, "current", self.current, "Next step: ", next_step)
        self.open.clear()
        self.grid_obj.prev = self.current
        return next_step

    def g_n(self, to: tuple) -> int:
        var = (self.current, to)
        cost = self.grid_obj.get_cost(to)  # Use the actual path cost
        self.pathTracker[var] = cost
        return cost

    def h_n(self, to: tuple) -> float:
        if to == self.grid_obj.goal:
            return 0
        dx = abs(to[0] - self.grid_obj.goal[0])
        dy = abs(to[1] - self.grid_obj.goal[1])
        return dx + dy


def main():
    grid_obj = grid()
    util_obj = Utility(grid_obj)
    util_obj.current = grid_obj.start
    final_path = [grid_obj.start]
    while True:
        if util_obj.current == grid_obj.goal:
            break
        util_obj.current = util_obj.next_move(util_obj.current)
        final_path.append(util_obj.current)
        print("Current: ", util_obj.current)
    print("Path: ", final_path)
    print("Closed: ", util_obj.closed)
    print(util_obj.grid_obj.path_cost)
    for i in range(len(grid_obj.graph)):
        for j in range(len(grid_obj.graph[0])):
            print("*", end=" ") if (i, j) in final_path else print("0", end=" ")
        print()


if __name__ == '__main__':
    main()
