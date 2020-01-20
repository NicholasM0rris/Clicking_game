import sys
import threading
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import vlc
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
import time


class ClickingGame(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.play_again = False
        self.play = True
        self.wins = 0
        self.wait_time = 5.0
        self.pushed = False
        self.start()

    def callback(self):
        sys.exit()

    def run(self):
        self.top = tk.Tk()
        self.is_green_button = False
        self.redbutton = ImageTk.PhotoImage(Image.open('support/redbutton.jpg').resize((500, 500), Image.ANTIALIAS))
        self.greenbutton = ImageTk.PhotoImage(Image.open('support/greenbutton.jpg').resize((500, 500), Image.ANTIALIAS))
        self.nuke = ImageTk.PhotoImage(Image.open('support/nuke.jpg').resize((500, 500), Image.ANTIALIAS))
        self.top.protocol("WM_DELETE_WINDOW", self.callback)
        self.top.title('Clicking Game')
        self.main_frame = tk.Frame(self.top)
        self.button = tk.Label(self.main_frame, image=self.redbutton)
        self.button.grid(row=2)
        self.text = tk.StringVar()
        self.label = tk.Label(self.main_frame, text=self.text)
        self.label.config(text="Press the green button when it appears!")
        self.label.config(font=("Arial", 18))
        self.button.bind("<Button-1>", self.button_press)
        self.label.grid(row=1)
        self.top.resizable(0, 0)
        self.main_frame.pack()
        mixer.init()
        mixer.music.load('support/badmusic.mp3')
        mixer.music.play()
        self.countdown_time = 1
        tk.mainloop()

    def button_press(self, event=None):
        self.pushed = True
        if self.is_green_button:
            game_win(self)
        else:
            game_loss(self)


def countdown(self):
    print('new_game')
    for count in reversed(range(1, 6)):
        self.label.config(text='Get Ready in {}!'.format(count))
        time.sleep(self.countdown_time)
    self.is_green_button = True
    self.start = time.time()
    self.label.config(text='Slam that button!'.format(count))
    self.button.configure(image=self.greenbutton)
    self.button.image = self.greenbutton
    time.sleep(self.wait_time)
    self.is_green_button = False
    if not self.pushed:
        self.label.config(text='We missed our chance! The world is doomed!')
        self.button.configure(image=self.redbutton)
        self.button.image = self.redbutton
        game_loss(self)


def game_loss(self):
    print('oops')
    self.button.configure(image=self.nuke)
    self.button.image = self.nuke
    self.label.config(text='YOU DIED!')

    p = vlc.MediaPlayer("support/boom.mp3")
    p.play()
    self.top.option_add('*Dialog.msg.font', 'Helvetica 40')
    messagebox.showinfo(message='YOU DIED')
    self.play = False
    sys.exit()


def game_win(self):
    timer = -self.start + time.time()
    if self.wins == 0:
        messagebox.showinfo(
            message='Your superior decision making and reflexes saved your house...! From totally obliteration anyway...')
        one_wins = Image.open('support/1win.jpg').resize((500, 500), Image.ANTIALIAS)
        one_wins.show()
    if self.wins == 2:
        messagebox.showinfo(
            message='You are praised as the saviour of the city! Wait a second, Why\'s it on fire...!!')
        three_wins = Image.open('support/3wins.jpg').resize((500, 500), Image.ANTIALIAS)
        three_wins.show()
    elif self.wins == 4:
        messagebox.showinfo(
            message='You saved your country from destruction! A hero for the ages!!')
        five_wins = Image.open('support/5wins.jpg').resize((500, 500), Image.ANTIALIAS)
        five_wins.show()
    elif self.wins == 7:
        messagebox.showinfo(
            message='You saved the world! Your people will never forget you!!')
        ten_wins = Image.open('support/10wins.jpg').resize((500, 500), Image.ANTIALIAS)
        ten_wins.show()
    elif self.wins == 9:
        messagebox.showinfo(
            message='You saved the universe! You have become a God!! There is nothing left for you to do now.')
        fifteen_wins = Image.open('support/15wins.jpg').resize((500, 500), Image.ANTIALIAS)
        fifteen_wins.show()
    print('Wow! What a champ!')
    self.wins += 1
    self.label.config(text='Incredible!!!! Get ready for the next round!')
    p = vlc.MediaPlayer("support/win.mp3")
    p.play()
    self.top.option_add('*Dialog.msg.font', 'Helvetica 40')
    messagebox.showinfo(message='WHAT A WINNER! You clicked the button in {} seconds! That is {} wins in a row!'.format(
        timer, self.wins))
    time.sleep(self.wait_time + 1)
    self.pushed = False
    new_round(self)


def new_round(self):
    self.wait_time = self.wait_time / 1.5
    self.label.config(text="Press the green button when it appears!")
    self.button.configure(image=self.redbutton)
    self.button.image = self.redbutton
    self.play_again = True


def main(arglist):
    game = ClickingGame()
    time.sleep(3)
    #print('test')
    try:
        countdown(game)
    except RuntimeError:
        sys.exit()

    while game.play:
        try:
            if game.play_again:
                countdown(game)
                game.play_again = False
        except RuntimeError:
            sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
