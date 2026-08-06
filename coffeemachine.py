menu = {'espresso': 3.0,
     'capuccino':2.0,
        'latte':4.0 }
def show_menu(menu):
    print('Hello. Here is our menu:')
    for i,v in menu.items():
        print(f'{i}: ${v}')
def get_order(menu):
    order = input('What would you like: ').lower()
    if order in menu:
        print(f'Here is your {order}. That will be {menu[order]}' )
    return
show_menu(menu)
get_order(menu)