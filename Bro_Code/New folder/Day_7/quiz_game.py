questions = (
    ("Which metal has the highest melting point?:  "),
    ("How many colour can human eye see ?: "),
    ("What is i²(iota^sq.)?: "),
    ("How many bones in human adult body?: "),
    ("In OSI model, Application layer present at?: ")
)
options = [["A. Helium B.Tungsten C. Platnium D. Zirconium"],
          ["A. 8 B. 4 C. 7 D. 2"],
          ["A. 1 B. -1 C. 3 D. 11"],
          ["A. 207 B. 206 C. 45 D. 208"],
          ["A. 7th Layer B. 1st layer C. 5th layer D. 4th layer"]]
guesses = []
answers = ("B","C","B","B","A")
score = 0
question_num = 0
for question in questions:
    print("-"*30)
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter A B C D : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("CORRECT !!")
        score += 1
    else:
        print("Wrong Answer")
        print(f"{answers[question_num]} is the correct answer !")
    question_num += 1

print("----------------------")
print("       RESULT         ")
print("----------------------")
print("Answer: ",end="")
for answer in answers:
    print(answer, end=" ")
print()
print("Your Answer: ",end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/len(questions)*100 )
print(f"Your Score is: {score}%")