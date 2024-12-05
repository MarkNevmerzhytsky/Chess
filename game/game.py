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
        self.turn_counter = 0

    def get_legal_moves(self, piece_id, x, y):
        figure_color = "BLACK" if piece_id <= 7 else "WHITE"
        possible_moves = []
        if (figure_color == "WHITE" and self.turn == "BLACK") or (figure_color == "BLACK" and self.turn == "WHITE"):
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
            if y + 2 < 8:
                possible_moves.append([x, y + 2])
            if y - 2 >= 0:
                possible_moves.append([x, y - 2])
            if x + 2 < 8:
                possible_moves.append([x + 2, y])
            if x - 2 >= 0:
                possible_moves.append([x - 2, y])
        if piece_id == 1 or piece_id == 11:
            possible_moves = self.get_vertical_moves(x, y, figure_color, 8, 1)
            possible_moves.extend(self.get_vertical_moves(x, y, figure_color, -1, -1))
            #possible_moves.extend(self.get_horizontal_moves(x, y, figure_color, 8, 1))
            #possible_moves.extend(self.get_horizontal_moves(x, y, figure_color, -1, -1))

        moves_to_remove = []
        for possible_move in possible_moves:
            destination_color = "BLACK" if 0 < self.field[possible_move[1]][possible_move[0]] <= 7 else "WHITE" if \
                self.field[possible_move[1]][possible_move[0]] >= 8 else "BLANK"

            if (figure_color == "BLACK" and destination_color == "BLACK") or (
                    figure_color == "WHITE" and destination_color == "WHITE"):
                moves_to_remove.append(possible_move)

        print(moves_to_remove)
        for move in moves_to_remove:
            possible_moves.remove(move)

        return possible_moves

    def get_vertical_moves(self, x, y, figure_color, j, direction):
        possible_moves = []
        for i in range(y, j, direction):
            current_element = self.field[x][i]
            if i == y:
                continue
            if current_element == 0:
                possible_moves.append([x, i])
            elif current_element >= 8 and figure_color == "WHITE" or (current_element <= 7 and figure_color == "BLACK"):
                break
            elif current_element >= 8 and figure_color == "BLACK" or (current_element <= 7 and figure_color == "WHITE"):
                possible_moves.append([x, i])
                break
        return possible_moves

    # def get_horizontal_moves(self, x, y, figure_color, j, direction):
    #     possible_moves = []
    #     for i in range(x, j, direction):
    #         current_element = self.field[i][x]
    #         if i == x:
    #             continue
    #         if current_element == 0:
    #             possible_moves.append([i, y])
    #         elif current_element >= 8 and figure_color == "WHITE" or (current_element <= 7 and figure_color == "BLACK"):
    #             break
    #         elif current_element >= 8 and figure_color == "BLACK" or (current_element <= 7 and figure_color == "WHITE"):
    #             possible_moves.append([i, y])
    #             break
    #     return possible_moves

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

        self.turn_counter += 1

        if self.turn_counter == 2:
            self.turn_counter = 0

            if self.turn == "WHITE":
                self.turn = "BLACK"
            else:
                self.turn = "WHITE"
