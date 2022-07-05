import time


name = ""
instructions_repeat = ""

def instructions():
    print("Welcome to \"Make It Or Break It\"!")
    print("To play \"Make It Or Break It\", You must answer questions until you lose, or until you give up!")
    print("For each question you answer correctly, you win $10 dollars! HOWEVER! Miss one question, and you lose ALL your money!")
    print("Do not worry! You can cash out after answering every question, and you can also guarantee yourself $50 if you can answer the 5th question, even if you get the next questions wrong!")
    print("Are you ready to MAKE it?")
    print("or are you going to BREAK it?")
    global instructions_repeat
    while instructions_repeat != "YES":
        if instructions_repeat == "NO":
            print("Goodbye, {}!" .format(name))
            time.sleep(1)
            exit()
        else:
            instructions_repeat = input("Type YES to start!, otherwise NO to quit. \n{}: " .format(name)).upper()
    if instructions_repeat == "YES":
        print("\nGreat! Let's Start!" + "\n" + "===================================================================\n")
        global question_number



print("Welcome to \"Make It Or Break It\"!")
print("To play \"Make It Or Break It\", You must answer questions until you lose, or until you give up!")
print("For each question you answer correctly, you win $10 dollars! HOWEVER! Miss one question, and you lose ALL your money!")
print("Do not worry! You can cash out after answering every question, and you can also guarantee yourself $50 if you can answer the 5th question, even if you get the next questions wrong!")
print("Are you ready to MAKE it?")
print("or are you going to BREAK it?")

repeat = input("would you like me to repeat the instructions?")
while repeat == "YES":
    print("Welcome to \"Make It Or Break It\"!")
    print("To play \"Make It Or Break It\", You must answer questions until you lose, or until you give up!")
    print("For each question you answer correctly, you win $10 dollars! HOWEVER! Miss one question, and you lose ALL your money!")
    print("Do not worry! You can cash out after answering every question, and you can also guarantee yourself $50 if you can answer the 5th question, even if you get the next questions wrong!")
    print("Are you ready to MAKE it?")
    print("or are you going to BREAK it?")
else:
    print("great! let us head to answering!")    

    


