import BuyApp
class Person:
    def __init__(self, First_Name, Last_Name):
        self.First_Name = First_Name
        self.Last_Name = Last_Name

    def talk(self):
        print("Hell0 " + self.First_Name + ' ' + self.Last_Name)


BuyApp.credit_score
person = Person("Zameer", "Delhve")
person.talk()

person1 = Person("Alifya", "Faizee")
person1.talk()
# print(person.First_Name + ' ' + person.Last_Name)
