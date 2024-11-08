class Game:
    def __init__(self):
        self.field = [[1, 2, 3, 4, 5, 3, 2, 1],
                      [7, 7, 7, 7, 7, 7, 7, 7],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [8, 8, 8, 8, 8, 8, 8, 8],
                      [11, 12, 13, 14, 15, 13, 12, 11]]

        self.turn = "BLACK"

    def get_legal_moves(self, piece_id, x, y):
        possible_moves = []
        if (piece_id >= 8 and self.turn == "BLACK") or (piece_id <= 7 and self.turn == "WHITE"):
            return []

        if piece_id == 8:
            possible_moves.append([x, y - 1])
        elif piece_id == 7:
            possible_moves.append([x, y + 1])
        if piece_id == 5 or piece_id == 15:
            for row in range(8):
                for column in range(8):
                    current_element = self.field[column][row]
                    if current_element == 0:
                        possible_moves.append([row, column])
        if piece_id == 2 or piece_id == 12:
            possible_moves.append([x, y + 2])
            possible_moves.append([x, y - 2])
            possible_moves.append([x + 2, y])
            possible_moves.append([x - 2, y])

            print()

        return possible_moves

    def move(self, figure, goal):
        if self.field[figure[0]][figure[1]] in [2, 12]:
            direction = [goal[0] - figure[0], goal[1] - figure[1]]
            print(direction)
            if direction[0] == -2:
                self.field[goal[0] + 1][goal[1]] = 0
            elif direction[0] == 2:
                self.field[goal[0] - 1][goal[1]] = 0
            elif direction[1] == -2:
                self.field[goal[0]][goal[1] + 1] = 0
            elif direction[1] == 2:
                self.field[goal[0]][goal[1] - 1] = 0

        self.field[goal[0]][goal[1]] = self.field[figure[0]][figure[1]]
        self.field[figure[0]][figure[1]] = 0

        if self.turn == "WHITE":
            self.turn = "BLACK"
        else:
            self.turn = "WHITE"

