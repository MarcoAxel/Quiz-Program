import user
import gui
import question_bank as qb
try:
    sys = user.System()
    quiz_name = "quiz1"
    #quiz_name = gui.quiz_select_window()
    gui.login_screen(sys)
    bank = qb.QuestionBank(quiz_name)
    curr = sys.logged_in_user
    if isinstance(curr,user.Student):
        try:
            curr.start_quiz(quiz_name)
        except:
            gui.error_window("Invalid quiz_name")
    elif isinstance(curr, user.Instructor):
        gui.question_window(bank)
except:
    gui.error_window("An error has occured")