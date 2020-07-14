
from solve import Solver
from priority_queue import PriorityQueue
from maze import Maze


class SolverAStarSearch(Solver):

    def __init__(self, maze):
        super().__init__(maze)

    def solve(self):
        pq = PriorityQueue(lambda x, y: x[3] >= y[3])
        pq.push((0, 0, 0, 2 * (self.maze_dim - 1)))
        visited = {}
        parents = {}
        distances = dict([((y, x), 1000 * self.maze_dim) for y in range(self.maze_dim) for x in range(self.maze_dim)])
        while True:
            while len(pq) > 0 and pq.peek()[:2] in visited:
                pq.pop()
            if len(pq) > 0:
                y, x, dist, sc = pq.pop()
                visited[(y, x)] = True
                if x + 1 < self.maze_dim and (y, x + 1) not in visited and not self.maze_matrix[y][x + 1][1] and distances[(y, x + 1)] > dist + 1:
                    distances[(y, x + 1)] = dist + 1
                    parents[(y, x + 1)] = (y, x)
                    pq.push((y, x + 1, dist + 1, dist + 1 + 2 * (self.maze_dim - 1) - y - (x + 1)))
                if y + 1 < self.maze_dim and (y + 1, x) not in visited and not self.maze_matrix[y + 1][x][0] and distances[(y + 1, x)] > dist + 1:
                    distances[(y + 1, x)] = dist + 1
                    parents[(y + 1, x)] = (y, x)
                    pq.push((y + 1, x, dist + 1, dist + 1 + 2 * (self.maze_dim - 1) - (y + 1) - x))
                if x > 0 and (y, x - 1) not in visited and not self.maze_matrix[y][x][1] and distances[(y, x - 1)] > dist + 1:
                    distances[(y, x - 1)] = dist + 1
                    parents[(y, x - 1)] = (y, x)
                    pq.push((y, x - 1, dist + 1, dist + 1 + 2 * (self.maze_dim - 1) - y - (x - 1)))
                if y > 0 and (y - 1, x) not in visited and not self.maze_matrix[y][x][0] and distances[(y - 1, x)] > dist + 1:
                    distances[(y - 1, x)] = dist + 1
                    parents[(y - 1, x)] = (y, x)
                    pq.push((y - 1, x, dist + 1, dist + 1 + 2 * (self.maze_dim - 1) - (y - 1) - x))
            else:
                break

        y_start, x_start = self.maze_dim - 1, self.maze_dim - 1
        while True:
            self.solution.append((y_start, x_start))
            if not (y_start == 0 and x_start == 0):
                y_start, x_start = parents[(y_start, x_start)]
            else:
                break


if __name__ == '__main__':
    maze = Maze(3)
    maze.build()
    solver = SolverAStarSearch(maze)
    solver.solve()
    print(maze)
    print(solver.get_solution())
