import random

import string

RC = []

DigitsGenerated = 0

while DigitsGenerated != 6:

    LetterOrNumber = random.randint(0,1)

    if LetterOrNumber == 0:

        randomLetter = random.choice(string.ascii_uppercase)

        RC.append(randomLetter)

        DigitsGenerated = DigitsGenerated + 1

    elif LetterOrNumber == 1:

        randomNumber = random.randint(0,9)

        num2str = str(randomNumber)

        RC.append(num2str)

        DigitsGenerated = DigitsGenerated + 1

print("Room Code: " + RC[0] + RC[1] + RC[2] + RC[3] + RC[4] + RC[5])

#find a way to shorten this line plz ↑
