import user
import gui
try:
    sys = user.System()
    gui.login_screen(sys)
    curr = sys.logged_in_user
    if isinstance(curr,user.Student):
        curr.start_quiz("quiz1")
        print(curr.scores)
    elif isinstance(curr, user.Instructor):
        print("Instuctor")
except:
    gui.error_window()