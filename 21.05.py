# def factorial(num):
#     if num < 0:
#         raise ValueError("Factorial is not defined for negative integers")   
#     result = 1
#     for i in range(2,num + 1):
#         result *= i
#     print(result)

# def sum_of_digits(num):
#     if num < 0:
#         raise ValueError("Input must be a positive number")
#     print(sum(int(digit)for digit in str(num)))



# def is_palidrome(num):
#     if num < 0:
#         return False
#     original = num
#     reversed_num = 0
#     while num > 0:
#         reversed_num = reversed_num * 10 + num % 10 
#         num //= 10
#     return original == reversed_num

# def max_digit(num):
#     return max(int(digit) for digit in str(num))

# def sum_even(num):
#     total = 0
#     for i in range(num):
#         total += i * 2
#     return total


# def func(num):
#     i = num
#     bajanarar = 1
#     while i > 0:
#         a = i % 10
#         if a > 0:
#             if num % a == 0:
#                 print(a)
#                 bajanarar *= a
#         i //= 10
#     return bajanarar

# def func1(lst):
#     counts = []
#     count = 0
#     for i in lst:
#         if i == 1:
#             count += 1
#         elif count > 0:
#             counts.append(count)
#             count = 0
#     print(counts)
#     return max(counts)

# def func1(lst):
#     counts = []
#     count = 0
#     for i in lst:
#         if i == 1:
#             count += 1
#         elif count > 0:
#             counts.append(count)
#             count = 0
#     if count > 0:  # Add this to handle end of list
#         counts.append(count)
#     print(counts)
#     return max(counts) if counts else 0  # Handle case where no 1s exist


def func3(txt):
    # lst = []
    # brackets = "(,),[,]{,}"
    # for item in str:
    #     if item in brackets:
    #         lst.append(str.count(item))
    # if len(str) % 2 == 1:
    #     return False
    # else:
    #     return True
    lst = ["(", ")", "[", "]", "{", "{", "}"]
    for i in lst:
        new_lst = txt.split(i)
        x = "".join(new_lst)  
        txt = x
        print(new_lst)   


if __name__ == "__main__":
    num = 121
    # factorial(num) 
    # sum_of_digits(num)
    # print(is_palidrome(num))
    # print(max_digit(num))
    # print(sum_even(4))
    print(func3("sdasdad(dsaad[dsadada)asdadsa]"))


