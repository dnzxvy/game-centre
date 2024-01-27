from tkinter import *
import subprocess
import pygame

def start_snake_game_wrapper():
    pygame.mixer.music.stop()
    create_snake_mode_window()

def start_tic_tac_toe_game_wrapper():
    pygame.mixer.music.stop()
    create_tic_tac_toe_mode_window()

def start_pong_game_wrapper():
    pygame.mixer.music.stop()
    subprocess.Popen(["python", "pong_game.py"])

def start_easy_mode_snake():
    subprocess.Popen(["python", "easy_mode_snake.py"])

def start_hard_mode_snake():
    subprocess.Popen(["python", "hard_mode_snake.py"])

def create_snake_mode_window():
    snake_mode_window = Toplevel(root)
    snake_mode_window.title("Select Snake Game Difficulty")

    easy_button = Button(snake_mode_window, text="Easy Mode", command=start_easy_mode_snake, padx=10, pady=5, font=('Helvetica', 12, 'bold'))
    easy_button.config(height=2, width=15)
    easy_button.pack(pady=20)

    hard_button = Button(snake_mode_window, text="Hard Mode", command=start_hard_mode_snake, padx=10, pady=5,font=('Helvetica', 12, 'bold'))
    hard_button.config(height=2, width=15)
    hard_button.pack(pady=20)

def start_two_player_mode_tictactoe():
    subprocess.Popen(["python", "tic_tac_toe_game.py"])

def start_human_vs_AI_tictactoe():
    subprocess.Popen(["python", "tictactoe_humanvsAI.py"])

def create_tic_tac_toe_mode_window():
    tic_tac_toe_mode_window = Toplevel(root)
    tic_tac_toe_mode_window.title("Select TicTacToe Game mode")

    twoplayer_button = Button(tic_tac_toe_mode_window, text="Two Player Mode", command=start_two_player_mode_tictactoe,padx=10, pady=5, font=('Helvetica', 12, 'bold'))
    twoplayer_button.config(height=2, width=15)
    twoplayer_button.pack(pady=20)

    human_vs_AI_button = Button(tic_tac_toe_mode_window, text="Human vs Computer Mode", command=start_human_vs_AI_tictactoe,padx=10, pady=5, font=('Helvetica', 12, 'bold'))
    human_vs_AI_button.config(height=2, width=15)
    human_vs_AI_button.pack(pady=20)


root = Tk()
root.title("Daniel Game Centre")
root.geometry("600x400")
root.configure(bg="black")

pygame.mixer.init()
pygame.mixer.music.load("geometry_dash_type_beat.mp3")
pygame.mixer.music.play(-1)

title_label = Label(root, text="Daniel Game Centre", font=('Helvetica', 16, 'bold'), fg="white", bg="black")
title_label.pack(pady=10)

snake_button = Button(root, text="Snake Game", command=start_snake_game_wrapper, padx=10, pady=5, bg="purple", fg="white", relief=RAISED, borderwidth=3, font=('Helvetica', 12, 'bold'))
snake_button.config(height=2, width=13)
snake_button.pack(pady=20)

tic_tac_toe_button = Button(root, text="Tic-Tac-Toe Game", command=start_tic_tac_toe_game_wrapper, bg="blue", fg="white", font=('Helvetica', 12, 'bold'))
tic_tac_toe_button.config(height=2, width=20)
tic_tac_toe_button.pack(pady=20)

pong_game_button = Button(root, text="Pong Game", command=start_pong_game_wrapper, bg="green", fg="white", font=('Helvetica', 12, 'bold'))
pong_game_button.config(height=2, width=20)
pong_game_button.pack(pady=20)

root.mainloop()

