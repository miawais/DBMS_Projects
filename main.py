import tkinter as tk

# Function to handle login button click (replace with your logic)
def login_clicked():
    username = username_entry.get()
    password = password_entry.get()
    # Implement your login validation and processing here (e.g., connect to a database)
    print(f"Username: {username}, Password: {password}")  # Placeholder

# Function to toggle password visibility (optional)
def toggle_password_visibility():
    if password_entry.show == "":
        password_entry.config(show="*")  # Hide password
    else:
        password_entry.config(show="")  # Show password

# Create the main window
root = tk.Tk()
root.title("Login Page")

# **Background image (optional):**
# You can add a background image using `tkinter.PhotoImage` or other methods.

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

# Password label and entry (set show="" for visible password initially)
password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="")  # Adjust show attribute as needed
password_entry.pack()

# Login button
login_button = tk.Button(root, text="Login", command=login_clicked)
login_button.pack()

# Optional: Remember me checkbox
remember_me_var = tk.IntVar()  # Boolean variable for checkbox state
remember_me_checkbox = tk.Checkbutton(root, text="Remember Me", variable=remember_me_var)
remember_me_checkbox.pack()

# Optional: Forgot password link
forgot_password_link = tk.Button(root, text="Forgot Password")  # Add functionality if needed
forgot_password_link.pack()

# Optional: Show password toggle button (more descriptive variable name)

root.mainloop()
