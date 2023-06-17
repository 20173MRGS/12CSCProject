import tkinter
import customtkinter




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
splash = customtkinter.CTkLabel(window, text='Welcome', font=primary)
splash.pack(pady=10)

button = customtkinter.CTkButton(window, text='Get Started', font=secondary)
button.pack(pady=10)

#-------Home Screen--------#
home_screen = customtkinter.CTkFrame(window)



window.mainloop()