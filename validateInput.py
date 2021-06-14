while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('\nPlease enter a number for your age.')

print(f'\nYour ages is {age}')

while True:
    print('\nSelect a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        print('\nPassword Saved')
        break
    print('\nPasswords can only have letters and numbers')

while True:
    print('\nPlease enter your password')
    password_login = input()
    
    if password_login == password:
        print('\nAccess granted')
        break
    print('\nPlease enter a valid password')
