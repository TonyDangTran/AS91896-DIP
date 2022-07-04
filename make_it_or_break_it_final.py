#Make It Or Break It - Final Version
#uses requests module to pull questions from an external API (functioning as a dictionary), in which the questions can then be called via a function. 
#much more flexible than previous version, in which it can go up to 50 questions, and uses less code to do so. 
#fixed boundary problems with money
#checkpoints work, being able to cash out the right amount of money. 
#name is capitialized and added extra aesthetic features such as emojis, and spaces
#imported time module for easier reading and smooth running. 


#requests module to request from the API
import requests
#html module 
import html
#randomises order in which the answers will appear.
import random
#imports time.sleep, which allows code to wait a few seconds before moving on.
import time
#imports json package to convert data from request module 
import json



#initalizing variables
name = ""
money = 0
instructions_repeat = ""
question_number = "0"
quit = ""
answer_check = False
checkpoint_money = 0


#initalizing functions
def incorrect(answer, correct_answer):

    time.sleep(1)
    print("You have answered with... \n{}!" .format(answer))
    time.sleep(2)
    print("Sorry! You have been disqualified! The right answer was... \n{}! \U0001F614".format(correct_answer))
    time.sleep(1)
    print("You lost with ${}!" .format(money))
    if money >= 50:
        print(f"however, since you reached the checkpoint of ${checkpoint_money}, you are able to cash out ${checkpoint_money}! \U0001F604")
        time.sleep(1)
        print("You have cashed out ${}!" .format(checkpoint_money))
        print("We'll see you next time!")
        print("===================================================================\n")
        time.sleep(1)
        exit()
    else:
        print("however, you are unable to cash out any money, due to not making the checkpoint!")
        print("We'll see you next time!")
        time.sleep(1)
        print("===================================================================\n")
        exit()        
    
   
def correct(answer):
    print("You have answered with... \n{}!" .format(answer))
    time.sleep(2)
    print("Congratulations on answering the question correctly!")
    global money
    money += 10
    if money == 500:
        print("Congratulations! You have won $500, {}!".format(name.capitalize()))
        print("Thank you for playing, {}! You have MADE it!".format(name.capitalize()))
        time.sleep(1)
        print("===================================================================\n")
        exit()
        
    elif money % 50 == 0:
        global checkpoint_money
        checkpoint_money += 50
        print("Congratulations! You have passed the {} dollar checkpoint!".format(checkpoint_money))
        time.sleep(1)
        print("Even if you get the next questions wrong, you will still be able to cash out ${}!" .format(checkpoint_money))
        time.sleep(2)
        quit = input("Would you like to quit and cash out now? \n" + "YES / NO\n" + "{}: " .format(name.capitalize())).upper() 
        while quit == "NO":
            break
        else:
            while quit == "YES":
                print("Thank you for playing \"Make It Or Break It\"! \U0001F600")
                time.sleep(1)
                print("You have sucessfully cashed out ${}!" .format(checkpoint_money))
                time.sleep(1)
                exit()
    else:
        print("Your current balance is: ${}!".format(money))
        time.sleep(1)
        quit = input("Would you like to quit and cash out now? \n" + "YES / NO\n" + "{}: " .format(name.capitalize())).upper()
        while quit == "NO":
            break
        else:
            print("Thank you for playing \"Make It Or Break It\"!")
            time.sleep(1)
            print("You have sucessfully cashed out ${}!" .format(money))
            time.sleep(1)
            exit()


def instructions():
    print("Welcome to \"Make It Or Break It\"!")
    time.sleep(1)
    print("To play \"Make It Or Break It\", You must answer questions until you lose, or until you give up!")
    time.sleep(2)
    print("For each question you answer correctly, you win $10 dollars!")
    time.sleep(3)
    print("HOWEVER!")
    time.sleep(1)
    print("Miss one question, and you lose ALL your money!")
    time.sleep(2)
    print("Do not worry! You can cash out after answering every question, and you can also guarantee yourself $50 if you can answer the 5th question,\neven if you get the next questions wrong!")
    time.sleep(5)
    print("Are you ready to MAKE it?")
    time.sleep(1)
    print("or are you going to BREAK it?")
    time.sleep(2)   
    global instructions_repeat
    while instructions_repeat != "YES":
        if instructions_repeat == "NO":
            print("Goodbye, {}!" .format(name))
            time.sleep(1)
            exit()
        else:
            instructions_repeat = input("Type YES to start!, otherwise NO to quit. \n{}: " .format(name.capitalize())).upper()
    if instructions_repeat == "YES":
        print("\nGreat! Let's Start!" + "\n" + "===================================================================\n")
        global question_number


#start of code

print("")   
print("Welcome to Make It Or Break It!" + "\n")
while name == "":
        name = input("What is your name? ")

print("Hello, {}!".format(name.capitalize()))

#instructions is called
instructions()


#after instructions while True loop is executed
while True:
    try:
        data = requests.get('https://opentdb.com/api.php?amount=1&type=multiple')
        data = json.loads(data.text)
        data = data['results']
        question_type = data[0]['type'] 
        question = data[0]['question'] #Take value question from the list
        question = html.unescape(question) #Turns html entities into unicode symbols
        if question_type == 'multiple': #Multiple choice type questions
            correct_answer = html.unescape(str(data[0]['correct_answer'])) #Takes the corrrect answer string varaible from the list generated by the api
            incorrect_answers = data[0]['incorrect_answers'] #Takes the incorrect answers list varaible from the api
            answers = incorrect_answers 
            answers.append(correct_answer) #Creates a new list called answers containing both correct and incorrect answers
            random.shuffle(answers) #Randomises the values inside the list
            for i in range(len(answers)): #Turns html entities into unicode symbols for all answers
                answers[i] = html.unescape(answers[i])

    except requests.exceptions.RequestException:
        print('Connection Error') #error to let users know a problem has occured 

    while not answer_check: #answer check so that only valid inputs are taken
        print(question)
        print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}")
        answer = input("{}: " .format(name.capitalize())).upper()
        if answer.lower() != 'a' and answer.lower() != 'b' and answer.lower() != 'c' and answer.lower() != 'd': #invalid input checking
            print('That is an invalid answer.') 
        else:
            answer_check = True #True = valid input
#valid input, then checks if answer is correct or incorrect. 
    if answer.lower() == 'a':
        if answers[0] == correct_answer:
            correct(answer)
        else:
            incorrect(answer, correct_answer)

    if answer.lower() == 'b':
        if answers[1] == correct_answer:
            correct(answer)
        else:
            incorrect(answer, correct_answer)

    if answer.lower() == 'c':
        if answers[2] == correct_answer:
            correct(answer)
        else:
            incorrect(answer, correct_answer)

    if answer.lower() == 'd':
        if answers[3] == correct_answer:
            correct(answer)
        else:
            incorrect(answer, correct_answer)
    answer_check = False #resets value to False to stop answer check loop. 
