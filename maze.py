
''' Define recursive maze generation algorithm '''

import random


class Maze():

    density_factor = 8
    intersection_factor = 600000000

    def __init__(self, DIM):
        self.DIM = DIM
        self.maze_matrix = []
        for i in range(self.DIM + 1):
            self.maze_matrix.append([])
            for j in range(self.DIM + 1):
                self.maze_matrix[i].append([False, False])

    def merge_maze(self, beg_r, beg_c, end_r, end_c, simplemerge=True):
        if beg_r == end_r:
            self.maze_matrix[beg_r][random.randint(
                beg_c, end_c - 1)][0] = False
            for i in range(beg_c, end_c):
                decision = random.randint(1, 1000000)
                if decision % self.density_factor == 0:
                    self.maze_matrix[beg_r][i][0] = False

            if not simplemerge:
                sum_array = [0]
                curr_sum = 0
                for i in range(beg_c, end_c):
                    curr_sum += int(self.maze_matrix[beg_r][i][0])
                    sum_array.append(curr_sum)

                last_block = beg_c
                for i in range(beg_c + 1, end_c - 1):
                    if sum_array[i - beg_c] - sum_array[last_block - beg_c] < i - last_block and sum_array[end_c - beg_c] - sum_array[i - beg_c] < end_c - i:
                        decision = random.randint(1, 1000000)
                        if decision % self.intersection_factor != 0:
                            self.maze_matrix[beg_r][i][1] = True
                            last_block = i

        else:
            self.maze_matrix[random.randint(
                beg_r, end_r - 1)][beg_c][1] = False
            for i in range(beg_r, end_r):
                decision = random.randint(1, 1000000)
                if decision % self.density_factor == 0:
                    self.maze_matrix[i][beg_c][1] = False

            if not simplemerge:
                sum_array = [0]
                curr_sum = 0
                for i in range(beg_r, end_r):
                    curr_sum += int(self.maze_matrix[i][beg_c][1])
                    sum_array.append(curr_sum)

                last_block = beg_r
                for i in range(beg_r + 1, end_r - 1):
                    if sum_array[i - beg_r] - sum_array[last_block - beg_r] < i - last_block and sum_array[end_r - beg_r] - sum_array[i - beg_r] < end_r - i:
                        decision = random.randint(1, 1000000)
                        if decision % self.intersection_factor != 0:
                            self.maze_matrix[i][beg_c][0] = True
                            last_block = i

    def build_maze(self, beg_r, beg_c, end_r, end_c):
        for i in range(beg_c, end_c):
            self.maze_matrix[beg_r][i][0] = True
            self.maze_matrix[end_r][i][0] = True

        for i in range(beg_r, end_r):
            self.maze_matrix[i][beg_c][1] = True
            self.maze_matrix[i][end_c][1] = True

        verical_dim = end_r - beg_r
        horizontal_dim = end_c - beg_c

        if not (verical_dim == 1 or horizontal_dim == 1):
            decision = random.randint(0, 1)
            if decision == 0:
                if horizontal_dim % 2 == 0:
                    self.build_maze(beg_r, beg_c, end_r,
                                    beg_c + horizontal_dim // 2)
                    self.build_maze(
                        beg_r, beg_c + horizontal_dim // 2, end_r, end_c)
                    self.merge_maze(beg_r, beg_c + horizontal_dim //
                                    2, end_r, beg_c + horizontal_dim // 2, True)
                else:
                    self.build_maze(beg_r, beg_c, end_r, end_c - 1)
                    self.merge_maze(beg_r, end_c - 1, end_r, end_c - 1, False)
            else:
                if verical_dim % 2 == 0:
                    self.build_maze(beg_r, beg_c, beg_r +
                                    verical_dim // 2, end_c)
                    self.build_maze(beg_r + verical_dim //
                                    2, beg_c, end_r, end_c)
                    self.merge_maze(beg_r + verical_dim // 2, beg_c,
                                    beg_r + verical_dim // 2, end_c, True)
                else:
                    self.build_maze(beg_r, beg_c, end_r - 1, end_c)
                    self.merge_maze(end_r - 1, beg_c, end_r - 1, end_c, False)

    def build(self):
        self.build_maze(0, 0, self.DIM, self.DIM)

    def get_maze_matrix(self):
        return self.maze_matrix

    def get_maze_dim(self):
        return self.DIM

    def __repr__(self):
        return 'Maze({})'.format(self.DIM)

    def __str__(self):
        out = ''
        for i in range(self.DIM + 1):
            line_horizontal = ' '
            for j in range(self.DIM + 1):
                line_horizontal += '-- ' if self.maze_matrix[i][j][0] else '   '
            out += line_horizontal + '\n'

            line_vertical = ''
            for j in range(self.DIM + 1):
                line_vertical += '|  ' if self.maze_matrix[i][j][1] else '   '
            out += line_vertical + '\n'

        return out


if __name__ == '__main__':
    maze = Maze(20)
    maze.build()
    print(maze)
