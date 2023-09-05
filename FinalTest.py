correct_options = ["A", "B", "C", "D"]
gk_questions = {}
gk_answers = []
science_questions = {}
science_answers = []


# ------------------------------------------------------
def quiz(questions, choices):
    correct_answers = 0
    question_num = 1
    for key in questions:
        print("*" * 50)
        print(key)
        for choice in choices[question_num - 1]:
            print("\t" + choice)
        while True:
            guess = input("Enter your option as A, B, C or D:\n")
            guess = guess.upper()
            if guess in correct_options:
                break
            else:
                print("Please enter correct option and", end=" ")   

        correct_answers += score_count(questions[key], guess)
        #print("score:", correct_answers)
        question_num += 1
    print("Your Score is", correct_answers)


# ------------------------------------------------------
def score_count(answer, guess):
    if answer == str(guess):
        return 1
    else:
        return 0


# ------------------------------------------------------
def choose_quiz_topic():
    print("*" * 50)
    print("Choose your topic for quiz:\n\tA. General Knowledge\n\tB. Science")
    while True:
        topic = input("Enter your option as A or B:\n")
        topic = topic.upper()
        if topic == "A":
            load_gkquestions()
            quiz(gk_questions, gk_answers)
            break
        elif topic == "B":
            load_sciencequestions()
            quiz(science_questions, science_answers)
            break
        else:
            print("Please enter correct option and", end=" ")


# ------------------------------------------------------
def start_app():
    print('Assalam o Alaikum & Welcome to our quiz app!')

    print("What you would like to do?\n\tA. Take a quiz\n\tB. Manage questions")
    while True:
        to_do = input("Enter your choice as A or B:\n")
        to_do = to_do.upper()
        if to_do == "A":
            choose_quiz_topic()
            break
        elif to_do == "B":
            manage_app()
            break
        else:
            print("Please enter correct option and", end=" ")


# -----------------------------------------------------
def manage_app():
    while True:
        password = input("Enter Admin Password:\n")
        if password == "Admin":
            print("You have successfully signed in as ADMIN")
            choose_managing_topic()
            break
        else:
            print("WRONG! Again", end=" ")


# -----------------------------------------------------
def choose_managing_topic():
    print("\nchoose subject you want to manage:\n\tA. General Knowledge\n\tB. Science\n\tC. Logout")
    while True:
        managing_topic = input("Enter your option as A or B or C:")
        managing_topic = managing_topic.upper()
        if managing_topic == "A":
            load_gkquestions()
            operation(gk_questions, gk_answers)
            choose_managing_topic()
            break
        elif managing_topic == "B":
            load_sciencequestions()
            operation(science_questions, science_answers)
            choose_managing_topic()
            break
        elif managing_topic == "C":
            start_app()
            break
        else:
            print("Please enter correct option and", end=" ")
        # ------------------------------------------------------


def operation(questions_dictionary, choices_list):
    print("What you want to do?\n\tA. View Questions\n\tB. Add Questions\n\tC. Back")
    while True:
        operation = input("Enter your choice as A or B")
        operation = operation.upper()
        if operation == "A":
            view_questions(questions_dictionary)
            break
        elif operation == "B":
            add_question(questions_dictionary, choices_list)
            break
        elif operation == "C":
            choose_managing_topic()
        else:
            print("Please enter correct option and", end=" ")


# -----------------------------------------------------
def add_question(questions_dictionary, choices_list):

    multiple_choices = []
    new_question = input("Enter question now\n")
    print("Enter your multiple choices:\nPlease enter your options like \'A. xyz\'")
    for options in range(1, 5):
        new_options = input("Enter option " + str(options) + "\n")   
        
        multiple_choices.append(new_options) 
    new_answer = input("Enter correct option\n")
    
    if(questions_dictionary == gk_questions):
        file2 = open('gkQuestions.txt', 'a+') #APPEND & READ
        file2.write(str(new_question)+'\n')
        file2.write(str(multiple_choices[0])+'\n')
        file2.write(str(multiple_choices[1])+'\n')
        file2.write(str(multiple_choices[2])+'\n')
        file2.write(str(multiple_choices[3])+'\n')
        file2.write(str(new_answer)+'\n')
        file2.seek(0)
        print("Question Added Successfully!")
        
    elif(questions_dictionary == science_questions):
        file2 = open('scienceQuestions.txt', 'a+')
        file2.write(str(new_question)+'\n')
        file2.write(str(multiple_choices[0])+'\n')
        file2.write(str(multiple_choices[1])+'\n')
        file2.write(str(multiple_choices[2])+'\n') 
        file2.write(str(multiple_choices[3])+'\n')
        file2.write(str(new_answer)+'\n')
        file2.seek(0)
        print("Question Added Successfully!")
        
    else:
        print("Unable to update files!")


# ------------------------------------------------------
def view_questions(questions_dictionary):
    questions_list = questions_dictionary.keys()
    for questions in questions_list:
        print("\n" + questions, "-->", questions_dictionary[questions])



# -----------------------------------------------------

def load_gkquestions():

    file = open("gkQuestions.txt","r")
    x = len(file.readlines())

    file1 = open("gkQuestions.txt", "r")
    counter=0
    while(counter != x):

        calc = int(counter)%6
        if(calc == 0):
            
            temporary_list = []
            data = file1.readline()
            optionA = file1.readline()
            optionB = file1.readline()
            optionC = file1.readline()
            optionD = file1.readline()
            answer = file1.readline()
            gk_questions[data[:-1]]= answer[:-1]
            temporary_list.extend(["A. " + str(optionA[:-1]),"B. " + str(optionB[:-1]),"C. " + str(optionC[:-1]),"D. " + str(optionD[:-1])])
            gk_answers.append(temporary_list)
            counter += 6

# -----------------------------------------------------

def load_sciencequestions():

    file = open("scienceQuestions.txt","r")
    x = len(file.readlines())

    file1 = open("scienceQuestions.txt", "r")
    counter=0
    while(counter != x):

        calc = int(counter)%6
        if(calc == 0):
            
            temporary_list = []
            data = file1.readline()
            optionA = file1.readline()
            optionB = file1.readline()
            optionC = file1.readline()
            optionD = file1.readline()
            answer = file1.readline()
            science_questions[data[:-1]]= answer[:-1]
            temporary_list.extend(["A. " + str(optionA[:-1]),"B. " + str(optionB[:-1]),"C. " + str(optionC[:-1]),"D. " + str(optionD[:-1])])
            science_answers.append(temporary_list)
            counter += 6


start_app()
