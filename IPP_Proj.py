import tkinter
import random

window = tkinter.Tk()
window.geometry("488x250")
window.title("Brain Teaser")
window.resizable(0, 0)


class IPP:
    def __init__(self):
        self.anspos = 0  # answer index position
        self.score = 0  # Score Counter
        self.progress = 0  # progress counter

    def newQues(self):  # making new question and printing in gui
        a = random.randint(0, 100)  # Two random numbers for question
        b = random.randint(0, 100)
        ans = a + b  # answer
        for j in range(4):  # storing random numbers in options
            option[j].set(random.randint(0, 200))
            while option[j] == ans:
                option[j].set(random.randint(0, 200))
        self.anspos = random.randint(0, 3)  # getting random position for printing answer
        option[self.anspos].set(ans)  # storing ans to that position
        quest.set((a, "+", b, "?"))  # setting q in gui
        self.progress = self.progress + 1  # increasing progress

    def isCorrect(self, n):  # checking whether option clicked is correct or not and updating info
        if n == self.anspos:
            self.score = self.score + 1  # increasing score if correct
        p.update()
        if self.progress != 10:
            p.newQues()  # going for next question if 10 questions are not yet completed
        else:
            Prog.grid_forget(), Score.grid_forget(), Q.grid_forget()  # removing unwanted labels and button
            A.grid_forget(), B.grid_forget(), C.grid_forget(), D.grid_forget()
            Result.grid(row="0", columnspan="2", pady="6", padx="10")  # adding result label
            final.set(("Congratulations!!,", "Your", "Score", "is", self.score, "/", "10"))  # setting result in gui.
            Quit.grid(row="1", column="1", padx="6", pady="10"), Restart.grid(row="1", column="0", padx="6", pady="10")

    def update(self):
        scorestr.set(("Score", ":", self.score, "/", "10"))
        progstr.set(("Progress", ":", p.progress, "/", "10"))

    def start(self):
        Prog.grid(column="0", row="0", pady="10"), Score.grid(column="1", row="0")
        Q.grid(row="1", columnspan="2", padx="4")  # making grid view in gui
        A.grid(column="0", row="2", pady="10"), B.grid(column="1", row="2")
        C.grid(column="0", row="3"), D.grid(column="1", row="3")
        Result.grid_forget(), Restart.grid_forget(), Quit.grid_forget()
        self.score = 0
        self.progress = 0
        p.update()
        p.newQues()


p = IPP()
progstr = tkinter.StringVar()
scorestr = tkinter.StringVar()
quest = tkinter.StringVar()
final = tkinter.StringVar()
option = [0] * 4
(option[0]) = tkinter.IntVar()
(option[1]) = tkinter.IntVar()
(option[2]) = tkinter.IntVar()
(option[3]) = tkinter.IntVar()
Prog = tkinter.Label(window, width="15", textvariable=progstr, font=("montserrat", 22), fg="white", bg="purple3")
Score = tkinter.Label(window, width="15", textvariable=scorestr, font=("montserrat", 22), fg="white", bg="purple3")
Q = tkinter.Label(window, width="11", textvariable=quest, font=("montserrat", 64), fg="white", bg="dark slate grey")
A = tkinter.Button(window, width="12", textvariable=(option[0]), font=("montserrat", 28), highlightbackground="peach puff",
                   command=lambda: p.isCorrect(0))
B = tkinter.Button(window, width="12", textvariable=(option[1]), font=("montserrat", 28), highlightbackground="peach puff",
                   command=lambda: p.isCorrect(1))
C = tkinter.Button(window, width="12", textvariable=(option[2]), font=("montserrat", 28), highlightbackground="peach puff",
                   command=lambda: p.isCorrect(2))
D = tkinter.Button(window, width="12", textvariable=(option[3]), font=("montserrat", 28), highlightbackground="peach puff",
                   command=lambda: p.isCorrect(3))
Result = tkinter.Label(window, width="29", height="6", bg="ivory4", fg="white", textvariable=final, font=("montserrat", 23))
Quit = tkinter.Button(window, width="13", text="Quit", command=lambda: quit(), font=("montserrat", 23))
Restart = tkinter.Button(window, width="13", text="Play Again", command=lambda: p.start(), font=("montserrat", 23))
p.start()
window.mainloop()
