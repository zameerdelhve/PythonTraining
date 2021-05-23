class Person:
    def __init__(self,First_Name, Last_Name):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
    def talk(self):
        print ("Hell0 " + self.First_Name + ' ' + self.Last_Name)




person = Person("Zameer", "Delhve")
person.talk()
#print(person.First_Name + ' ' + person.Last_Name)

