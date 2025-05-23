questions = ("How many elements are there in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in the Earth's Atmosphere?: ",
                       "How many bones are there in the human body?: ",
                       "Which planet in the solar system is the hottest?:")

options = (("A. 116 ", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. CO2", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers =("C", "D", "A", "A", "B")
guesses =[]
score = 0
question_num = 0

for question in questions:
    print("----------------------------------------------------------------------------------------------------")
    print(f"Question No {question_num + 1}: {question}")
    print("----------------------------------------------------------------------------------------------------")
    print()
    for option in options[question_num]:
        print(option)
    print("----------------------------------------------------------------------------------------------------")
    guess = input("Enter the Correct Option Like (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Your Answer is Correct!")
    else:
        print("Your Answer is Wrong!")
        print("Correct Answer is: ", answers[question_num])
    question_num += 1

print("----------------------------------------------------------------------------------------------------")
print("                                                         RESULTS                                                             ")
print("----------------------------------------------------------------------------------------------------")

print("Correct Answers Are: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Your Guesses Were: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
score = int(score/len(questions) * 100)
print(f"Your Score is: {score}%")
print("----------------------------------------------------------------------------------------------------")
print()