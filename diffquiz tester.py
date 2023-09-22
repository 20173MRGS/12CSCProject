import tkinter
import customtkinter
from random import *

global score
score = 0
a = 1
b = 1
quizzer = None

def transition(start, end):
    print('<transitioning>')
    start.pack_forget()
    end.pack()

def change_theme(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

def diffquizzer(): # This is the function that takes in input for differentiation quiz and checks if it is correct#
    global score
    user_answer = diff_answer.get()
    print("<submit button pressed>")
    print(user_answer)
    print(str(a * b) + "x^" + str(b - 1))
    if user_answer == (str(a * b) + "x^" + str(b - 1)):
        print("<correct>")
        score+=1
        print(score)
        transition(diffquiz, correct_screen)
    else:
        print("<incorrect>")
        diff_correct_answer.configure(text=("dy/dx= " + str(a*b) + "x^" + str(b-1)))
        diff_score_tally.configure(text=("You managed to get " + str(score) + " without losing"))
        transition(diffquiz, incorrect_screen)
        score = 0
def intquizzer(): # Function that takes input and checks whether it is correct or not for integration quiz #
    global score
    user_answer = answer.get()
    print("<submit button pressed>")
    print(user_answer)
    print(str(str(a) + "x^" + str(b)))
    if user_answer == str(str(a) + "x^" + str(b)):
        print("<correct>")
        score+=1
        print(score)
        transition(intquiz, correct_int_screen)
    else:
        print("<incorrect>")
        diff_correct_answer.configure(text=("f(x)= " + str(a) + "x^" + str(b)))
        score_tally.configure(text=("You managed to get " + str(score) + " without losing"))
        transition(intquiz, incorrect_int_screen)
        score = 0
def diffquizgen(c): # Generates the questions for the integration and differentiation quiz #
    print("<generating question>")
    global a, b, question, quizzer
    a = randint(1, 10)
    b = randint(1, 10)
    print(a)
    print(b)

    if c == 1:
        question = str('Differentiate f(x)= ' + str(a) + "x^" + str(b))
    elif c == 2:
        question = str('Integrate dy/dx = ' + str(a * b) + "x^" + str(b - 1))
    print(question)

    if quizzer == None:
        print("Quizzer is null")
        pass
    else:
        print("text configured")
        diff_quizzer.configure(text=question)
        quizzer.configure(text=question)

diffquizgen(1)

#------Default Settings--------#
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

#-------Window---------#
window = customtkinter.CTk()
window.geometry('300x300')
window.title('12CSC Project')

#-------Home Screen--------#
home_screen = customtkinter.CTkFrame(window)
home_screen.pack()

home_label = customtkinter.CTkLabel(home_screen, text='Main Menu')
home_label.pack(side='left', padx=10)

study_button = customtkinter.CTkButton(home_screen, text="Study", command=lambda: transition(home_screen, study_screen))
study_button.pack(pady=10)

options_button = customtkinter.CTkButton(home_screen, text="Options", command=lambda: transition(home_screen, options_screen))
options_button.pack(pady=10)

quit_button = customtkinter.CTkButton(home_screen, text="Quit", command=quit)
quit_button.pack(pady=10)


#------Study screen-----#
study_screen = customtkinter.CTkFrame(window)

study_label = customtkinter.CTkLabel(study_screen, text="Study")
study_label.pack(side='left', padx=10)

differentiation = customtkinter.CTkButton(study_screen, text="Differentiation", command=lambda: transition(study_screen, pre_diffquiz))
differentiation.pack(padx=10, pady=10)

integration = customtkinter.CTkButton(study_screen, text="Integration", command=lambda: transition(study_screen, pre_intquiz))
integration.pack(padx=10, pady=10)

back = customtkinter.CTkButton(study_screen, text="Back", command=lambda: transition(study_screen, home_screen))
back.pack(padx=10, pady=10)

#------Pre Diffquiz------#
pre_diffquiz = customtkinter.CTkFrame(window)

label = customtkinter.CTkLabel(pre_diffquiz, wraplength=200, text="This is a simple quiz to test your basic differentiation skills. Please write your answer the in form ax^b")
label.pack(padx=10, pady=10)

quiz = customtkinter.CTkButton(pre_diffquiz, text="Continue", command=lambda: [transition(pre_diffquiz, diffquiz), diffquizgen(1)])
quiz.pack(padx=10, pady=10)

back = customtkinter.CTkButton(pre_diffquiz, text="Back", command=lambda: transition(pre_diffquiz, study_screen))
back.pack(padx=10, pady=10)

#---differentiation quiz----#

diffquiz = customtkinter.CTkFrame(window)


diff_quizzer = customtkinter.CTkLabel(diffquiz, text=question)
diff_quizzer.pack(side='left', padx=10)

diff_answer = customtkinter.CTkEntry(diffquiz)
diff_answer.pack(padx=10, pady=10)

submit = customtkinter.CTkButton(diffquiz, text="submit", command=diffquizzer)
submit.pack()


#------Correct Screen-----#

correct_screen = customtkinter.CTkFrame(window)
correct = customtkinter.CTkLabel(correct_screen, text="correct")
correct.pack()

try_again = customtkinter.CTkButton(correct_screen, text="Next", command=lambda: [transition(correct_screen, diffquiz), diffquizgen(1)])
try_again.pack(pady=10)

back_button = customtkinter.CTkButton(correct_screen, text='Back', command=lambda: transition(correct_screen, study_screen))
back_button.pack(pady=10)

#------Incorrect Screen-----#

incorrect_screen = customtkinter.CTkFrame(window)

incorrect = customtkinter.CTkLabel(incorrect_screen, text="incorrect")
incorrect.pack()

diff_correct_answer = customtkinter.CTkLabel(incorrect_screen, text=("dy/dx= " + str(a*b) + "x^" + str(b-1)))
diff_correct_answer.pack(pady=10)

diff_score_tally = customtkinter.CTkLabel(incorrect_screen, text=("You managed to get " + str(score) + " without losing"))
diff_score_tally.pack(pady=10)

back_button = customtkinter.CTkButton(incorrect_screen, text='Back', command=lambda: transition(incorrect_screen, study_screen))
back_button.pack(pady=10)

#------Pre integration quiz------#
pre_intquiz = customtkinter.CTkFrame(window)

label = customtkinter.CTkLabel(pre_intquiz, wraplength=200 ,text="This is a simple quiz to test your basic integration skills. Please write your answer the in form ax^b, you do not need to include +c for this, but don't forget to include it in your exam!")
label.pack(padx=10, pady=10)

quiz = customtkinter.CTkButton(pre_intquiz, text="Continue", command=lambda: [transition(pre_intquiz, intquiz), diffquizgen(2)])
quiz.pack(padx=10, pady=10)

back = customtkinter.CTkButton(pre_intquiz, text="Back", command=lambda: transition(pre_intquiz, study_screen))
back.pack(padx=10, pady=10)

#-----Integration Quiz------#

intquiz = customtkinter.CTkFrame(window)

quizzer = customtkinter.CTkLabel(intquiz, text=question)
quizzer.pack(side='left', padx=10)

answer = customtkinter.CTkEntry(intquiz)
answer.pack(padx=10, pady=10)

submit = customtkinter.CTkButton(intquiz, text="submit", command=intquizzer)
submit.pack()

#----Correct integration screen-----#
correct_int_screen = customtkinter.CTkFrame(window)

correct = customtkinter.CTkLabel(correct_int_screen, text="correct")
correct.pack()

try_again = customtkinter.CTkButton(correct_int_screen, text="Next", command=lambda: [diffquizgen(2), transition(correct_int_screen, intquiz)])
try_again.pack(pady=10)

back_button = customtkinter.CTkButton(correct_int_screen, text='Quit', command=lambda: transition(correct_int_screen, study_screen))
back_button.pack(pady=10)

#-------Incorrect integration screen------#

incorrect_int_screen = customtkinter.CTkFrame(window)

incorrect = customtkinter.CTkLabel(incorrect_int_screen, text="incorrect")
incorrect.pack()

correct_answer = customtkinter.CTkLabel(incorrect_int_screen, text=("f(x)= " + str(a) + "x^" + str(b)))
correct_answer.pack(pady=10)

score_tally = customtkinter.CTkLabel(incorrect_int_screen, text=("You managed to get " + str(score) + " without losing"))
score_tally.pack(pady=10)

try_again = customtkinter.CTkButton(incorrect_int_screen, text="try again", command=lambda: [transition(incorrect_int_screen, diffquiz), diffquizgen(2)])

back_button = customtkinter.CTkButton(incorrect_int_screen, text='Back', command=lambda: transition(incorrect_int_screen, study_screen))
back_button.pack(pady=10)


#-----Options Screen-------#
options_screen = customtkinter.CTkFrame(window)

options_label = customtkinter.CTkLabel(options_screen, text='Options')
options_label.pack(side='left', padx=10, pady=10)

theme_label = customtkinter.CTkLabel(options_screen, text="theme")
theme_label.pack()

theme_options = customtkinter.CTkSegmentedButton(options_screen, values=["Light", "Dark","System"], command=change_theme)
theme_options.pack(pady=10, padx=10)

back = customtkinter.CTkButton(options_screen, text="Back", command=lambda: transition(options_screen, home_screen))
back.pack()

window.mainloop()