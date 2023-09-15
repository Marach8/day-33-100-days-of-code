import time, os

list = []
def menu():
  print()
  print('\033[0mEnter:')
  print()
  print()
  time.sleep(1)
  print('\033[1;33m"\033[32m1\033[1;33m" to view Todo List')
  print()
  time.sleep(1)
  print('"\033[32m2\033[1;33m" to edit Todo List')
  print()
  time.sleep(1)
  print('"\033[32m3\033[1;33m" to add a Todo to your List')
  time.sleep(1)
  print()
  a = input('\033[34m>> ')
  return a

def view():
  os.system('clear')
  global list
  if len(list) != 0:
    Printer(list)
    time.sleep(20)
  else:
    print('\033[31mYou have no items in your Todo List! Please, add items before you can view them!👿👿\033[0m')
    time.sleep(8)
  os.system('clear')

def edit():
  os.system('clear')
  global list
  if len(list) != 0:
    time.sleep(2)
    print()
    Printer(list)
    print()
    ask = input('\033[36mWhich item have you completed(and would want to remove from the list above?: ')
    if ask in list:
      print()
      time.sleep(2)
      list.remove(ask)
      print('\033[32mItem succesfully removed!😎')
    else:
      print('\033[31mThis item is not in your Todo List!')
  else:
    print('\033[31mYou have no items in your Todo List! Please, add items before you can edit them!👿👿\033[0m')
  time.sleep(10)
  os.system('clear')

def add():
  os.system('clear')
  time.sleep(2)
  global list
  while True:
    ask = input('Enter the item you want to add to your Todo List: ')
    list.append(ask)
    time.sleep(0.5)
    print()
    ask1 = input('Want to add again? y/n: ')
    print()
    if ask1 == 'y':
      continue
    else:
      break
  print()
  print('\033[32mItems added Succesfully!😊')
  time.sleep(4)
  os.system('clear')

def Printer(a):    
  b = '\033[4mMy Todo List\033[0m'
  print(f'\033[35{b:^70}.')
  print()
  for i in a:
    print(f'\033[32m{i} ', end='\033[0m|| ')
    time.sleep(2)
  print()


while True:
  b = menu()
  if b == '1':
    view()
  elif b == '2':
    edit()
  elif b == '3':
    add() 
  else:
    print()
    print('\033[31mPlease, choose 1, 2 or 3 from the menu!')
    time.sleep(4)
    os.system('clear')
    continue
  