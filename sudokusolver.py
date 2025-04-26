import time

def solve_sudoku(grid):
    values = {(i, j): str(grid[i][j]) if grid[i][j] != 0 else "123456789"
              for i in range(9) for j in range(9)}
    
    peers = {}
    for i in range(9):
        for j in range(9):
            row = [(i, c) for c in range(9)]
            col = [(r, j) for r in range(9)]
            block = [(3*(i//3) + dr, 3*(j//3) + dc) for dr in range(3) for dc in range(3)]
            peers[(i, j)] = set(row + col + block) - {(i, j)}

    def reduce(values):
        stuck = False
        while not stuck:
            solved = [k for k in values if len(values[k]) == 1]
            before = sum(len(values[k]) for k in values)
            for k in solved:
                for p in peers[k]:
                    if values[k] in values[p]:
                        values[p] = values[p].replace(values[k], '')
                        if len(values[p]) == 0:
                            return None
            after = sum(len(values[k]) for k in values)
            stuck = before == after
        return values

    def search(values):
        values = reduce(values)
        if values is None:
            return None
        if all(len(v) == 1 for v in values.values()):
            return values
        k = min((k for k in values if len(values[k]) > 1), key=lambda x: len(values[x]))
        for num in values[k]:
            attempt = values.copy()
            attempt[k] = num
            result = search(attempt)
            if result:
                return result
        return None

    reduced = reduce(values)
    final = search(reduced)
    if final:
        return [[int(final[(i, j)]) for j in range(9)] for i in range(9)]
    return None

if __name__ == "__main__":
    puzzle = [
        [0, 1, 0, 5, 0, 8, 0, 0, 6],
        [0, 0, 8, 1, 0, 0, 0, 0, 0],
        [0, 7, 5, 0, 6, 0, 8, 1, 0],
        [0, 8, 0, 0, 0, 0, 1, 9, 0],
        [0, 3, 0, 0, 0, 0, 0, 6, 0],
        [0, 5, 2, 0, 0, 0, 0, 8, 0],
        [0, 6, 7, 0, 5, 0, 4, 3, 0],
        [0, 0, 0, 0, 0, 9, 7, 0, 0],
        [8, 0, 0, 7, 0, 4, 0, 5, 0]
    ]

    print("Original puzzle:")
    for row in puzzle:
        print(row)

    start = time.time()
    solved = solve_sudoku(puzzle)
    end = time.time()

    if solved:
        for row in solved:
            print(row)
        print(f"\nSolved in {end - start:.4f} seconds")
    else:
        print("\nNo solution exists")
