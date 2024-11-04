
def load_bank_from_file():
    '''
    Loads questions from file into a dictonary and returns the dictonary 
    '''
    dict = {}
    file = open('/Users/senrabel/Documents/Classes/Python Programming/Final Project/Question bank/bank.txt','r')
    question_list = file.readlines()
    for i in question_list:
        question_raw = i.split(':')
        q = question_raw[0]
        ans = question_raw[1]
        a = ans.split(',')
        a.remove('\n')
        dict.update({f'{q}':a})
    file.close()
    return dict

def write_bank_to_file(dict):
    '''
    Takes the dictonary and writes it into the bank.txt file overwriting anything else in the file
    '''
    file = open('/Users/senrabel/Documents/Classes/Python Programming/Final Project/Question bank/bank.txt', 'w')
    for key, val in dict.items():
        s = ""
        for i in val:
            s += i + ","
        file.write(f'{key}:{s}\n')

def add_to_bank(dict):
    '''
    Adds new items into the dictonary that stores the question bank DOES NOT write 
    the bank to a file
    '''
    num = int(input("Enter number of questions to add to the bank:"))
    for i in range(num):
        q = input("Enter question:")
        a = []
        a.append(input("Enter answer:"))
        for j in range(3):
            a.append(input("Enter decoy answer:"))
        dict.update({f'{q}':a})
    return dict

def print_bank(dict):
    '''
    prints the key and values froma given dictonary 
    '''
    for key, val in dict.items():
        print(f'{key}:{val}')
        