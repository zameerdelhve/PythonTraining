credit = input('Is buyer credit good? ')
credit_score = credit.upper()
print(credit_score)
if credit_score == "YES" and 1==3:
    print("good credit")
elif credit_score == "NO":
    print("bad credit")
else:
    print("unknown credit")