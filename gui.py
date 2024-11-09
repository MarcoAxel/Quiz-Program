import tkinter as tk
import user 


def login_screen():
    #intitilzies the system for login
    sys = user.System()

    # Create the main window
    root = tk.Tk()
    root.title("Login")
    root.geometry("600x500")  # Set the size of the window

    # Create a label and entry for the username
    username_label = tk.Label(root, text="Username", font=("Arial", 15))
    username_label.pack(pady=5)
    username_entry = tk.Entry(root, font=("Arial", 12))
    username_entry.pack(pady=5)

    # Create a label and entry for the password
    password_label = tk.Label(root, text="Password", font=("Arial", 15))
    password_label.pack(pady=5)
    password_entry = tk.Entry(root, font=("Arial", 12))
    password_entry.pack(pady=5)


    # Create a login button
    def on_login():
        username = username_entry.get()
        password = password_entry.get()
        if sys.login(username, password) == True:
            pop_up_window(root, "400x300", "Welcome", "Login Successful!")
        else:
            pop_up_window(root, "400x300", "Oops", "Login Failed")

    login_button = tk.Button(root, text="Login", font=("Arial", 12), command=on_login)
    login_button.pack(pady=10)

    # Start the main event loop
    root.mainloop()

def pop_up_window(root, size, title, label_text):
    """
    Opens a new window with specified size,title and text label.
    """
    new_window = tk.Toplevel(root)
    new_window.title(title)
    new_window.geometry(size)
    tk.Label(new_window, text=label_text).pack(pady=10)
    tk.Button(new_window, text="OK", command=new_window.destroy).pack()
