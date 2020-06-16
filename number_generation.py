import random

low = 1
high = 10

for item in range(1):
    hi_to_num = random.randrange(low, high)
    hi_to_num2 = random.randrange(low, high)

    question = "{} x {}".format(hi_to_num, hi_to_num2)
    print(question)
