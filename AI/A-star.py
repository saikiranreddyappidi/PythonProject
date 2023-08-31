from random import randint
from math import dist


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

    def info(self, coordinates: tuple) -> bool:
        try:
            if self.graph[coordinates[0]][coordinates[1]] == 1 and coordinates[0] > -1 and coordinates[1] > -1:
                return True
            else:
                return False
        except IndexError:
            print("Invalid Coordinates", coordinates)
            return False


class Utility:
    def __init__(self, grid_obj: grid):
        self.arr = []
        self.current = ()
        self.cost = 0
        self.pathTracker = {}
        self.grid_obj = grid_obj
        # self.prev = self.current

    def next_move(self, current: tuple) -> tuple:
        x, y = self.current = current
        temp = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
                (x + 1, y + 1)]
        costs = []
        for i in temp:
            if i != self.grid_obj.prev and self.grid_obj.info(i):
                self.arr.append(i)
                costs.append(self.g_n(i) + self.h_n(i))
            if i == self.grid_obj.goal:
                self.arr.append(i)
                costs.append(self.g_n(i) + self.h_n(i))
                print("Goal Reached")
                return i
        try:
            next_step = self.arr[costs.index(min(costs))]
            print("Prev: ", self.grid_obj.prev, "Current: ", self.current, "Next Step: ", next_step)
        except ValueError:
            print("No valid moves left.")
            exit(2)
        self.grid_obj.prev = self.current
        self.arr.clear()
        return next_step

    def g_n(self, to: tuple) -> int:
        var = (self.current, to)
        cost = self.pathTracker[var] = 1# randint(0, 25)
        return cost

    def h_n(self, to: tuple) -> float:
        if to == self.grid_obj.goal:
            return 0
        return dist(to, self.grid_obj.goal)


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
        # print("Current: ", util_obj.current)
    print("Path: ", final_path)
    print("Cost: ", util_obj.pathTracker)
    for i in range(len(grid_obj.graph)):
        for j in range(len(grid_obj.graph[0])):
            print("*", end=" ") if (i, j) in final_path else print("0", end=" ")
        print()


if __name__ == '__main__':
    main()
