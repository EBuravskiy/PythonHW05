print("Enter an integer:")
number = int(input())
description = ""
if number == 0:
    description = "Zero number"
if number != 0:
    if number > 0:
        description = "Positive "
    else:
        description = "Negative "
    if number%2 == 0:
        description += "even number"
    else:
        description += "odd number"
print (description)