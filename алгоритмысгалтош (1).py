# # name=('jon'+
# #       "smith")
# #
# # print(name)
# num1='45' #cast
# num2=45
# print(num1+num2)  #конкетакция
# print(int(num1+num2

# день2
# name='jon'+"smith"
# name2='smith john'
# name=name2
# print(name)
#
# num1='45' # cast
# num2=45
# print(f'result={int(num1)+num2}')

#день3
# print(input('enter number: '))

#calculator, coffee machine, atm terminal
# num1=45
# num2=33
# print(num1+num2)

# num1= float(input('enter first number:'))
# num2= float(input('enter second number:'))
# print(num1+num2)


# print('welcome to calculator')
# num1= float(input('enter first number:'))
# num2= float(input('enter second number:'))
# result = num1+num2
# print(f'the result: {round(result,2)}')


# welcome = 'welcome to calculator'
# print(welcome)
# print(type(welcome))
# print('welcome to calculator')
# num1= float(input('enter first number:'))
# num2= float(input('enter second number:'))
# result = num1+num2
# print('the type of result is {}:'.format(type(result)))
# print('the type of result is %d:' %type(result))
# print(f'the result: {round(result,2)}')
#
# age = int(input('what is your age?'))
# if age < 16:
#     print('you are too young')
# elif 16 < age < 26:
#     print('you are teenager')
# else:
#     print('you are olf enough')


#день 4
# l = [32,56,69]
# l = ['56','96']
# l = [432,56,'text', None]

# drinks = ['espresso','latte', 'cappuccino']
# print('hello to coffee machine')
# drinks.append('americano')
# drinks = sorted(drinks)
#for i,v in enumerate(drinks):
#   print(i, v)

# choice = input('what would you like to drink?')
# if choice == 'espresso':
#     print('one espresso coming up')
# elif choice == 'latte':
#     print('one latte coming up')
# else:
#     print('one cappuccino coming up')





# while True:
#         ops = input('enter operations(+,-,*,/) or q/quit to exit')
#         if ops == 'quit' or ops == 'q':
#             break
#         num1= int(input('enter first number: '))
#         num2= int(input('enter second number: '))
#         result=0
#         if ops == '+':
#             result= num1 + num2
#         elif ops == '-':
#             result = num1 - num2
#         elif ops == '*':
#             result = num1 * num2
#         else:
#             result = num1 / num2
#         print(f'result is: {result}')

#5 день
# drinks =  ['espresso','latte', 'cappuccino']
# for i in range(len(drinks)):
#     print(i, drinks[i])
#     # print(drinks[i])
# for i,v in enumerate(drinks):
#     print(i, v)


#return vs void\
# def calc(name= 'john',surname='smith'):
#     return f'hello {name} {surname}'
# print(calc(name='john',surname='smith'))
#
#
# def calc(name,surname):
#     return f'hello {name} {surname}'
# print(calc(name='john',surname='smith'))
#

# def calc():
#     name = input('your name: ')
#     surname = input('your surname: ')
#     return f'hello {name} {surname}'
# print(calc)

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mult(a,b):
#     return a*b
# def div(a,b):
#     return a/b
#
#
# def main():
#     while True:
#         ops = input('enter operations(+,-,*,/) or q/quit to exit')
#         if ops == 'quit' or ops == 'q':
#             break
#         num1 = int(input('enter first number: '))
#         num2 = int(input('enter second number: '))
#         result = 0
#         if ops == '+':
#             result = add(num1, num2)
#         elif ops == '-':
#             result = sub(num1, num2)
#         elif ops == '*':
#             result =mult(num1, num2)
#         else:
#             result = div(num1, num2)
#         print(f'result is: {result}')


# def show_drink(drinks):
#     print("here is today's menu")
#     for i,v in enumerate(drinks):
#         print(i,v)
# def take_order(drinks):
#     choice = input('what would you like to order?')
#     if choice in drinks:
#         return choice
#     return None
# drinks =  ['espresso','latte', 'cappuccino']
# def make_drink(coffee):
#     print(f'one {coffee} coming up')
# print('hello to coffee machine')
# show_drink(drinks)
# drink = take_order(drinks)
# if drink is None:
#     print('no such coffee')
# else:
#     make_drink(drink)

#следующий день
# # try:
# #     number = int(input('enter a whole number: '))
# #     number2 = int(input('second number: '))
# #     print(f'you entred: {number/number2}')
# # except ValueError:
# #     print('that was not a whole number')
# # except ZeroDivisionError:
# #     print('you cannot devide by 0')
# def ask_for_number(prompt):
#     while True:
#         text = input(prompt)
#         try:
#             return float(text)
#         except ValueError:
#             print(f'{text} is nnot a number. Try again')
#         except ZeroDivisionError:
#             print(f'DIVISION TO ZERO IS NOT ALLOWED')
# def add(num1,num2):
#     return num1+num2
# def sub(num1,num2):
#     return num1-num2
# def mult(num1,num2):
#     return num1*num2
# def div(num1,num2):
#     if num2 == 0:
#         raise ZeroDivisionError()
#     return num1/num2
# def isAgain():
#     return True if input('do you want again(yes,no): ') == 'yes' else False
# #     a = input('do you want again(y,n)')
# #     if a == 'y':
# #         return True
# #     else:
# #         return False
#
#
# def calc():
#     while True:
#         num1=ask_for_number('Enter first number: ')
#         num2=ask_for_number('Enter second number: ')
#         op = input('Enter operation()+,-,*,/: ')
#         result = 0
#         if op == '+':
#             result = add(num1,num2)
#         elif op == '-':
#             result = sub(num1,num2)
#         elif op == '*':
#             result = mult(num1,num2)
#         else:
#             result = div(num1,num2)
#         print(f'result is: {result}')
#         if not isAgain():
#             break
# calc()

# l = [32,65,89,45]
# d = {'name':'john','surname':'smith'}
# d2 =[
# {'name':'john','surname':'smith'},
# {'name':'mary','surname':'son'}
# ]
# for i,v in d.items():
#     print(i,v)
# for i in d2:
#     print(i['name'])



# ноывй день

# l = [3,2,5,1]
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while j>=0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1] = key
#     return arr
# print(insertion_sort(l))

# l = [3,2,5,1]
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#             if min_idx != i:
#                 arr[min_idx], arr[i] = arr[i], arr[min_idx]
#     return arr
# print(selection_sort(l))

# def ask_for_number(prompt):
#     while True:
#         text = input(prompt)
#         try:
#             return float(text)
#         except ValueError:
#             print(f'{text} is nnot a number. Try again')
#         except ZeroDivisionError:
#             print(f'DIVISION TO ZERO IS NOT ALLOWED')
#
# def show_balance(account):
#     print(f"current balance {account['balance']:.2f}C")
# def deposit(account):
#     amount = ask_for_number('enter amount: ')
#     account['balance'] += amount
#     print(f"Deposited {amount:.2f} C")
# def withdraw(account):
#     amount = ask_for_number('enter amount: ')
#     account['balance'] -= amount
#     print(f"Withdrawn {amount:.2f} C")
# account = {'balance':100.00}
# print('welcome to the atm')
# show_balance(account)
# deposit(account)
# withdraw(account)
# show_balance(account)
#
# while True:
#     print()
#     print('1. Show balance')
#     print('2. Deposit')
#     print('3. Withdraw')
#     print('4. Quit')
#     choice = input('Choose an operation: ')
#     if choice == '1':
#         show_balance(account)
#     elif choice == '2':
#         deposit(account)
#     elif choice == '3':
#         withdraw(account)
#     elif choice == '4':
#         break
#     else:
#         print('Unknown choice')
# print('good bye')

# новый день
# quick sort
# l=[45,23,12,55,27]
# smaller=[23,12,27]
# equal=[45]
# larger=[55]
# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr
#     pivot= arr[0]
#     smaller=[i for i in arr if i<pivot]
#     equal=[i for i in arr if i==pivot]
#     larger=[i for i in arr if i> pivot]
#     return quick_sort(smaller) + equal + quick_sort(larger)
# print(quick_sort(l))


# l=[45,23,12,55,27]
# def radix_sort(arr):
#
#     exp=1
#     max_num = max(arr)
#     while max_num // exp > 0:
#         buckets = [[]for i in range(10)]
#         for num in arr:
#             remainder = num // exp
#             digit = remainder % 10
#             buckets[digit].append(num)
#         arr =[i for bucket in buckets for i in bucket]
#         exp *= 10
#     return arr
# print(radix_sort(l))
#
#
# import random
# secret = random.randint(1,100)
# attempts = 0
# while True:
#     guess = int(input("Guess a number between 1 and 100: "))
#     attempts += 1
#     if attempts > 5:
#         print('you ran out of attempts')
#         print(f'the number was {secret}')
#         break
#     if guess < secret:
#         print("Too low")
#     elif guess > secret:
#         print("Too high")
#     else:
#         print("Correct")


# продолжение
# l = [4,3,1,6,0]
# def merge_sort(arr):
#     if len(arr) <=1:
#         return arr
#     mid = len(arr)//2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)
#
# def merge(left, right):
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#              result.append(right[j])
#              j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
#
# print(merge_sort(l))


# новый день
# AVL
# class BinaryNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# class BST:
#     def __init__(self):
#         self.root = None
#     def insert(self, value):
#         self.root = self._insert(value, self.root)
#     def _insert(self, value,node):
#         if not node:
#             return BinaryNode(value)
#         if node.data < value:
#             node.right = self._insert(value,node.right)
#         else:
#             node.left = self._insert(value,node.left)
#
# bst = BST()
# bst.insert(19)
# bst.insert(26)
# print(bst.root.right.data)





