#---------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter(A,B,C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses,guesses)

#---------------------------------
def check_answer(answer,guess):
    if answer==guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG")
        return 0

#---------------------------------
def display_score(correct_guesses,guesses):
    print("RESULTS")
    print("-----------------------------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

#---------------------------------

def play_again():
    
   response = input("Do you want to play agin?(yes or no): ")
   response = response.upper()
   if response == "YES":
       return True
   else:
       return False

#---------------------------------

questions = {
    "who created python? ":"A",
    "Which year was python created? ":"B",
    "Python is tributed to which comedy group? ":"C",
    "Is the earth round? ":"B"
}

options = [["A.guido","B.helon","C.bill","D.mark"],
           ["A.1989","B.1991","C.2000","D.2016"],
           ["A.lonely","B.smosh","C.monty","D.SNL"],
           ["A.true","B.false","C.sometimes","D.what's earth"]]
new_game()

while play_again():
    new_game()

print("BYEEEEEEEE")