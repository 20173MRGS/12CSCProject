import tkinter
import customtkinter
from random import *


def transition(start, end):
    start.pack_forget()
    end.pack()

def p_label(text, frame):
    z = customtkinter.CTkLabel(frame, text=text, font=primary)
    return z
def s_label(text, frame):
    z = customtkinter.CTkLabel(frame, text=text, font=secondary)
    return z
def f_button(text, frame, command):
    z = customtkinter.CTkButton(frame, text=text, command=command)
    return z

def change_theme(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

def back_button(start, end):
    back = customtkinter.CTkButton(start, text='Back', font=secondary,
                                         command=lambda: transition(start, end))
    back.pack(padx=10, pady=10)

def differentiationquiz():

    correct_screen = customtkinter.CTkFrame(window)
    correct = customtkinter.CTkLabel(correct_screen, text="correct", font=primary)
    correct.pack()

    incorrect_screen = customtkinter.CTkFrame(window)
    incorrect = customtkinter.CTkLabel(incorrect_screen, text="incorrect", font=primary)
    incorrect.pack()

    right_answer = customtkinter.CTkLabel(incorrect_screen, text=(str(str(a * b) + "x^" + str(b - 1))), font=primary)
    right_answer.pack()

    a = randint(1, 10)
    b = randint(1, 10)
    question = ('f(x)= ' + str(a) + "x^" + str(b))
    print(question)
    answer = input('differentiate f(x)= ' + str(a) + "x^" + str(b) + ": ")
    if answer == str(str(a * b) + "x^" + str(b - 1)):
        print("Correct")
    else:
        print("Incorrect")
        print("dy/dx= " + str(a * b) + "x^" + str(b - 1))


#------Default Settings--------#
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

#------- Window---------#

window = customtkinter.CTk()
window.geometry('300x300')
window.title('12CSC Project')

#--------Fonts---------#
primary = customtkinter.CTkFont(family="SF Pro Display", size=18)
secondary = customtkinter.CTkFont(family='SF Pro Display', size=14)

#--------Splash Screen-------#
splash_screen = customtkinter.CTkFrame(window)
splash_screen.pack()

splash = customtkinter.CTkLabel(splash_screen, text='Hello There', font=primary)
splash.pack(side="left", padx=10)

button = customtkinter.CTkButton(splash_screen, text='Get Started', font=secondary, command=lambda: transition(splash_screen, home_screen))
button.pack(pady=10)

#-------Home Screen--------#
home_screen = customtkinter.CTkFrame(window)

home_label = customtkinter.CTkLabel(home_screen, text='Main Menu', font=primary)
home_label.pack(side='left', padx=10)

study_button = customtkinter.CTkButton(home_screen, text="Study", font=primary, command=lambda: transition(home_screen, study_screen))
study_button.pack(pady=10)

options_button = customtkinter.CTkButton(home_screen, text="Options", font=primary, command= lambda: transition(home_screen, options_screen))
options_button.pack(pady=10)

help_button = customtkinter.CTkButton(home_screen, text="Help", font=primary)
help_button.pack(pady=10)

Quit_button = customtkinter.CTkButton(home_screen, text="Quit", font=primary, command=quit)
Quit_button.pack(pady=10)

#-------Study Screen-------#
study_screen = customtkinter.CTkFrame(window)

study_label = p_label('Study', study_screen)
study_label.pack(side='left', padx=10)

levels_button = customtkinter.CTkButton(study_screen, text="Levels", font=secondary, command=lambda: transition(study_screen, level_screen))
levels_button.pack(padx=10, pady=10)

recent_button = customtkinter.CTkButton(study_screen, text="Recent", font=secondary)
recent_button.pack(padx=10, pady=10)

study_back = customtkinter.CTkButton(study_screen, text='Back', font=secondary, command=lambda: transition(study_screen, home_screen))
study_back.pack(padx=10, pady=10)

#--------Levels Screen--------#
level_screen = customtkinter.CTkFrame(window)

study_label_2 = p_label('Levels', level_screen)
study_label_2.pack(side='left', padx=10)

level_1 = customtkinter.CTkButton(level_screen, text='Level 1', command=lambda: transition(level_screen, level_1_screen))
level_1.pack(padx=10, pady=10)

level_2 = customtkinter.CTkButton(level_screen, text='Level 2', command=lambda: transition(level_screen, level_2_screen))
level_2.pack(padx=10, pady=10)

level_3 = customtkinter.CTkButton(level_screen, text='Level 3')
level_3.pack(padx=10, pady=10)

back_button(level_screen, study_screen)

#------------------------Level 1 --------------------------------#
level_1_screen = customtkinter.CTkFrame(window)

study1_label = p_label('Level 1', level_1_screen)
study1_label.pack(side='left', padx=10)

standard_1 = customtkinter.CTkButton(level_1_screen, text='TEG')
standard_1.pack(padx=10, pady=10)

standard_2 = customtkinter.CTkButton(level_1_screen, text='MCAT', command=lambda: transition(level_1_screen, mcat_screen))
standard_2.pack(padx=10, pady=10)

standard_3 = customtkinter.CTkButton(level_1_screen, text='stats')
standard_3.pack(padx=10, pady=10)

back_button(level_1_screen, level_screen)

#--------MCAT-------#
mcat_screen = customtkinter.CTkFrame(window)

mcat_label = p_label('MCAT', mcat_screen)
mcat_label.pack(side='left', padx=10)

achieved = customtkinter.CTkButton(mcat_screen, text='Achieved')
achieved.pack(padx=10, pady=10)

merit = customtkinter.CTkButton(mcat_screen, text='Merit')
merit.pack(padx=10, pady=10)

excellence = customtkinter.CTkButton(mcat_screen, text='Excellence')
excellence.pack(padx=10, pady=10)

mcat_skills = customtkinter.CTkButton(mcat_screen, text='Skills')
mcat_skills.pack(padx=10, pady=10)

back_button(mcat_screen, level_1_screen)


#-----------------------Level 2-------------------------#

level_2_screen = customtkinter.CTkFrame(window)

study2_label = p_label('Level 2', level_2_screen)
study2_label.pack(side='left', padx=10)

standard_1 = customtkinter.CTkButton(level_2_screen, text='Algebra')
standard_1.pack(padx=10, pady=10)

standard_2 = customtkinter.CTkButton(level_2_screen, text='Calculus', command=lambda: transition(level_2_screen, level_2_calculus))
standard_2.pack(padx=10, pady=10)

back_button(level_2_screen, level_screen)

#--------------Calculus--------------#
level_2_calculus = customtkinter.CTkFrame(window)

skills = customtkinter.CTkButton(level_2_calculus, text='Skills', command=lambda: transition(level_2_calculus, lvl_2_calculus_skills ))
skills.pack(padx=10, pady=10)

lvl_2_calculus_skills = customtkinter.CTkFrame(window)
differentiaiton = customtkinter.CTkButton(lvl_2_calculus_skills, text='Differentiation', command=lambda: transition(lvl_2_calculus_skills, diffquiz))
differentiaiton.pack(padx=10, pady=10)
#-------------Differentiation Quiz --------------#
diffquiz = customtkinter.CTkFrame(window)

a = randint(1,10)
b = randint(1,10)
question = ('f(x)= ' + str(a) +"x^" + str(b))
correct_answer = ("dy/dx= " + str(a*b) + "x^" + str(b-1))
quizzer = customtkinter.CTkLabel(diffquiz, text=question, font=primary)
quizzer.pack(side='left', padx=10)
answer = customtkinter.CTkEntry(diffquiz)
answer.pack(padx=10, pady=10)
user_answer = answer.get()
if user_answer == str(str(a*b) + "x^" + str(b-1)):
    lambda: transition(diffquiz, correct_screen)
else:
    lambda: transition(diffquiz, incorrect_screen)

back_button(diffquiz, level_2_calculus)
#-----Correct Screen--------#
correct_screen = customtkinter.CTkFrame(window)
correct = customtkinter.CTkLabel(correct_screen, text="correct", font=primary)
correct.pack()

#--------Incorrect Screen-----#
incorrect_screen = customtkinter.CTkFrame(window)
incorrect = customtkinter.CTkLabel(incorrect_screen, text="incorrect", font=primary)
incorrect.pack()

right_answer = customtkinter.CTkLabel(incorrect_screen, text=(str(str(a*b) + "x^" + str(b-1))), font=primary)
right_answer.pack()



#-------------------level 3 ----------------------------#





#-----Options Screen-------#
options_screen = customtkinter.CTkFrame(window)

options_label = p_label('Options', options_screen)
options_label.pack(side='left', padx=10, pady=10)

theme_label = s_label('Theme', options_screen)
theme_label.pack()

theme_options = customtkinter.CTkSegmentedButton(options_screen, values=["Light", "Dark","System"], command=change_theme)
theme_options.pack(pady=10, padx=10)

back_button(options_screen, home_screen)

window.mainloop()