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
            pass

        return possible_moves
