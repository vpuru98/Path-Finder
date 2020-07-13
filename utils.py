

''' Utility functions for rendering maze '''

from gui.res.colors import color_list
import threading
import time


def draw_maze(window, maze, maze_position_x, maze_position_y, cell_size,
              border_width, shadow_width=1, border_color=color_list['dark_gray'],
              shadow_color=color_list['light_gray'], precision=True):

    dim = maze.get_maze_dim()
    maze_matrix = maze.get_maze_matrix()

    def fill_gaps():
        for i in range(dim + 1):
            for j in range(dim + 1):
                x_cor = maze_position_x + j * cell_size
                y_cor = maze_position_y + i * cell_size

                if maze_matrix[i][j][0]:
                    if i > 0 and j < dim and maze_matrix[i - 1][j + 1][1]:
                        window.draw_rect(
                            x_cor + cell_size, y_cor, border_width // 2, border_width // 2, border_color)
                    if i > 0 and maze_matrix[i - 1][j][1]:
                        window.draw_rect(x_cor - border_width // 2, y_cor,
                                         border_width // 2, border_width // 2, border_color)

                if maze_matrix[i][j][1]:
                    if maze_matrix[i][j][0]:
                        window.draw_rect(x_cor - border_width // 2, y_cor -
                                         border_width // 2, border_width // 2, border_width
                                         // 2, border_color)
                    if j > 0 and maze_matrix[i][j - 1][0]:
                        window.draw_rect(x_cor, y_cor - border_width // 2,
                                         border_width // 2, border_width // 2, border_color)

    def draw_shadows():
        for i in range(dim + 1):
            for j in range(dim + 1):
                x_cor = maze_position_x + j * cell_size
                y_cor = maze_position_y + i * cell_size

                if j < dim:
                    window.draw_rect(x_cor, y_cor - shadow_width //
                                     2, cell_size, shadow_width, shadow_color)
                if i < dim:
                    window.draw_rect(x_cor - shadow_width // 2,
                                     y_cor, shadow_width, cell_size, shadow_color)

    def draw_borders():
        for i in range(dim + 1):
            for j in range(dim + 1):
                x_cor = maze_position_x + j * cell_size
                y_cor = maze_position_y + i * cell_size

                if maze_matrix[i][j][0]:
                    window.draw_rect(x_cor, y_cor - border_width //
                                     2, cell_size, border_width, border_color)
                if maze_matrix[i][j][1]:
                    window.draw_rect(x_cor - border_width // 2,
                                     y_cor, border_width, cell_size, border_color)

    def draw_maze():
        draw_shadows()
        draw_borders()

    draw_maze()
    if precision:
        fill_gaps()


def mark_cell(window, cell_x, cell_y, cell_size, border_width, color=color_list['shade'],           mark_size_factor=0.4):
    mark_dim = int(cell_size * mark_size_factor)
    window.draw_rect(cell_x + (cell_size - mark_dim) // 2, cell_y + (cell_size -
                                                                     mark_dim) // 2, mark_dim, mark_dim, color)


def get_solver_thread(window, solver, maze, maze_position_x, maze_position_y, cell_size, border_width, fps=30):

    def thread_func(window, trace, maze_offset_x, maze_offset_y, cell_size, border_width, fps):
        while len(trace):
            cell_y, cell_x = trace.pop()
            mark_cell(window, maze_offset_x + cell_x * cell_size, maze_offset_y + cell_y * cell_size, cell_size, border_width)
            time.sleep(1 / fps)
        while True:
        	pass

    solver.solve()
    trace = solver.get_solution()
    solver_thread = threading.Thread(target=thread_func, args=(window, trace, maze_position_x, maze_position_y, cell_size, border_width, fps))
    solver_thread.daemon = True

    return solver_thread
