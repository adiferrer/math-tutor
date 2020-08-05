import random, datetime, time

# prints out the current date
print(f'TODAY IS {datetime.date.today()}')

# gets the name of the user and checks if they put a name 
name = str(input('Welcome to SumTimes! What is your name? '))
while len(name) == 0:
    name = str(input('Welcome to SumTimes! What is your name? '))

# gets the input of the user
qnum = input(f"\nHi, {name.title()}! How many questions do you want to have in this quiz?\nMinimum of 5, maximum of 50: ")
while len(qnum) == 0 or int(qnum) >= 50 or int(qnum) <= 4:
    qnum = input("Please enter a valid number (5-50): ")

mode = input("\nWhat do you want to practice today?\nType 1 for Addition and 2 for Multipication: ")
while len(mode) == 0 or int(mode) < 1 or int(mode) > 2:
    mode = input("Please enter a valid number (1 or 2): ")

prompt = 0
score = 0
start = time.time()
answer_sheet = []

# addition
if int(mode) == 1:
    # verifies input
    limit = input("\nWhat's your limit in addition? (e.g. 13) ")
    while len(limit) == 0:
        limit = input("Please enter a number: ")
    print("")

    # prints out the customized questions
    while prompt < int(qnum):
        prompt += 1
        num1 = random.randint(1,int(limit))
        num2 = random.randint(1,int(limit))
        sum = num1 + num2
        question = input(f"{prompt}. {num1} + {num2} = ")
        while len(question) == 0:
            question = input("Plese answer the latest question: ")
        answer_sheet.append(f"{prompt}. {num1} + {num2} = {sum}")
        if int(question) == sum:
            score += 1
        end = time.time()

# multiplication
elif int(mode) == 2:
    # verifies input
    limit = input("\nWhat's your limit in the multiplication table? (e.g. 13) ")
    while len(limit) == 0:
        limit = input("Please enter a number: ")
    print("")

    # prints out the customized questions
    while prompt < int(qnum):
        prompt += 1
        num1 = random.randint(1,int(limit))
        num2 = random.randint(1,int(limit))
        product = num1 * num2
        question = input(f"{prompt}. {num1} x {num2} = ")
        while len(question) == 0:
            question = input("Plese answer the latest question: ")
        answer_sheet.append(f"{prompt}. {num1} x {num2} = {product}")
        if int(question) == product:
            score += 1
        end = time.time()



# prints out a comment based on the status of the score
print("")
half_score = round(int(qnum) / 2)
if score < half_score:
    print(f"Oh, bummer! Well, just keep on practicing, {name.title()}!\n")
elif score > half_score and score != int(qnum):
    print(f"Nice job, {name.title()}! You're almost there!\n")
elif score == int(qnum):
    print(f"You're a genius, {name.title()}!\n")

# prints out results

rate = score/int(qnum) * 100
print(f'Total time to answer: {round(end-start)} seconds')
print(f'Average speed per question: {round(int(end - start) / int(qnum))} seconds\n')
print(f'You got {score} out of {qnum}!')
print(f'And with a rate of: {round(rate)}%')
print("Nevertheless, thanks for playing!\n")
print("Here are the answers:")

# prints the answer sheet
for a in answer_sheet:
    print(a)
