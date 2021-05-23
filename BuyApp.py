credit = input('Is your buyer credit good? ')
credit_score = credit.upper()
print(credit_score)
if credit_score == "YES":
    print("good credit")
elif credit_score == "NO":
    print("bad credit")
else:
    print("unknown credit")