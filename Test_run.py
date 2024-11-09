import user
from gui import login_screen

# Initialize the System instance
system = user.System()

# Launch the login GUI
login_screen(system)

# After closing the GUI, check the logged-in user
if system.logged_in_user:
    print(f"Logged in as: {system.logged_in_user.userID}")
else:
    print("No user logged in.")