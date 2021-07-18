import tkinter as tk
from tkinter import messagebox

clicked = True
count = 0
winner = False


def game_winner():
    global winner, count
    if bt1['text'] == "O" and bt2['text'] == "O" and bt3['text'] == "O" and winner == False:
        bt1.config(bg='lightskyblue')
        bt2.config(bg='lightskyblue')
        bt3.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '2nd Player won.')
        winner = True
        reset_game()
    elif bt1['text'] == "X" and bt2['text'] == "X" and bt3['text'] == "X" and winner == False:
        bt1.config(bg='lightskyblue')
        bt2.config(bg='lightskyblue')
        bt3.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '1st Player won.')
        winner = True
        reset_game()
    elif bt4['text'] == 'O' and bt5['text'] == 'O' and bt6['text'] == 'O' and winner == False:
        bt4.config(bg='lightskyblue')
        bt5.config(bg='lightskyblue')
        bt6.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '2nd Player won.')
        winner = True
        reset_game()
    elif bt4['text'] == 'X' and bt5['text'] == 'X' and bt6['text'] == 'X' and winner == False:

        bt4.config(bg='lightskyblue')
        bt5.config(bg='lightskyblue')
        bt6.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '1st Player won.')
        winner = True
        reset_game()
    elif bt7['text'] == 'O' and bt8['text'] == 'O' and bt9['text'] == 'O' and winner == False:

        bt7.config(bg='lightskyblue')
        bt8.config(bg='lightskyblue')
        bt9.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '2nd Player won.')
        winner = True
        reset_game()
    elif bt7['text'] == 'X' and bt8['text'] == 'X' and bt9['text'] == 'X' and winner == False:
        bt7.config(bg='lightskyblue')
        bt8.config(bg='lightskyblue')
        bt9.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '1st Player won.')
        winner = True

        reset_game()

    elif bt1['text'] == "O" and bt4['text'] == "O" and bt7['text'] == "O" and winner == False:
        bt1.config(bg='lightskyblue')
        bt4.config(bg='lightskyblue')
        bt7.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '2nd Player won.')
        winner = True
        reset_game()
    elif bt1['text'] == "X" and bt4['text'] == "X" and bt7['text'] == "X" and winner == False:
        bt1.config(bg='lightskyblue')
        bt4.config(bg='lightskyblue')
        bt7.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '1st Player won.')
        winner = True
        reset_game()
    elif bt2['text'] == 'O' and bt5['text'] == 'O' and bt8['text'] == 'O' and winner == False:
        bt2.config(bg='lightskyblue')
        bt5.config(bg='lightskyblue')
        bt8.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '2nd Player won.')
        winner = True
        reset_game()
    elif bt2['text'] == 'X' and bt5['text'] == 'X' and bt8['text'] == 'X' and winner == False:
        bt2.config(bg='lightskyblue')
        bt5.config(bg='lightskyblue')
        bt8.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '1st Player won.')
        winner = True
        reset_game()
    elif bt3['text'] == 'O' and bt6['text'] == 'O' and bt9['text'] == 'O' and winner == False:
        bt3.config(bg='lightskyblue')
        bt6.config(bg='lightskyblue')
        bt9.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '2nd Player won.')
        winner = True
        reset_game()
    elif bt3['text'] == 'X' and bt6['text'] == 'X' and bt9['text'] == 'X' and winner == False:
        bt3.config(bg='lightskyblue')
        bt6.config(bg='lightskyblue')
        bt9.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '1st Player won.')
        winner = True
        reset_game()
    elif bt1['text'] == 'O' and bt5['text'] == 'O' and bt9['text'] == 'O' and winner == False:
        bt1.config(bg='lightskyblue')
        bt5.config(bg='lightskyblue')
        bt9.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '2nd Player won.')
        winner = True
        reset_game()
    elif bt1['text'] == 'X' and bt5['text'] == 'X' and bt9['text'] == 'X' and winner == False:
        bt1.config(bg='lightskyblue')
        bt5.config(bg='lightskyblue')
        bt9.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '1st Player won.')
        winner = True
        reset_game()
    elif bt3['text'] == 'O' and bt5['text'] == 'O' and bt7['text'] == 'O' and winner == False:
        bt3.config(bg='lightskyblue')
        bt5.config(bg='lightskyblue')
        bt7.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '2nd Player won.')
        winner = True
        reset_game()
    elif bt3['text'] == 'X' and bt5['text'] == 'X' and bt7['text'] == 'X' and winner == False:

        bt3.config(bg='lightskyblue')
        bt5.config(bg='lightskyblue')
        bt7.config(bg='lightskyblue')
        messagebox.showinfo('Tik Tac Toe', '1st Player won.')
        winner = True
        reset_game()

    elif winner == False and count == 9:
        messagebox.showinfo('Tik Tac Toe', "It's a draw")
        reset_game()


def play(button):
    global clicked, count
    if clicked == True and button["text"] == " ":
        button["text"] = "X"
        count += 1
        clicked = False
        game_winner()

    elif clicked == False and button["text"] == " ":
        button["text"] = "O"
        clicked = True
        count += 1
        game_winner()
    else:
        messagebox.showerror('Tik Tac Toe', 'This block has already been selected, please click on other block.')


def reset_game():
    global count, clicked, winner
    bt1['text'] = " "
    bt2['text'] = " "
    bt3['text'] = " "
    bt4['text'] = " "
    bt5['text'] = " "
    bt6['text'] = " "
    bt7['text'] = " "
    bt8['text'] = " "
    bt9['text'] = " "
    bt1['bg'] = 'SystemButtonFace'
    bt2['bg'] = 'SystemButtonFace'
    bt3['bg'] = 'SystemButtonFace'
    bt4['bg'] = 'SystemButtonFace'
    bt5['bg'] = 'SystemButtonFace'
    bt6['bg'] = 'SystemButtonFace'
    bt7['bg'] = 'SystemButtonFace'
    bt8['bg'] = 'SystemButtonFace'
    bt9['bg'] = 'SystemButtonFace'

    count = 0
    clicked = True
    winner = False


root = tk.Tk()

root.title('Tick tac toe')
# defaultbg = root.cget('bg')
# print(defaultbg)
bt1 = tk.Button(root, width=18, height=8, text=" ", bg="SystemButtonFace", command=lambda: play(bt1))
bt1.grid(row=0, column=0)
bt2 = tk.Button(root, width=18, height=8, text=" ", bg="SystemButtonFace", command=lambda: play(bt2))
bt2.grid(row=0, column=1)
bt3 = tk.Button(root, width=18, height=8, text=" ", bg="SystemButtonFace", command=lambda: play(bt3))
bt3.grid(row=0, column=2)
bt4 = tk.Button(root, width=18, height=8, text=" ", bg="SystemButtonFace", command=lambda: play(bt4))
bt4.grid(row=1, column=0)
bt5 = tk.Button(root, width=18, height=8, text=" ", bg="SystemButtonFace", command=lambda: play(bt5))
bt5.grid(row=1, column=1)
bt6 = tk.Button(root, width=18, height=8, text=" ", bg="SystemButtonFace", command=lambda: play(bt6))
bt6.grid(row=1, column=2)
bt7 = tk.Button(root, width=18, height=8, text=" ", bg="SystemButtonFace", command=lambda: play(bt7))
bt7.grid(row=2, column=0)
bt8 = tk.Button(root, width=18, height=8, text=" ", bg="SystemButtonFace", command=lambda: play(bt8))
bt8.grid(row=2, column=1)
bt9 = tk.Button(root, width=18, height=8, text=" ", bg="SystemButtonFace", command=lambda: play(bt9))
bt9.grid(row=2, column=2)
new_game = tk.Button(root, width=13, bg='light coral', font=('Courier', 12), text="Reset Game", command=reset_game)

new_game.grid(row=3, column=1)
root.mainloop()


