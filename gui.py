import tkinter as tk

def login_screen(sys):
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
            confirmation_window(root)
        else:
            pop_up_window(root, "400x300", "Oops", "Login Failed")

    login_button = tk.Button(root, text="Login", font=("Arial", 12), command=on_login)
    login_button.pack(pady=10)

    # Start the main event loop
    root.mainloop()

def confirmation_window(root):
    """
    Opens a window to confirm that the login was a success.
    """
    new_window = tk.Toplevel(root)
    new_window.title("Welcome")
    new_window.geometry("400x300")
    tk.Label(new_window, text="Login Successful!").pack(pady=10)
    tk.Button(new_window, text="OK", command=root.destroy).pack()

def pop_up_window(root, size, title, label_text):
    """
    Opens a new window with specified size,title and text label.
    """
    new_window = tk.Toplevel(root)
    new_window.title(title)
    new_window.geometry(size)
    tk.Label(new_window, text=label_text).pack(pady=10)
    tk.Button(new_window, text="OK", command=new_window.destroy).pack()

def error_window(label_text):
    root = tk.Tk()
    root.title("Error")
    root.geometry("200x100")  # Set the size of the window

    # Create a label and entry for the username
    textLabel = tk.Label(root, text=label_text, font=("Arial", 15))
    textLabel.pack()
    tk.Button(root, text="Exit", command=root.destroy).pack()
    root.mainloop()

def question_window(bank):
    from tkinter import messagebox

    def add_question():
        """
        Opens a dialog to add a new question and its answers to the question bank.
        """
        def save_question():
            question = question_entry.get()
            answers = [correct_entry.get(),wrong1_entry.get(),wrong2_entry.get(),wrong3_entry.get()]
            if not question or any(not ans for ans in answers):
                messagebox.showerror("Input Error", "All fields must be filled!")
                return
            bank.add_question(question,answers)
            clear_entries()
        def finish():
            root.destroy()
        def clear_entries():
            """Clear all input fields."""
            question_entry.delete(0, tk.END)
            correct_entry.delete(0, tk.END)
            wrong1_entry.delete(0, tk.END)
            wrong2_entry.delete(0, tk.END)
            wrong3_entry.delete(0, tk.END)


            
        # Create the GUI
        root = tk.Tk()
        root.title("Add Questions to quiz")

        # Labels and entry fields
        tk.Label(root, text="Question:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        question_entry = tk.Entry(root, width=50)
        question_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Correct Answer:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        correct_entry = tk.Entry(root, width=50)
        correct_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Wrong Answer 1:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        wrong1_entry = tk.Entry(root, width=50)
        wrong1_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Wrong Answer 2:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        wrong2_entry = tk.Entry(root, width=50)
        wrong2_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Wrong Answer 3:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        wrong3_entry = tk.Entry(root, width=50)
        wrong3_entry.grid(row=4, column=1, padx=10, pady=5)

        # Buttons
        save_button = tk.Button(root, text="Save Question", command=save_question)
        save_button.grid(row=5, column=0, padx=10, pady=10, sticky="e")

        finish_button = tk.Button(root, text="Finish", command=finish)
        finish_button.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        root.mainloop()

    def display_csv_contents():
        """
        Displays the contents of the CSV file in a Tkinter window.
        """
        bank.load_bank_from_csv()
        def refresh_text_area():
            """
            Refreshes the Text widget with the current state of the CSV data.
            """
            text_area.configure(state="normal")  # Allow editing temporarily
            text_area.delete("1.0", tk.END)  # Clear existing content
            counter = 0
            for question, answers in bank.dict.items():
                counter += 1
                ans_text = ", ".join(answers)
                text_area.insert(tk.END, f"{counter}) {question}: {ans_text}\n")
            text_area.configure(state="disabled")  # Make it read-only again
        def remove_question():
            """
            Deletes question based on the given index
            """
            try:
                index = int(index_entry.get())
            except:
                return
            counter = 0
            for question, answers in bank.dict.items():
                counter +=1
                if counter == index:
                    if bank.delete_question(question):
                        messagebox.showinfo("Success", f"Deleted question: {question}")
                        refresh_text_area()
                    else:
                        messagebox.showerror("Error", "Question not found in the bank.")
                    break

        # Create a new window
        display_window = tk.Toplevel(root)
        display_window.title("CSV Contents")
        
        # Add a Text widget with a scrollbar
        text_area = tk.Text(display_window, wrap="none", height=20, width=80)
        scrollbar = tk.Scrollbar(display_window, orient=tk.VERTICAL, command=text_area.yview)
        text_area.configure(yscrollcommand=scrollbar.set)

        # Pack the widgets
        text_area.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Populate the Text widget with CSV contents
        refresh_text_area()

        # Labels and entry fields
        tk.Label(display_window, text="Enter index of question you wish to remove:").grid(row=1, column=0, columnspan=2, pady=10)
        index_entry = tk.Entry(display_window, width=50)
        index_entry.grid(row=2, column=0, columnspan=2, pady=10)

        # 
        confirm_button = tk.Button(display_window, text="Confirm deletion", command=remove_question)
        confirm_button.grid(row=2, column=1, columnspan=2, pady=10)

        # Add an "Exit" button at the bottom
        exit_button = tk.Button(display_window, text="Exit", command=display_window.destroy)
        exit_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Configure resizing
        display_window.grid_rowconfigure(0, weight=1)
        display_window.grid_columnconfigure(0, weight=1)

       
    root = tk.Tk()
    root.title("Question Bank Manager")
    root.geometry("600x100")

    btn_add = tk.Button(root, text="Add Question", command=add_question)
    btn_add.pack(side=tk.LEFT, padx=10, pady=10)
    
    btn_load = tk.Button(root, text="View or Delete Questions", command=display_csv_contents)
    btn_load.pack(side=tk.LEFT, padx=10, pady=10)

    root.mainloop()

def quiz_select_window():
    """
    Create a Tkinter window to prompt the user for a string.
    Returns the string entered by the user.
    """
    user_input = None  # Variable to store the user's input

    def on_submit():
        nonlocal user_input
        user_input = input_entry.get()  # Retrieve the text from the entry widget
        root.destroy()  # Close the window

    # Create the main Tkinter window
    root = tk.Tk()
    root.title("File Select")
    root.geometry("300x150")

    # Create and place a label and an entry field
    tk.Label(root, text="Enter the name of a quiz:", font=("Arial", 12)).pack(pady=10)
    input_entry = tk.Entry(root, font=("Arial", 12))
    input_entry.pack(pady=5)

    # Create and place a submit button
    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()

    return user_input