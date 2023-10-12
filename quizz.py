score = 0

print("Welcome to this quizz")
#Ask the user if the want to play the quizz
def user_input():
#Ask the user if they want to play the game or not
    user_prompt=input("Do you want to play the quizz?: (yes/no) ").lower().strip()


    if user_prompt!="yes":
        print('Enter (yes/no)')
        user_input()
    elif user_input == 'no':
        quit()
    else:
        print("Lets begin the game,make sure you answer all the questions")
user_input()

#function to show the different questions displayed to the user
def game_questions():
    global score
    question_one=input("who is the founder of python?: ").lower()
    if question_one!= "Guido van Rossum".lower():
        print("INCORRECT")
    
    else:
        print("Correct!")
        score += 1


    question_two=input("which year was python  first released?: ").strip(" ")
    if question_two.isdigit() and question_two == "1991":
        question_two=int(question_two)
        print("CORRECT")
        score += 1
    else:
        print("INCorrect!")
    

    question_three=input("Which type of Programming does Python support?: ").lower()
    answers=["object-oriented programming", "structured programming", "functional programming"]
   
    if question_three not in answers:
        print("INCORRECT")

    else:
        print("Correct!")
        score += 1

    question_four=input("Is python compiled or interpreted? ").lower()
    if question_four=="interpreted":
       print("Correct!")
       score += 1
    else:
        print("INCORRECT")    


    question_five = input("Does python support for each loop?: ").lower()
    if question_five == "no":
        print("CORRECT!")
        score += 1
    else:
        print("INCorrect!")
    

    print(f"your mark was {score*20}%")



game_questions()



