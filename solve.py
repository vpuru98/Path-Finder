
''' Define abstract Solver Class '''


class Solver():


    def __init__(self, maze):
        self.maze_matrix = maze.get_maze_matrix()
        self.maze_dim = maze.get_maze_dim()
        self.maze = maze
        self.solution = []


    def solve(self):
        pass


    def get_solution(self):
        return self.solution


    def __repr__(self):
        return 'Solver({})'.format(repr(self.maze))
