# Split temp variable

def save_into_db(info):
    print("saved into databse")

if __name__ == "__main__":
  username_input = input('Please enter your username: ')
  save_into_db(username_input)
  birthday_input = int(input('Please enter your birth year: '))
  age = 2020 - birthday_input
  print("You are",age, "years old.")