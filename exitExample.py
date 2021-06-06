import sys

while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()#FUnción para terminar el programa
    print('You typed ' + response + '.')