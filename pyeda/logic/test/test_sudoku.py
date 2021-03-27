"""
Test logic functions for Sudoku
"""

import os

from pyeda.logic.sudoku import SudokuSolver


def test_sudoku(solver, grids, solns):
    """
    params:
        solver:
        grids:
        solns:
    """
    for i, grid in enumerate(grids):
        assert solver.display_solve(grid) == solns[i]


if __name__ == '__main__':

    SOLVER = SudokuSolver()

    cwd, _ = os.path.split(__file__)
    top95_txt = os.path.join(cwd, 'top95.txt')
    top95_solns_txt = os.path.join(cwd, 'top95_solns.txt')
    with open(top95_txt) as fin:
        GRIDS = [line.strip() for line in fin]
    with open(top95_solns_txt) as fin:
        SOLNS = [line.strip() for line in fin]
    params = {
        "solver": SOLVER,
        "grids": GRIDS,
        "solns": SOLNS
    }
    test_sudoku(*params)
