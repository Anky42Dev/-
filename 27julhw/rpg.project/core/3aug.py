# def hello(name, greet = 'Hello'):
#     return f'{greet},{name}'
# print(hello('Zaki'))
# print(hello('Sarah','Bonjour'))
# def find_max(*numbers):
#     max_idx = numbers[0]
#     for number in numbers:
#         if number>max_idx:
#             max_idx = number
#     return max_idx
# print(find_max(1,4,3,6,5,7))
def describe_pet(name,type,*args, **extra_fields):
    description = f'name: {name}, type = {type},'
    for key,value in extra_fields.items():
        description += f', {key} : {value}'
    return description
print(describe_pet('Hatiko','Dog', 2008 , age = 12, color = 'beige'))

        

       