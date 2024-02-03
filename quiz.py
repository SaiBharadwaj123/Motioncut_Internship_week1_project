# Creating a list contain  dictionary which has question , options and answer
#list with hard questions
hardquestions = [
    {"question": "Which of the following is a correct way to open a file in Python for reading?", "options": ["file = open(""example.txt"", ""w"")","file = open(""example.txt"", ""r"")","file = open(""example.txt"", ""a"")","file = open(""example.txt"", ""x"")"], "answer": "file = open(""example.txt"", ""r"")"},
    {"question": "What is the purpose of the __slots__ attribute in a Python class?", "options": ["To specify the methods of a class","To declare private variables","To restrict the attributes a class can have","To define the slots for storing instance variables"], "answer": "To restrict the attributes a class can have"},
    {"question": "What is the purpose of the __del__ method in Python?", "options": ["To delete an instance of a class","To define a destructor method","To deallocate memory resources","To call the superclass constructor"], "answer": "To define a destructor method"}
]
#list with average questions
averagequestions =[
    {"question": "What is the purpose of the __init__ method in a Python class?", "options": ["To initialize the class object","To define a new instance method","To create a static method","To declare class variables"], "answer": "To initialize the class object"},
    {"question": "What is the purpose of the try and except blocks in Python?", "options": ["To define a new function","To handle exceptions and errors","To create a loop","To check the syntax of the code"], "answer": "To handle exceptions and errors"},
    {"question": "What does the len() function do in Python?", "options": ["Returns the length of a string","Returns the length of a list, tuple, or sequence","Returns the length of an integer","Returns the length of a dictionary"], "answer": "Returns the length of a list, tuple, or sequence"}
]
#list with simple questions
simplequestions = [
    {"question": "Which of the following is the correct way to comment out multiple lines in Python?", "options": ["/* This is a comment */","# This is a comment","// This is a comment","-- This is a comment"], "answer": "# This is a comment"},
    {"question": "Which of the following data types is mutable?", "options": ["int","float","str","list"], "answer": "list"},
    {"question": "Which of the following is used to accept user input in Python?", "options": ["input()","get()","read()","scan()"], "answer": "input()"}
]
#Selecting answers by the user
def get_user_answer(question):
    print(question['question'])
    print("\n".join(f"{i}. {option}" for i, option in enumerate(question['options'], start=1)))
    while True: 
        try:
            user_answer = int(input("Enter your answer: "))
            #Check that the chosen option is correct or not
            if 1 <= user_answer <= len(question['options']): 
                return user_answer
            else:
                print("Invalid answer. Please enter a number between 1 and", len(question['options']))
        except ValueError:
            print("Invalid input. Please enter a number.")
#checking answer is correct or not
def check_user_answer(question, user_answer): 
    correct_answer = question['options'].index(question['answer']) + 1
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is", question['answer'])
        return False
def main():
    score = 0
    print("Welcome to Python Quiz\nSelect difficulty level")
    print("For simple questions press 1\nFor average questions press 2 \nFor hard questions press 3 ")
    #choosing the difficulty level
    level = int(input("Enter level"))
    if level == 1:
        questions = simplequestions
    elif level == 2:
        questions = averagequestions
    elif level == 3:
        questions = hardquestions
    else:
        print("Enter correct level")
        main()
    #calculate the score
    for question in questions:
        #calling get_user_answer to get answer from the user 
        user_answer = get_user_answer(question)
        #checking if the chosen answer is correct or not
        if check_user_answer(question, user_answer):
            score += 1
    print("\nQuiz Complete! Your final score is", score, "/", len(questions))
if __name__ == "__main__":
    #Calling the main()
    main()