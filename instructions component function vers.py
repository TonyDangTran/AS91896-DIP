import time


name = ""
instructions_repeat = ""

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
            instructions_repeat = input("Type YES to start!, otherwise NO to quit. \n{}: " .format(name)).upper()
    if instructions_repeat == "YES":
        print("\nGreat! Let's Start!" + "\n" + "===================================================================\n")

print("")   
print("Welcome to Make It Or Break It!" + "\n")
while name == "":
        name = input("What is your name? ")

print("Hello, {}!" .format(name))

instructions()