
from solve import Solver
from maze import Maze


class SolverDFS(Solver):

    MAX = 1000000000

    def __init__(self, maze):
        super().__init__(maze)

    def solveDFS(self, visited, source_y, source_x):
        visited[source_y][source_x] = True
        if source_y == self.maze_dim - 1 and source_x == self.maze_dim - 1:
            return [(source_y, source_x)]
        else:
            if source_x + 1 < self.maze_dim and not visited[source_y][source_x + 1] and not self.maze_matrix[source_y][source_x + 1][1]:
                path = self.solveDFS(visited, source_y, source_x + 1)
                if len(path) > 0:
                    path.append((source_y, source_x))
                    return path
            if source_y + 1 < self.maze_dim and not visited[source_y + 1][source_x] and not self.maze_matrix[source_y + 1][source_x][0]:
                path = self.solveDFS(visited, source_y + 1, source_x)
                if len(path) > 0:
                    path.append((source_y, source_x))
                    return path
            if source_x > 0 and not visited[source_y][source_x - 1] and not self.maze_matrix[source_y][source_x][1]:
                path = self.solveDFS(visited, source_y, source_x - 1)
                if len(path) > 0:
                    path.append((source_y, source_x))
                    return path
            if source_y > 0 and not visited[source_y - 1][source_x] and not self.maze_matrix[source_y][source_x][0]:
                path = self.solveDFS(visited, source_y - 1, source_x)
                if len(path) > 0:
                    path.append((source_y, source_x))
                    return path

            return []

    def solve(self):
        visited = []
        for i in range(self.maze_dim):
            visited.append([])
            for j in range(self.maze_dim):
                visited[i].append(False)

        self.solution = self.solveDFS(visited, 0, 0)


if __name__ == '__main__':
    maze = Maze(3)
    maze.build()
    solver = SolverDFS(maze)
    solver.solve()
    print(solver.get_solution())
