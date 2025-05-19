def make_integer(txt): # TODO
    try:
        return int(txt) + 10
    except ValueError:
        return 0


def is_year_leap(year): # TODO
    if not year % 4 and year % 100 or not year % 400:
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")

def matrix():
    for row in range(1,6):
        for col in range(1,6):
            matrix = row * col
            print(f"{matrix:3}",end=" ")
        print()

def greet(name, message = "Hello"):
    print(f"{message},{name}!")

def remove_dublicate(lst): # TODO
    for i in lst:
        if lst.count(i) > 1:
            lst.remove(i)
    print(lst)

def sorted_dict(dict):
    # scores = {'Alice': 91, 'Bob': 85, 'David': 99}
    #sorted_students = sorted(dict.items(),key=lambda item: item[1],reverse=True)
    students_list = list(dict.items())
    print(students_list)
    students_list.sort(key=lambda x: x[1], reverse=True)
    print(students_list)
    for name, _ in students_list:
        print(name)

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for i in text:
        if i not in vowels:
            result+=i
    print(result)

def file_handling(name):
    with open("names.txt","a") as f:
        f.write(f"{name}""\n")

def exeption_handling():
    try:
        num = input("Input number :")
        number = int(num)
        result = 10 / number
        print(num)
    except ValueError:
        print("Its not valid number, Please enter numeric value")
    except ZeroDivisionError:
        print("Cannot divide by zero")

class rectangle:
    def __init__(self):
        self.__height = 0
        self.__width = 0
    
    def set_height(self,height):
        self.__height = height

    def set_width(self,width):
        self.__width = width

    def area(self):
        return self.__width * self.__height
        



        
    
    
if __name__ == "__main__":
    # txt = input("Input number: ")
    # print(make_integer(txt))
    # year = 2024
    # is_year_leap(year)
    # matrix()
    # greet("Alice","Wlcome")
    # greet("Lyov")
    # lst = [1, 2, 2, 3, 1, 4] 
    # remove_dublicate(lst)
    # scores = {'Alice': 91, 'Bob': 85, 'David': 99}
    # sorted_dict(scores)
    # text = "Hello World"
    # remove_vowels(text)
    # name = input("What is your name :")
    # file_handling(name)
    # exeption_handling()
    obj = rectangle()
    obj.set_height(15)
    obj.set_width(10)
    print(obj.area())






