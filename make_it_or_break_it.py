#Make It Or Break It - Version 1
#This Programme asks users questions until they lose, and winning 10 dollars for each question they answer correctly.
#Programme will end once a user has answered a question wrong. They are able to cash out at certain cash checkpoints, but will lose all their money if they do not cash out. 
#Questions in the programme are multichoice from 4 different options, with only 1 correct option to progress.

#importations
import time
import random


#Initialisation of Variables.
name = ""
money = 0
instructions_repeat = ""
question_number = "0"
answer = ""
correct_answer = ""
quit = ""
question1 = [1, 2, 3, 4]
question2 = [5, 6, 7, 8]
question3 = [9, 10, 11, 12]
question4 = [13, 14, 15, 16]
question5 = [17, 18, 19, 20]
question6 = [21, 22, 23, 24]
question7 = [25, 26, 27, 28]
question8 = [29, 30, 31, 32]
question9 = [33, 34, 35, 36]
question10 = [37, 38, 39, 40]

#defining 
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
        global question_number
        question_number = 1
        

    
        
def incorrect():

    time.sleep(1)
    print("You have answered with... \n{}!" .format(answer))
    time.sleep(2)
    print("Sorry! You have been disqualified! The right answer was... \n{}! \U0001F614".format(correct_answer))
    time.sleep(1)
    print("You lost with ${}!" .format(money))
    if money >= 50:
        print("however, since you reached the checkpoint of $50, you are able to cash out $50! \U0001F604")
        time.sleep(1)
        print("You have cashed out $50!")
        print("We'll see you next time!")
        time.sleep(1)
        exit()
    else:
        print("however, you are unable to cash out any money, due to not making the checkpoint!")
        print("We'll see you next time!")
        time.sleep(1)
        exit()        
    
   
def correct():
    print("You have answered with... \n{}!" .format(answer))
    time.sleep(2)
    print("Congratulations on answering the question correctly!")
    global money
    money += 10
    if money == 100:
        print("Congratulations! You have won $100, {}!".format(name))
        print("Thank you for playing, {}! You truly are quiz master!".format(name))
        time.sleep(1)
        exit()
        
    elif money == 50:
        print("Congratulations! You have passed the $50 dollar checkpoint!")
        time.sleep(1)
        print("Even if you get the next questions wrong, you will still be able to cash out $50!")
        time.sleep(2)
        quit = input("Would you like to quit and cash out now? \n" + "YES / NO\n" + "{}: " .format(name)).upper() 
        while quit == "NO":
            global question_number
            question_number += 1
            break
        else:
            while quit == "YES":
                print("Thank you for playing \"Make It Or Break It\"! \U0001F600")
                time.sleep(1)
                print("You have sucessfully cashed out ${}!" .format(money))
                time.sleep(1)
                exit()
    else:
        print("Your current balance is: ${}!".format(money))
        time.sleep(1)
        quit = input("Would you like to quit and cash out now? \n" + "YES / NO\n" + "{}: " .format(name)).upper()
        while quit == "NO":
            question_number += 1
            break
        else:
            print("Thank you for playing \"Make It Or Break It\"!")
            time.sleep(1)
            print("You have sucessfully cashed out ${}!" .format(money))
            time.sleep(1)
            exit()

#start of code 
print("")   
print("Welcome to Make It Or Break It!" + "\n")
while name == "":
        name = input("What is your name? ")

print("Hello, {}!" .format(name))
        
time.sleep(1)

#instructions function being used
instructions()
while question_number == 1: 
    if random.choice(question1) == 1:
        print("Question 1: What is the capital of New Zealand?")
        while answer == "":
            answer = input("A: Hamilton\nB: Auckland\nC: Christchurch\nD: Wellington\n{}: " .format(name)).upper()           
        correct_answer = "D"
        if answer == correct_answer:
            correct()
        elif answer != correct_answer:
            incorrect()
    elif random.choice(question1) == 2:
            print("Question 1: Pure water has a pH level of around?")
            answer = input("A: 8.5\nB: 7.5\nC: 7\nD: 8\n{}: " .format(name)).upper()
            correct_answer = "C"
            if answer == correct_answer:
                correct()
            elif answer != correct_answer:
                incorrect()
    elif random.choice(question1) == 3:
                print("Question 1: Who starts first in Chess?")
                answer = input("A: Black\nB: White\n{}: ".format(name)).upper()
                correct_answer = "B"
                if answer == correct_answer:
                    correct()
                elif answer != correct_answer:
                    incorrect()  
    elif random.choice(question1) == 4:
        print("Question 1: What color is your blood when it�s inside your body?")
        answer = input("A: Red\nB: Blue\nC: Purple\nD: Pink\n{}: " .format(name)).upper()
        correct_answer = "A"
        if answer == correct_answer:
            correct()
        elif answer != correct_answer:
            incorrect()
                    
time.sleep(1)

while question_number == 2:
    if random.choice(question2) == 5:
        print("Question 2: Which country produces the most coffee in the world?")
        answer = input("A: Colombia\nB: Vietnam\nC: Mexico\nD: Brazil\n{}: " .format(name)).upper()
        correct_answer = "D"
        if answer == correct_answer:
            correct()
        elif answer != correct_answer:
            incorrect()
    elif random.choice(question2) == 6:
                print("Question 2: Area 51 is located in which state?")
                answer = input("A: Iowa\nB: Nevada\nC: Florida\nD: Virginia\n{}: ".format(name)).upper()
                correct_answer = "B"
                if answer == correct_answer:
                    correct()
                elif answer != correct_answer:
                    incorrect()
    elif random.choice(question2) == 7:
            print("What fast food is the most ordered in America?")
            answer = input("A: Hot Dogs\nB: Burgers\nC: Fried Chicken\nD: Pizza\n{}: ".format(name)).upper()
            correct_answer = "C"
            if answer == correct_answer:
                correct()
            elif answer != correct_answer:
                incorrect()            
    elif random.choice(question2) == 8:
                    print("Question 2: What does the acronym, \"SMH\" stand for?")
                    answer = input("A: Shaking my hips\nB: Shaking my hand\nC: Shaking my head\nD: Sharing my heart\n{}: " .format(name)).upper()
                    correct_answer = "C"
                    if answer == correct_answer:
                        correct()
                    elif answer != correct_answer:
                        incorrect()
time.sleep(1)

while question_number == 3:
    if random.choice(question3) == 9:
        print("Question 3: Who created Sherlock Holmes?")
        answer = input("A: James Patterson\nB: Dashiell Hammett\nC: Raymond Chandler\nD: Arthur Conan Doyle\n{}: " .format(name)).upper()
        correct_answer = "D"
        if answer == correct_answer:
            correct()
        elif answer != correct_answer:
            incorrect()
    elif random.choice(question3) == 10:
                print("Question 3: Which planet has the most gravity?")
                answer = input("A: Uranus\nB: Jupiter\nC: Neptune\nD: Mars\n{}: ".format(name)).upper()
                correct_answer = "B"
                if answer == correct_answer:
                    correct()
                elif answer != correct_answer:
                    incorrect()
    elif random.choice(question3) == 11:
            print("Question 3: Which tech entrepreneur named his son X � A-12?")
            answer = input("A: Linus Sebastian\nB: Tim Cook\nC: Mark Zuckerberg\nD: Elon Musk\n{}: ".format(name)).upper()
            correct_answer = "D"
            if answer == correct_answer:
                correct()
            elif answer != correct_answer:
                incorrect()            
    elif random.choice(question3) == 12:
                    print("Question 3: What is a duel between three people called?")
                    answer = input("A: Truel\nB: Trinity\nC: Trifle\nD: Triad\n{}: " .format(name)).upper()
                    correct_answer = "A"
                    if answer == correct_answer:
                        correct()
                    elif answer != correct_answer:
                        time.sleep(1)

time.sleep(1)
                        
while question_number == 4:
    if random.choice(question4) == 13:
        print("Question 4! You are nearly at the checkpoint! What tragedy occured in 2001?")
        answer = input("A: 9/11 Attacks\nB: Christchurch Earthquakes\nC: Hurricane Katrina\nD: Syrian Civil War\n{}: " .format(name)).upper()
        correct_answer = "A"
        if answer == correct_answer:
            correct()
        elif answer != correct_answer:
            incorrect()
    elif random.choice(question4) == 14:
                print("Question 4! You are nearly at the checkpoint! What is the name of Batman�s butler?")
                answer = input("A: Frank\nB: Alfred\nC: Dean\nD: Pete\n{}: ".format(name)).upper()
                correct_answer = "B"
                if answer == correct_answer:
                    correct()
                elif answer != correct_answer:
                    incorrect()
    elif random.choice(question4) == 15:
            print("Question 4! You are nearly at the checkpoint! What is the name of the biggest technology company in South Korea?")
            answer = input("A: Hyundai\nB: SK Telecomms\nC: Samsung\nD: LG Electronics\n{}: ".format(name)).upper()
            correct_answer = "C"
            if answer == correct_answer:
                correct()
            elif answer != correct_answer:
                incorrect()            
    elif random.choice(question4) == 16:
                    print("Question 4! You are nearly at the checkpoint! Which country was the Caesar salad invented in?")
                    answer = input("A: Mexico\nB: Italy\nC: France\nD: Greece\n{}: " .format(name)).upper()
                    correct_answer = "A"
                    if answer == correct_answer:
                        correct()
                    elif answer != correct_answer:
                        incorrect()
                        
time.sleep(1)

while question_number == 5:
    if random.choice(question5) == 17:
        print("Question 5 - Checkpoint question! Who is the half-blood prince in Harry Potter?")
        answer = input("A: George Weasley\nB: Severus Snape\nC: Sirius Black\nD: Lucius Malfoy\n{}: " .format(name)).upper()
        correct_answer = "B"
        if answer == correct_answer:
            correct()
        elif answer != correct_answer:
            incorrect()
    elif random.choice(question5) == 18:
                print("Question 5 - Checkpoint question! What does the term \"piano\" mean?")
                answer = input("A: To be played smoothly\nB: To be played elegantly\nC: To be played beautifully\nD: To be played softly\n{}: ".format(name)).upper()
                correct_answer = "D"
                if answer == correct_answer:
                    correct()
                elif answer != correct_answer:
                    incorrect()
    elif random.choice(question5) == 19:
            print("Question 5 - Checkpoint question! Which country invented ice cream?")
            answer = input("A: Russia\nB: United States\nC: China\nD: Norway\n{}: ".format(name)).upper()
            correct_answer = "C"
            if answer == correct_answer:
                correct()
            elif answer != correct_answer:
                incorrect()            
    elif random.choice(question5) == 20:
                    print("Question 5 - Checkpoint question! What is the third sign of the zodiac?")
                    answer = input("A: Gemini\nB: Taurus\nC: Sagittarius\nD: Pisces\n{}: " .format(name)).upper()
                    correct_answer = "A"
                    if answer == correct_answer:
                        correct()
                    elif answer != correct_answer:
                        incorrect()

time.sleep(1)
                        
while question_number == 6:
    if random.choice(question6) == 21:
        print("Question 6: How many children does Oprah Winfrey have?")
        answer = input("A: 0\nB: 1\nC: 2\nD: 3\n{}: " .format(name)).upper()
        correct_answer = "A"
        if answer == correct_answer:
            correct()
        elif answer != correct_answer:
            incorrect()
    elif random.choice(question6) == 22:
                print("Question 6: What colour is a Giraffe's tongue?")
                answer = input("A: Black\nB: Pink\nC: Blue\nD: Purple\n{}: ".format(name)).upper()
                correct_answer = "C"
                if answer == correct_answer:
                    correct()
                elif answer != correct_answer:
                    incorrect()
    elif random.choice(question6) == 23:
            print("Question 6: What does �HTTP� stand for?")
            answer = input("A: HashText To Parse\nB: Harsh Transfer Text Process\nC: HyperText Transfer Protocol\nD: Hyphen To Transit Pact\n{}: ".format(name)).upper()
            correct_answer = "C"
            if answer == correct_answer:
                correct()
            elif answer != correct_answer:
                incorrect()            
    elif random.choice(question6) == 24:
                    print("Question 6: In the popular series, Pokemon, what Pokemon is the 151st Pokemon in the Pokedex?")
                    answer = input("A: Mew\nB: Mewtwo\nC: Dragonite\nD: Porygon\n{}: " .format(name)).upper()
                    correct_answer = "A"
                    if answer == correct_answer:
                        correct()
                    elif answer != correct_answer:
                        incorrect()
time.sleep(1)                        
                        
while question_number == 7:
    if random.choice(question7) == 25:
        print("Nearly There! Question 7: In publishing, what does POD mean?")
        answer = input("A: Paper only document\nB: Publicly official document\nC: Publish once, Draft\nD: Print on demand\n{}: " .format(name)).upper()
        correct_answer = "D"
        if answer == correct_answer:
            correct()
        elif answer != correct_answer:
            incorrect()
    elif random.choice(question7) == 26:
                print("Nearly There! Question 7: Who wrote the critically acclaimed Twilight books?")
                answer = input("A: Harper Lee\nB: Agatha Christie\nC: Toni Morrison\nD: Stephenie Meyer\n{}: ".format(name)).upper()
                correct_answer = "D"
                if answer == correct_answer:
                    correct()
                elif answer != correct_answer:
                    incorrect()
    elif random.choice(question7) == 27:
            print("Nearly There! Question 7: In what year did Steve Jobs die?")
            answer = input("A: 2009\nB: 2004\nC: 2011\nD: 2002\n{}: ".format(name)).upper()
            correct_answer = "C"
            if answer == correct_answer:
                correct()
            elif answer != correct_answer:
                incorrect()            
    elif random.choice(question7) == 28:
                    print("Nearly There! Question 7: When was the first computer invented?")
                    answer = input("A: 1943\nB: 1938\nC: 1945\nD: 1931\n{}: " .format(name)).upper()
                    correct_answer = "A"
                    if answer == correct_answer:
                        correct()
                    elif answer != correct_answer:
                        incorrect()
                        
time.sleep(1)                        
                        
while question_number == 8:
    if random.choice(question8) == 29:
        print("Question 8: How many elements are there in the periodic table?")
        answer = input("A: 96\nB: 104\nC: 118\nD: 122\n{}: " .format(name)).upper()
        correct_answer = "C"
        if answer == correct_answer:
            correct()
        elif answer != correct_answer:
            incorrect()
    elif random.choice(question8) == 30:
                print("Question 8: How many cards are there in a deck of Uno?")
                answer = input("A: 140\nB: 108\nC: 152\nD: 164\n{}: ".format(name)).upper()
                correct_answer = "B"
                if answer == correct_answer:
                    correct()
                elif answer != correct_answer:
                    incorrect()
    elif random.choice(question8) == 31:
            print("Question 8: Which bone are babies born without?")
            answer = input("A: Malleus\nB: Pelvis\nC: Kneecaps\nD: Tibia\n{}: ".format(name)).upper()
            correct_answer = "C"
            if answer == correct_answer:
                correct()
            elif answer != correct_answer:
                incorrect()            
    elif random.choice(question8) == 32:
                    print("Question 8: What�s the medical term for bad breath?")
                    answer = input("A: Halitosis\nB: Papillitis\nC: Ganglioneuralgia\nD: Borborygmi\n{}: " .format(name)).upper()
                    correct_answer = "A"
                    if answer == correct_answer:
                        correct()
                    elif answer != correct_answer:
                        incorrect()
                        
                        time.sleep(1)                        
                                                
while question_number == 9:
    if random.choice(question9) == 33:
        print("Question 9! You are one step closer to winning $100!\nWhat insect shorted out an early supercomputer and inspired the term \"computer bug\"?")
        answer = input("A: Moth\nB: Roach\nC: Ants\nD: Fly\n{}: " .format(name)).upper()
        correct_answer = "A"
        if answer == correct_answer:
            correct()
        elif answer != correct_answer:
            incorrect()
    elif random.choice(question9) == 34:
                print("Question 9! You are one step closer to winning $100!\nWhen is Canada Day?")
                answer = input("A: July 7th\nB: July 1st\nC: July 12th\nD: July 9th\n{}: ".format(name)).upper()
                correct_answer = "B"
                if answer == correct_answer:
                    correct()
                elif answer != correct_answer:
                    incorrect()
    elif random.choice(question9) == 35:
            print("Question 9! You are one step closer to winning $100!\nWhich animal symbolizes good luck in Europe?")
            answer = input("A: Deer\nB: Rabbit\nC: Ladybug\nD: Dolphin\n{}: ".format(name)).upper()
            correct_answer = "C"
            if answer == correct_answer:
                correct()
            elif answer != correct_answer:
                incorrect()            
    elif random.choice(question8) == 36:
                    print("Question 9! You are one step closer to winning $100!\nWhat is the name of a group of stars that form an imaginary picture?")
                    answer = input("A: Constellation\nB: Zodiac\nC: Astrophotography\nD: Star Trail\n{}:" .format(name)).upper()
                    correct_answer = "A"
                    if answer == correct_answer:
                        correct()
                    elif answer != correct_answer:
                        incorrect()
                        
while question_number == 10:
    if random.choice(question10) == 37:
        print("Final Question! Question 10: What was the original name of the popular search engine \"Google\"?")
        answer = input("A: Cipher\nB: Backrub\nC: Palo\nD: Junction\n{}: " .format(name)).upper()
        correct_answer = "B"
        if answer == correct_answer:
            correct()
        elif answer != correct_answer:
            incorrect()
    elif random.choice(question10) == 38:
                print("Final Question! Question 10: What letter is not included in any of the 50 U.S. state names?")
                answer = input("A: Q\nB: X\nC: Y\nD: Z\n{}: ".format(name)).upper()
                correct_answer = "A"
                if answer == correct_answer:
                    correct()
                elif answer != correct_answer:
                    incorrect()
    elif random.choice(question10) == 39:
            print("Final Question! Question 10: What animal is on the fashion brand Levi�s logo?")
            answer = input("A: Rhino\nB: Crocodile\nC: Horse\nD: Deer\n{}: ".format(name)).upper()
            correct_answer = "C"
            if answer == correct_answer:
                correct()
            elif answer != correct_answer:
                incorrect()            
    elif random.choice(question10) == 40:
                    print("Final Question! Question 10: What year was Queen Elizabeth II born?")
                    answer = input("A: 1926\nB: 1932\nC: 1934\nD: 1924\n{}: " .format(name)).upper()
                    correct_answer = "A"
                    if answer == correct_answer:
                        correct()
                    elif answer != correct_answer:
                        incorrect()