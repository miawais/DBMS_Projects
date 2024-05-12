from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("1280x720+0+0")
window.resizable(True, True)

background_image = Image.open('bd.jpg')
background_photo = ImageTk.PhotoImage(background_image)
bg_label = Label(window, image=background_photo)
bg_label.place(x=0, y=0)

login_frame = Frame(window,bg='black')
login_frame.place(x=600, y=180)

logo_image = Image.open('user.png')
# Resize the image to fit within the login frame
new_width = 100  # Adjust the width as needed
new_height = 100  # Adjust the height as needed
logo_image = logo_image.resize((new_width, new_height))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = Label(login_frame, image=logo_photo)
logo_label.grid(row=0, column=0,columnspan=4)

profileImage=PhotoImage(file='profile.png')
profileLabel=Label(login_frame,image=profileImage,
                   text='USERNAME',compound=LEFT,
                   font=('times new roman',15,'bold'))

profileLabel.grid(row=1,column=1)

usernameEntry=Entry(login_frame)
usernameEntry.grid(row=1,column=3)



window.mainloop()
