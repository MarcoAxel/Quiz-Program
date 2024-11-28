import user
import gui
import question_bank as qb
try:
    bank = qb.QuestionBank("quiz1")
    sys = user.System()
    gui.login_screen(sys)
    curr = sys.logged_in_user
    if isinstance(curr,user.Student):
        curr.start_quiz("quiz1")
    elif isinstance(curr, user.Instructor):
        gui.question_window(bank)
except:
    gui.error_window()