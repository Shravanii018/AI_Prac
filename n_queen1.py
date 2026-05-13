def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


def solve_n_queens(n):

    board = [-1] * n

    col = [False] * n
    diag1 = [False] * (2 * n)
    diag2 = [False] * (2 * n)

    def solve(row):

        if row == n:
            print_solution(board, n)
            return

        for c in range(n):

            if not col[c] and not diag1[row + c] and not diag2[row - c + n]:

                # Place queen
                board[row] = c
                col[c] = True
                diag1[row + c] = True
                diag2[row - c + n] = True

                # Recursive call
                solve(row + 1)

                # Backtracking
                col[c] = False
                diag1[row + c] = False
                diag2[row - c + n] = False


    solve(0)


# Driver code
n = int(input("Enter value of N: "))
solve_n_queens(n)