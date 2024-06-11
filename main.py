from datetime import datetime


def retrieve_food(name: str) -> None:
  try:
    with open(f'{name}_food.txt') as f:
      a = f.read()
      print(a)
  except FileNotFoundError:
    print('Oops! No file Found!')


def retrieve_exercise(name: str) -> None:
  try:
    with open(f'{name}_exercise.txt') as f:
      a = f.read()
      print(a)
  except FileNotFoundError:
    print('Oops! No file Found!')
  

def log_food(name: str) -> None:
  print('Which food you had?')
  info: str = input('> ')
  print()
  with open(f'{name}_food.txt', 'a') as f:
    f.write(f'{datetime.now()}: {info}\n')
  print('Successfully added this food:')
  print(f'{info}')


def log_exercise(name: str) -> None:
  print('Which exercise have you done?')
  info: str = input('> ')
  print()
  with open(f'{name}_exercise.txt', 'a') as f:
    f.write(f'{datetime.now()}: {info}\n')
  print('Successfully added this Exercise:')
  print(f'{info}')


if __name__ == '__main__': 
  print('Who is accessing the system?')
  print('1: Anuj')
  print('2: Rohan')
  print('3: Harry')
  
  while True:
    try:
      user_name: int = int(input('> '))
      if user_name in [1,2,3]:
        break
      else:
        raise ValueError
    except ValueError:
      print()
      print('Only select from 1, 2, or 3')
      continue
  
  print()
  print('Which action do you want to perform? ')
  print('1: Retrieve Food info')
  print('2: Retrieve Exercise info')
  print('3: Add Food')
  print('4: Add Exercise')
  
  while True:
    try:
      action: int = int(input('> '))
      if action in [1,2,3,4]:
        break
      else:
        raise ValueError
    except ValueError:
      print()
      print('Only select from 1, 2, 3, or 4')
      continue
  
  print()
  
  if user_name == 1:
    if action == 1:
      retrieve_food('Anuj')
    elif action == 2:
      retrieve_exercise('Anuj')
    elif action == 3:
      log_food('Anuj')
    elif action == 4:
      log_exercise('Anuj')
  
  elif user_name == 2:
    if action == 1:
      retrieve_food('Rohan')
    elif action == 2:
      retrieve_exercise('Rohan')
    elif action == 3:
      log_food('Rohan')
    elif action == 4:
      log_exercise('Rohan')
    
  elif user_name == 3:
    if action == 1:
      retrieve_food('Harry')
    elif action == 2:
      retrieve_exercise('Harry')
    elif action == 3:
      log_food('Harry')
    elif action == 4:
      log_exercise('Harry')
