class Student:
    def __init__(self,name,age,bank_acc):
        self.name = name
        self.age = age
        self.__ban = bank_acc
    
    def introduce(self):
        print(f"My name is {self.name} and my age is {self.age} and my acc number is {self.__ban}")

    
# s1 = Student("harsh", 22, 789654123)
# s2 = Student("aman", 22, 1234567890)

# s1.introduce()
# s2.introduce()
# print(s1._Student__ban)


from abc import ABC, abstractmethod
class Bank(ABC):
    def __init__(self,user_name, user_acc):
        self.user_name = user_name
        self.__user_acc = user_acc
        pass

    def getdetails(self):
        print(f"name : {self.user_name}")
    
    @abstractmethod
    def acc(self):
        pass

class Account(Bank):
    def getdetails(self):
        super().getdetails()
        print(f"account number {self._Bank__user_acc}")

    def acc(self):
        return super().acc()


c1 = Account("Harsh", 78962582)

c1.getdetails()