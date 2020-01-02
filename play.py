import sys
import os

sys.path.append('gui/api')
sys.path.append('gui/res')

from colors import color_list
from window import Window
from utils import draw_maze
from utils import get_solver_thread
from solveDFS import SolverDFS
from maze import Maze


def play(dim=20):
    display_window_width = 1050
    display_window_height = 710
    maze_size = 580
    partition = 720
    cell_size = maze_size // dim
    maze_offset_x = (partition - cell_size * dim) // 2
    maze_offset_y = (display_window_height - cell_size * dim) // 2
    border_width = int(20 / dim + 1.7)

    display_window = Window(display_window_width, display_window_height,
                            caption='Maze')

    maze = Maze(dim)
    maze.build()

    draw_maze(display_window, maze, maze_offset_x, maze_offset_y,
              cell_size, border_width, precision=False if dim > 35 else True)


    solver = SolverDFS(maze)
    solver_thread = get_solver_thread(display_window, solver, maze, maze_offset_x, maze_offset_y, cell_size, border_width, fps=15)

    arguments = {'solver_thread': solver_thread}
    def solve(solver_thread):
        solver_thread.start()

    action = {'callable': solve, 'arguments': arguments}
    solution_rect = display_window.draw_textbox((partition + display_window_width) / 2.08, display_window_height / 2 - 30, 'See solution', color=color_list['dark_gray'], size=52, action=action, fontstyle='rasa', underline=True)

    arguments = {'window': display_window, 'x': 0, 'y': 0, 'width': partition,
                 'height': display_window_height, 'filepath': (os.path.join(os.getcwd(), 'export', 'maze.jpeg'))}
    def save(window, x, y, width, height, filepath): 
        window.capture_rect(x, y, width, height, filepath)

    action = {'callable': save, 'arguments': arguments}
    save_rect = display_window.draw_textbox((partition + display_window_width) / 2.08, display_window_height / 2 + 30,
                                            'Export Maze', color=color_list['dark_gray'], size=32, action=action, fontstyle='rasa', underline=True, italic=False)

    display_window.show()


def main():
    if len(sys.argv) == 1:
        play(40)
    else:
        DIM = int(sys.argv[1][1:])
        if DIM > 50 or DIM < 1:
            print("Please enter a dimension between 1 and 50")
        else:
            play(DIM)


if __name__ == '__main__':
    main()
