import random

low = 1
high = 12

for item in range(1):
    num_1 = random.randrange(low, high)
    num_2 = random.randrange(low, high)

    question = "{} x {}".format(num_1, num_2)
    print(question)
