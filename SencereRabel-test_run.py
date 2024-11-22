import user
import gui
try:
    sys = user.System()
    gui.login_screen(sys)
    curr = sys.logged_in_user
    curr.start_quiz("quiz1")
    print(curr.scores)
except:
    gui.error_window()




