#Quiz Game
# any Func will be as True when debugging / {starting} the program.
def new_game(): #will create a new game
    guesses = [] #sets, will store my guesses values
    correct_guesses = 0 #deafult 0 cause i recently started the game
    question_num = 1 #my first question begining starting

    for keys in questions:
        print(keys)
        for option in options[question_num-1]:
            print(option)
        question_num += 1

        write_guess = input("Enter (A,B,C, or D): ")
        write_guess = write_guess.upper()
        guesses.append(write_guess)
        correct_guesses += check_answer(questions.get(keys),write_guess) #correct question answer,

    display_score(correct_guesses, guesses) # when all question end
    # pass #placeHolder
#--------------
def check_answer(correct_guess, my_guess):
    if correct_guess == my_guess: #"A", "A"
        print("Correct")
        print("----#") #print new line empty
        return 1 # return +1 to my correct question
    else:
        print("Wrong")
        print()  # print new line empty
        return 0
    #pass
#--------------
def display_score(correct_answer,guesses): # it will be called when all question has been answered
    print("-=-=-=-=-=")
    print("Result")
    print("-----")
    print("Answers : ", end="")

    for i in questions: # i value1, value2...
        print(questions.get(i), end=" ") # Answers : A B C D A
    print()

    print("My Guesses : ", end="")
    for i in guesses:  # ["A","B",,,....]
        print(i, end=" ")  # Answers : A B C D A
    print()

    score = int(correct_answer / len(questions) *100)
    print("Your Score is : " , str(score) + "%")
    #pass
#--------------
def play_again(): # output will be : are u wanna to play again.

    response = input("Are u want to play again (y/n): ")
    response = response.lower()

    if response == "y":
        return True
    else:
        return False

    # pass
#--------------



# store questions as dictionary
questions = {
"What band was Harry Styles in before his solo career?":"A",
"What kind of food is Penne?":"B",
"Which Disney Princess called Gus and Jaq friends?":"C",
"Who is the President of the United States?":"D",
"What sport did David Beckham play?":"A",
}

#list[] of lists[] || list of tuples will work too if u want
options = \
[["A. One Direction","B. Two","C. three","D. four"],
["A. Boo","B. Pasta","C. Toast","D. Coola"],
["A. Cino","B. Cindra","C. Cinderella","D. Calorine"],
["A. joey","B. Joo","C. Joe Biden","D. Je i joe"],
["A. Football","B. Swimming","C. Tennis","D. Running"],]

new_game()

while play_again(): #true
    new_game()