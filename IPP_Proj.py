import tkinter
import random
from playsound import playsound
from gtts import gTTS

window = tkinter.Tk()
window.geometry("488x250")
window.title("Brain Teaser")
window.resizable(0, 0)



def play(audio):  # function to play audio
    sound = gTTS(audio)
    sound.save('sound.mp3')
    playsound('sound.mp3')


def homeScreen():  # setting up home screen in gui
    Result.grid_forget(), Restart.grid_forget(), Quit.grid_forget(), Home.grid_forget()
    welcome.grid(row="0", columnspan="2")
    enterName.grid(row="1", column="0", pady="20")
    Name.grid(row="1", column="1")
    instruction.grid(row="2", padx="15", pady="10", columnspan="2")
    start.grid(row="3", columnspan="2")


class IPP:
    def __init__(self):
        self.name = ""  # storing user name
        self.anspos = 0  # answer index position
        self.score = 0  # Score Counter
        self.progress = 0  # progress counter
        self.operations = ["+", "-", "x"]

    def newQues(self):  # making new question and printing in gui
        a = random.randint(0, 100)  # Two random numbers for question
        b = random.randint(0, 100)
        operation = random.choice(self.operations)
        if operation == "+": ans = a + b  # answer
        elif operation == "-": ans = a-b
        elif operation == "x": ans = a*b
        for j in range(4):  # storing random numbers in options
            option[j].set(random.randint(-200, 200))
            while option[j] == ans:
                option[j].set(random.randint(-200, 200))
        self.anspos = random.randint(0, 3)  # getting random position for printing answer
        option[self.anspos].set(ans)  # storing ans to that position
        quest.set((a, operation, b, "?"))  # setting q in gui
        window.update()  # updating windows
        if operation == "+" : play(str((a, "+", b)))  # playing question
        elif operation == "-" : play(str((a, "minus", b)))
        elif operation == "x" : play(str((a, "multiplied by", b)))

    def isCorrect(self, n):  # checking whether option clicked is correct or not and updating info
        if n == self.anspos:
            self.score = self.score + 1  # increasing score if correct
            play("Correct Answer")
        else:
            play("Wrong answer")
        self.progress = self.progress + 1  # increasing progress
        p.update()
        if self.progress != 10:
            p.newQues()  # going for next question if 10 questions are not yet completed
        else:
            Prog.grid_forget(), Score.grid_forget(), Q.grid_forget()  # removing unwanted labels and button
            A.grid_forget(), B.grid_forget(), C.grid_forget(), D.grid_forget()
            Result.grid(row="0", columnspan="3", pady="6", padx="10")  # adding result label
            final.set(("Congratulations", self.name, "!,Your", "Score", "is", self.score, "/", "10"))
            Quit.grid(row="1", column="2", pady="10"), Restart.grid(row="1", column="0", pady="10")
            Home.grid(row="1", column="1", pady="10")  # setting Widgets in gui.
            window.update()
            play(str(("Congratulations", self.name, ", Your Score is", self.score, "out of 10.")))  # playing result
    def update(self):  # updating progress and score.
        scorestr.set(("Score", ":", self.score, "/", "10"))
        progstr.set(("Progress", ":", p.progress, "/", "10"))

    def start(self):  # setting up start widgets and removing unnecessary widgets
        self.name = Name.get("1.0", 'end-1c')
        if self.name == "":
            play("Please enter Your Name")
            return 0
        instruction.grid_forget(), start.grid_forget(), welcome.grid_forget()
        enterName.grid_forget(), Name.grid_forget()
        Prog.grid(column="0", row="0", pady="10"), Score.grid(column="1", row="0")
        Q.grid(row="1", columnspan="2", padx="4")  # making grid view in gui
        A.grid(column="0", row="2", pady="10"), B.grid(column="1", row="2")
        C.grid(column="0", row="3"), D.grid(column="1", row="3")
        Result.grid_forget(), Restart.grid_forget(), Quit.grid_forget(), Home.grid_forget()
        self.score = 0
        self.progress = 0
        p.update()  # updating score and prog in gui
        p.newQues()  # new question


p = IPP()  # creating instance of class IPP()
progstr = tkinter.StringVar()
scorestr = tkinter.StringVar()  # creating textvariables for tkinter widgets
quest = tkinter.StringVar()
final = tkinter.StringVar()
option = [0] * 4
(option[0]) = tkinter.IntVar()
(option[1]) = tkinter.IntVar()
(option[2]) = tkinter.IntVar()
(option[3]) = tkinter.IntVar()
welcome = tkinter.Label(window, width="22", text="Welcome to Brain Teaser!", font=("montserrat", 32), fg="white",
                        bg="dark slate grey")
enterName = tkinter.Label(window, width="14", text="Enter Your Name :", font=("montserrat", 25))
Name = tkinter.Text(window, width="8", height="1", font=("montserrat", 32))
instruction = tkinter.Button(window, width="24", text="INSTRUCTIONS", highlightbackground="peach puff",
                             font=("montserrat", 28), command=lambda: play("this is your instruction 1  this is your instruction 2"))
start = tkinter.Button(window, width="24", text="START", highlightbackground="peach puff", font=("montserrat", 28),
                       command=lambda: p.start())
Prog = tkinter.Label(window, width="15", textvariable=progstr, font=("montserrat", 22), fg="white", bg="purple3")
Score = tkinter.Label(window, width="15", textvariable=scorestr, font=("montserrat", 22), fg="white", bg="purple3")
Q = tkinter.Label(window, width="11", textvariable=quest, font=("montserrat", 64), fg="white", bg="dark slate grey")
A = tkinter.Button(window, width="12", textvariable=(option[0]), font=("montserrat", 28),
                   highlightbackground="peach puff",
                   command=lambda: p.isCorrect(0))
B = tkinter.Button(window, width="12", textvariable=(option[1]), font=("montserrat", 28),
                   highlightbackground="peach puff",
                   command=lambda: p.isCorrect(1))
C = tkinter.Button(window, width="12", textvariable=(option[2]), font=("montserrat", 28),
                   highlightbackground="peach puff",
                   command=lambda: p.isCorrect(2))
D = tkinter.Button(window, width="12", textvariable=(option[3]), font=("montserrat", 28),
                   highlightbackground="peach puff",
                   command=lambda: p.isCorrect(3))
Result = tkinter.Label(window, width="33", height="7", bg="ivory4", fg="white", textvariable=final,
                       font=("montserrat", 20))
Quit = tkinter.Button(window, width="8", text="Quit", command=lambda: quit(), font=("montserrat", 23))
Restart = tkinter.Button(window, width="8", text="Play Again", command=lambda: p.start(), font=("montserrat", 23))
Home = tkinter.Button(window, width="8", text="Home", command=lambda: homeScreen(), font=("montserrat", 23))
homeScreen()
window.mainloop()
