from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
def right_clicked():
    pass
class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        #window
        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(padx=20, pady=20,bg = THEME_COLOR)

        # score
        self.score_label = Label(text="Score: 0 ", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        #canvas
        self.canvas = Canvas(width = 300, height = 250)
        self.question_text = self.canvas.create_text(150,125,
                                                     width = 280,
            text = "some question text",
            fill = THEME_COLOR,
            font = ("Arial",20, "italic"))
        self.canvas.grid(row = 1,column = 0,columnspan = 2)

        #buttons
        self.right_image = PhotoImage(file = "images/true.png")
        self.truebutton = Button(image = self.right_image,command = self.true_pressed,highlightthickness=0)
        self.truebutton.grid(row = 2, column = 0)


        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, command = self.false_pressed,highlightthickness=0)
        self.false_button.grid(row = 2,column = 1 )


        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text = f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text , text = q_text)
        else:
            self.canvas.itemconfig(self.question_text,text = "you have reched the end")
            self.truebutton.config(state = "disabled")
            self.false_button.config(state = "disabled")

    def true_pressed(self):

        is_right = self.quiz.check_answer("True")
        self.give_feed_back(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feed_back(is_right)


    def give_feed_back(self,is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "yellow")

        self.window.after(1000,self.get_next_question)