import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 12
        num_cols = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                len(m1._cells),
                num_cols,
            )
        self.assertEqual(
                len(m1._cells[0]),
                num_rows,
            )

    def test_maze_create_cells_large(self):
        num_rows = 12
        num_cols = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                len(m1._cells),
                num_cols,
            )
        self.assertEqual(
                len(m1._cells[0]),
                num_rows,
            )

    def test_break_entrance_and_exit(self):
        num_rows = 12
        num_cols = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

    def test_cell_reset_visited(self):
        num_rows = 12
        num_cols = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        num_reset = 0
        for column in m1._cells:
            for cell in column:
                if not cell.visited:
                    num_reset += 1
        self.assertEqual(
                num_reset,
                num_rows * num_cols,
            )

if __name__ == "__main__":
    unittest.main()
