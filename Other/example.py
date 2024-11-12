import json

score = 0

with open("Other/questions.json", "r") as file:
    content = file.read()
data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1,"-", alternative)

    user_input = int(input("Enter the answer number: "))
    question["user_answer"] = user_input


for index, question in enumerate(data):
    if question["user_answer"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer!"
    else:
        result = "Incorrect Answer!"
    message = f"{index + 1} - {result} - Your Answer {question['user_answer']}, Corret Answer {question['correct_answer']}"
    print(message)


print(f"Your score is {score}/2")

