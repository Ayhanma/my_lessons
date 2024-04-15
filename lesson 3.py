# name = 'Ayhan'
# def say_name():
#     global name 
#     name = 'Seyran'
#     print(name)

# # print(name)
# def say_hello_2():
#     print(name)
# say_hello_2()
# say_name()

# c = 10  


# def mul():
#     global c
#     c = c * 10 
#     print("Значение в функции:", c)  

# # mul()  
# print("Значение вне функции:", c)  
# def sellect(input_funk):
#     def output_funk():
#         print('**********')
#         input_funk()
#         print('**********')
#     return output_funk
# @sellect 
# def hello():
#     print('Hello world')
# hello()
# def math():
#     print(2 + 3)
    
# a = math
# a()
# def check(input_funk):
#     def output_funk(*args):
#         print('*****')
#         input_funk(*args)
#         print('*****')
#     return output_funk
# @check 
# def print_person(name,age):
#     print(f'Hello {name},{age}')
# print_person('Ayhan',15)
# class Rectangle():
#     def __init__(self,width,length):
#         self.length = length
#         self.width = width
#     def area(self):
#         print(self.width*self.length)
#     def perimetr(self):
#         print(2*(self.width+self.length))
# rect = Rectangle(2,3)
# rect.area()
# rect.perimetr()
# a = 3000
# class BankAccount():
#     def __init__(self):
#         self.account_number = 1234542626
#         self.balance = a
#     def add(self, num):
#         self.balance += num 
#         print(self.balance)
#     def withdraw(self, num1):
#         if num1 < self.balance:
#             self.balance -= num1 
#             print(self.balance)
#         else:
#             print(False)
# acc = BankAccount()
# acc.add(200)
# acc.withdraw(800)
# mat = [
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ]
# print(f'mat:{mat}')
# for i in range(0,len(mat)):
#     print(f'mat[{i}]:{mat[i]}')
#     for j in range(0,len(mat)):
#         print(f'mat[{i}][{j}]:{mat[i][j]}')