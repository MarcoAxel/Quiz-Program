import user
import question_bank as qb
import gui
sys = user.System()
bank = qb.QuestionBank()
gui.login_screen(sys,bank)
bank.load_bank_from_file()
bank.print_bank()


