import tkinter
import customtkinter

def transition():
    splash_screen.pack_forget()
    home_screen.pack()

def label(text, frame):
    z = customtkinter.CTkLabel(frame, text=text, font=primary)
    return z

def f_button(text, frame, command):
    z = customtkinter.CTkButton(frame, text=text, command=command)
    return z

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
splash = customtkinter.CTkLabel(splash_screen, text='Welcome', font=primary)
splash.pack(pady=10)

button = customtkinter.CTkButton(splash_screen, text='Get Started', font=secondary, command=transition)
button.pack(pady=10)

#-------Home Screen--------#
home_screen = customtkinter.CTkFrame(window)
home_label = customtkinter.CTkLabel(home_screen, text='Main Menu', font=primary)
home_label.pack()

study_button = customtkinter.CTkButton(home_screen, text="Study", font=primary)
study_button.pack(pady=10)

options_button = customtkinter.CTkButton(home_screen, text="Options", font=primary)
options_button.pack(pady=10)

help_button = customtkinter.CTkButton(home_screen, text="Help", font=primary)
help_button.pack(pady=10)

suit_button = customtkinter.CTkButton(home_screen, text="Quit", font=primary, command=quit)
suit_button.pack(pady=10)

window.mainloop()