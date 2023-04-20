from cell import Cell
import random
import time

class Maze:
    def __init__(self, 
                 x1, 
                 y1, 
                 num_rows, 
                 num_columns, 
                 cell_size_x, 
                 cell_size_y, 
                 win=None, 
                 seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_columns
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)

        self._create_cells()

    def solve(self):
        self._solve_r(0,0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # Check left
        if (
            i > 0
            and not self._cells[i - 1][j].visited
            and not self._cells[i][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # Check right
        if (
            i < self._num_cols - 1
            and not self._cells[i + 1][j].visited
            and not self._cells[i][j].has_right_wall
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # Check top
        if (
            j > 0 
            and not self._cells[i][j - 1].visited
            and not self._cells[i][j].has_top_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # Check top
        if (
            j < self._num_rows - 1 
            and not self._cells[i][j + 1].visited
            and not self._cells[i][j].has_bottom_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False


    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        
        self._break_entrance_and_exit()
        self._break_cells_r(0, 0)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)

        self._reset_cells_visited()

    def _draw_cell(self, i, j):
        if self._win == None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False     
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False

    def _break_cells_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            possible_dir = 0

            # check if i or j is in bounds of the Maze
            # check if adjacent cells have been visited
            # add to next index next_index_list

            # check left
            if i > 0 and not self._cells[i - 1][j].visited:
                # append tuple to store cell coords
                next_index_list.append((i - 1, j))
                possible_dir += 1

            # check right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
                possible_dir += 1

            # check up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i,j - 1))
                possible_dir += 1

            # check down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))
                possible_dir += 1

            # If there are no directions to go return
            if possible_dir == 0:
                return

            dir_idx = random.randrange(possible_dir)
            next_idx = next_index_list[dir_idx]

            # next check where the next index is in relation to the current idx
            # and break down the walls

            # right
            if next_idx[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            # left
            if next_idx[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False

            # bottom
            if next_idx[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            
            # top
            if next_idx[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_cells_r(next_idx[0], next_idx[1])

    # Reset the cells visited
    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column: 
                cell.visited = False




















