import random

num_1 = random.randrange(1, 12)
num_2 = random.randrange(1, 12)

question = "{} + {} ".format(num_1, num_2)
correct = num_1 + num_2

user = int(input(question))

if user == correct:
    feedback = "great job"
else:
    feedback = "oops"

print(feedback)


