import pygame
import random
from basic_version import print_board, is_valid, find_empty, random_sudoku, solved
import time
from datetime import datetime


now = datetime.now()

easy = 10000
medium = 1000
hard = 81
fast = 20

sodoku_difficulty = hard

clock_delay = 0
pygame.font.init()
pygame.init()
WIDTH = 548
HEIGHT = 610
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")


def message_to_screen(msg, x, y, color=(0, 0, 0), font_size=40):
    screen_text = pygame.font.SysFont(None, font_size).render(msg, True, color)
    screen.blit(screen_text, (int(x), int(y)))



class Game_board():

    def __init__(self, board, width=60, height=60):
        self.board = board
        self.width = width
        self.height = height
        self.selection = None
        self.player_ans = [[0 for i in range(9)] for j in range(9)]
        self.player_assum = [[0 for i in range(9)] for j in range(9)]

    def guess(self, position, value):
        self.board[position[0]][position[1]] = value

    def select(self, r, c):
        for i in range(9):
            for j in range(9):
                self.selection = None

        self.selection = [r, c]

    def highlight(self):
        if self.selection:
            if self.selection[0] < 9:
                pygame.draw.line(screen, (255, 0, 0), (self.selection[1] * self.width, self.selection[0] * self.height),
                                 ((self.selection[1] + 1) * self.width, self.selection[0] * self.height), 5)
                pygame.draw.line(screen, (255, 0, 0), (self.selection[1] * self.width, self.selection[0] * self.height),
                                 (self.selection[1] * self.width, (self.selection[0] + 1) * self.height), 5)
                pygame.draw.line(screen, (255, 0, 0),
                                 ((self.selection[1] + 1) * self.width, (self.selection[0] + 1) * self.height),
                                 ((self.selection[1]) * self.width, (self.selection[0] + 1) * self.height), 5)
                pygame.draw.line(screen, (255, 0, 0),
                                 ((self.selection[1] + 1) * self.width, (self.selection[0] + 1) * self.height),
                                 ((self.selection[1] + 1) * self.width, (self.selection[0]) * self.height), 5)

            else:
                pygame.draw.line(screen, (0, 255, 0), (self.selection[1] * self.width, self.selection[0] * self.height),
                                 ((self.selection[1] + 1) * self.width, self.selection[0] * self.height), 5)
                pygame.draw.line(screen, (0, 255, 0), (self.selection[1] * self.width, self.selection[0] * self.height),
                                 (self.selection[1] * self.width, (self.selection[0] + 1) * self.height), 5)
                pygame.draw.line(screen, (0, 255, 0),
                                 ((self.selection[1] + 1) * self.width, (self.selection[0] + 1) * self.height),
                                 ((self.selection[1]) * self.width, (self.selection[0] + 1) * self.height), 5)
                pygame.draw.line(screen, (0, 255, 0),
                                 ((self.selection[1] + 1) * self.width, (self.selection[0] + 1) * self.height),
                                 ((self.selection[1] + 1) * self.width, (self.selection[0]) * self.height), 5)

    def all_ans(self, val):
        if self.selection == [9, 0]:
            self.player_assum = [[val for i in range(9)] for i in range(9)]

    def poss_ans(self, val):
        if self.selection == [9, 1]:
            for r in range(9):
                for c in range(9):
                    if (self.board[r][c] == 0 and self.player_ans[r][c] == 0) and (
                            is_valid(self.player_ans, val, [r, c]) and is_valid(self.board, val, [r, c])):
                        self.player_assum[r][c] = val
                        # print(r,c)
                        # print("board", self.board)
                        # print("answer", self.player_ans)

    def one_more_val(self):
        if self.selection == [9, 2]:
            while True:
                a = random.randint(0, 8)
                b = random.randint(0, 8)
                if self.board[a][b] == 0:
                    self.board[a][b] = copy_board[a][b]
                    break

    def check_ans(self):
        if self.selection == [9, 3]:
            for r in range(9):
                for c in range(9):
                    if self.player_assum[r][c] != 0:
                        if self.player_assum[r][c] == copy_board[r][c]:
                            self.player_ans[r][c] = self.player_assum[r][c]
                        else:
                            self.player_assum[r][c] = "X"

    def draw_grid(self):
        for row in range(10):
            if row % 3 == 0:
                pygame.draw.line(screen, (0, 0, 0), (0, self.height * row), (9 * self.width, self.height * row), 3)
            else:
                pygame.draw.line(screen, (0, 0, 0), (0, self.height * row), (9 * self.width, self.height * row))

        for col in range(10):
            if col % 3 == 0:
                pygame.draw.line(screen, (0, 0, 0), (self.width * col + 2, 0), (self.width * col + 2, self.width * 9),
                                 3)

            else:
                pygame.draw.line(screen, (0, 0, 0), (self.width * col + 2, 0), (self.width * col + 2, self.width * 9))

        # pygame.draw.line(screen, (0, 255, 0), (2, HEIGHT-4), (2, HEIGHT-4 - self.height),3)
        # pygame.draw.line(screen, (0, 255, 0), (2, HEIGHT-4), (2 + self.width, HEIGHT-4),3)
        # pygame.draw.line(screen, (0, 255, 0), (2 + self.width, HEIGHT-4 - self.height), (2 + self.width, HEIGHT-4),3)
        # pygame.draw.line(screen, (0, 255, 0), (2 + self.width, HEIGHT-4 - self.height), (2, HEIGHT-4 - self.height),3)

    def fill_in_board(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != 0:
                    message_to_screen(str(self.board[row][col]), self.width * (col + 0.4), self.height * (row + 0.3))
        for row in range(9):
            for col in range(9):
                if self.player_assum[row][col] != 0 and (self.board[row][col] == 0 and self.player_ans[row][col] == 0):
                    message_to_screen(str(self.player_assum[row][col]), self.width * (col + 0.4),
                                      self.height * (row + 0.3), (0, 200, 0))
        for row in range(9):
            for col in range(9):
                if self.player_ans[row][col] != 0 and self.board[row][col] == 0:
                    message_to_screen(str(self.player_ans[row][col]), self.width * (col + 0.4),
                                      self.height * (row + 0.3), (0, 70, 0))

    def player_fill(self, val):
        if self.selection and self.selection[0] < 9:
            r = self.selection[0]
            c = self.selection[1]
            if self.board[r][c] == 0:
                self.player_assum[r][c] = val

    def win(self):
        temp_board = [x[:] for x in self.board]

        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0 and self.player_ans[row][col] != 0:
                    temp_board[row][col] = self.player_ans[row][col]

        if find_empty(temp_board):
            return False
        else:
            for r in range(9):
                for c in range(9):
                    if not is_valid(temp_board, temp_board[c][r], (c, r)):
                        return False
            return True

run = True
reset = True
count = 0


while run:
    while reset == True:
        random_board = random_sudoku(sodoku_difficulty)

        copy_board = [x[:] for x in random_board]
        count += 1
        print(f"Solving sudoku #{count}...")
        if solved(copy_board):
            print(random_board)
            game = Game_board(random_board)
            reset = False
            with open("history", "a") as f:
                f.write(f"{now.strftime('%m/%d/%Y %H:%M:%S')}\n")
                f.write("Board: \n")
                for line in random_board:
                    f.write(f"{line} \n")
                f.write("Solution: \n")
                for line in copy_board:
                    f.write(f"{line} \n")

        a = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                key = 1
                game.player_fill(key)
                game.all_ans(key)
                game.poss_ans(key)
            elif event.key == pygame.K_2:
                key = 2
                game.player_fill(key)
                game.all_ans(key)
                game.poss_ans(key)
            elif event.key == pygame.K_3:
                key = 3
                game.player_fill(key)
                game.all_ans(key)
                game.poss_ans(key)
            elif event.key == pygame.K_4:
                key = 4
                game.player_fill(key)
                game.all_ans(key)
                game.poss_ans(key)
            elif event.key == pygame.K_5:
                key = 5
                game.player_fill(key)
                game.all_ans(key)
                game.poss_ans(key)
            elif event.key == pygame.K_6:
                key = 6
                game.player_fill(key)
                game.all_ans(key)
                game.poss_ans(key)
            elif event.key == pygame.K_7:
                key = 7
                game.player_fill(key)
                game.all_ans(key)
                game.poss_ans(key)
            elif event.key == pygame.K_8:
                key = 8
                game.player_fill(key)
                game.all_ans(key)
                game.poss_ans(key)
            elif event.key == pygame.K_9:
                key = 9
                game.player_fill(key)
                game.all_ans(key)
                game.poss_ans(key)
            elif event.key == pygame.K_0:
                key = 0
                game.player_fill(key)
                game.all_ans(key)
            elif event.key == pygame.K_UP:
                if game.selection and game.selection[0] != 0:
                    idx = game.selection[0]
                    game.selection[0] = idx - 1
                elif game.selection:
                    game.selection[0] = 8
            elif event.key == pygame.K_DOWN:
                if game.selection and game.selection[0] != 8:
                    idx = game.selection[0]
                    game.selection[0] = idx + 1
                elif game.selection:
                    game.selection[0] = 0
            elif event.key == pygame.K_LEFT:
                if game.selection and game.selection[1] != 0:
                    idx = game.selection[1]
                    game.selection[1] = idx - 1
                elif game.selection:
                    game.selection[1] = 8
            elif event.key == pygame.K_RIGHT:
                if game.selection and game.selection[1] != 8:
                    idx = game.selection[1]
                    game.selection[1] = idx + 1
                elif game.selection:
                    game.selection[1] = 0

            elif event.key == pygame.K_BACKSPACE:
                game.player_ans[game.selection[0]][game.selection[1]] = 0

            elif event.key == pygame.K_EQUALS:
                game.player_ans = copy_board

            elif event.key == pygame.K_RETURN:
                if game.selection:
                    game.one_more_val()
                    game.check_ans()
                    r = game.selection[0]
                    c = game.selection[1]
                    if r < 9 and game.player_assum[r][c] != 0:
                        game.player_ans[r][c] = game.player_assum[r][c]

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            c = pos[0] // game.width
            r = pos[1] // game.height
            if c <= 8 and r <= 8:
                game.select(r, c)
            if c < 4 and r == 9:
                game.select(r, c)

    screen.fill((250, 250, 250))

    game.draw_grid()
    game.fill_in_board()
    game.highlight()

    if not game.win():

        message_to_screen("All", game.width * (0 + 0.4), game.height * (9 + 0.3), (90, 70, 30), 20)
        message_to_screen("Poss", game.width * (1 + 0.4) - 2, game.height * (9 + 0.3), (90, 70, 30), 20)
        message_to_screen("Add", game.width * (2 + 0.4) - 2, game.height * (9 + 0.3), (90, 70, 30), 20)
        message_to_screen("Check", game.width * (3 + 0.4) - 4, game.height * (9 + 0.3), (90, 70, 30), 20)

        b = time.time() - a - clock_delay
        if b // 60 < 10 and int(b % 60) < 10:
            message_to_screen(f"TIME: 0{int(b // 60)}:0{int(b % 60)}", 300, 550)

        elif b // 60 < 10 and int(b % 60) >= 10:
            message_to_screen(f"TIME: 0{int(b // 60)}:{int(b % 60)}", 300, 550)

        elif b // 60 >= 10 and int(b % 60) < 10:
            message_to_screen(f"TIME: {int(b // 60)}:0{int(b % 60)}", 300, 550)

        elif b // 60 >= 10 and int(b % 60) >= 10:
            message_to_screen(f"TIME: {int(b // 60)}:{int(b % 60)}", 300, 550)

    else:
        c = b
        message_to_screen(
            f"Congratulation you won! The time you spent on the sudoku is {int(c // 60)}:{int(c % 60)}", 0,
            HEIGHT - 50, (0, 0, 255), 24)

        with open("best_time_score", "r") as rf:
            try:
                current_score = float(rf.readline())
            except:
                current_score = 99999999
            if current_score > c:
                with open("best_time_score", "w") as wf:
                    wf.write(str(c))
        pygame.display.flip()
        time.sleep(5)

    pygame.display.flip()





