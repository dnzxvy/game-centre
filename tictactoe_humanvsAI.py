import tkinter as tk
from tkinter import messagebox
import random


class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        
        self.board = [' ' for _ in range(9)]
        self.current_turn = 'X'
        
        self.buttons = []
        for i in range(9):
            row, col = divmod(i, 3)
            button = tk.Button(master, text='', font=('normal', 20), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=row, column=col)
            self.buttons.append(button)

    def make_move(self, square):
        if self.board[square] == ' ':
            self.board[square] = self.current_turn
            self.buttons[square].config(text=self.current_turn)
            if self.check_winner(square):
                messagebox.showinfo("Game Over", f"{self.current_turn} wins!")
                self.reset_game()
            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_turn = 'O' if self.current_turn == 'X' else 'X'
                if self.current_turn == 'O':
                    self.computer_move()

    def check_winner(self, square):
        row = square // 3
        if self.board[row * 3] == self.board[row * 3 + 1] == self.board[row * 3 + 2] != ' ':
            return True

        # Check column
        col = square % 3
        if self.board[col] == self.board[col + 3] == self.board[col + 6] != ' ':
            return True

        # Check diagonals
        if square % 4 == 0 and self.board[0] == self.board[4] == self.board[8] != ' ':
            return True
        if square % 2 == 0 and square != 0 and self.board[2] == self.board[4] == self.board[6] != ' ':
            return True

        return False

    def reset_game(self):
            self.board = [' ' for _ in range(9)]
            for button in self.buttons:
                button.config(text='')
                self.current_turn = 'X'

    def computer_move(self):
        available_moves = [i for i, spot in enumerate(self.board) if spot == ' ']
        if available_moves:
            square = random.choice(available_moves)
            self.make_move(square)

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
