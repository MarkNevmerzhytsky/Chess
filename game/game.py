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

    def get_legal_moves(self, piece_id, x, y):
        possible_moves = []
        if piece_id == 8:
            possible_moves.append([x, y - 1])
        elif piece_id == 7:
            possible_moves.append([x, y + 1])

        return possible_moves

    def move(self, figure, goal):
        self.field[goal[0]][goal[1]] = self.field[figure[0]][figure[1]]
        self.field[figure[0]][figure[1]] = 0
