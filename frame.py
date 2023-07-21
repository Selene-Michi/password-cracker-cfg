#importing our pop up window from tkinter
import tkinter
from tkinter import messagebox #pop up box appears outside our window
#haslib import needed...




#DICTIONARY ATTACK CODE NEEDED FOR CODE TO WORK
#FOLLOWING CODE IS FOR THE GUI 












window = tkinter.Tk()
window.title("password cracker")
#popup window size in width and height
window.geometry('600x450')
#main frame bg color dark slate gray
window.configure(bg='#2F2F4F')

#inner frame color dark slate, placing all our widgets inside a frame for better UI exterience
frame = tkinter.Frame(bg='#2F2F4F') #frame is our tkinter container inside window for responsivness on larger screen size

# Creating widgets using grid (login created using pack above grid)
#Parent is window and text is username followed by another parent window and text password 
#x3 labels as static text on our password cracker screen 
#multiple attributes used to style our pop up window bg(background) fg(foreground)
login_label = tkinter.Label(frame, text="Check if a password can be cracked: ", bg='#52528B', fg="#FFFF14", font=("Arial", 19))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 18))
password_label = tkinter.Label(frame, text="Password", bg='#52528B', fg="#FFFF14", font=("Arial", 18))
#command used to execute when button is clicked
login_button = tkinter.Button( frame, text="Enter", bg='#FFFFEF', fg="#272740", font=("Arial", 18), command=compare_passwords)

# Placing widgets on the screen using grid which has 4 rows and 2 columns, starting at zero, 1, 2  & 3
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)#Pad(y) adding spaceing on y axis
password_label.grid(row=2, column=0,)
password_entry.grid(row=2, column=1, pady=20, padx=(100, 10))
login_button.grid(row=3, column=0, columnspan=2, pady=30) #spacing of login button on y axis

#using pack to make our pop up window responsive when you change the sizing to larger screen to look centralised
frame.pack()

#window.mainloop allows Tkinter to run and display our pop up window. Placed at the end of our password cracker code
window.mainloop()
