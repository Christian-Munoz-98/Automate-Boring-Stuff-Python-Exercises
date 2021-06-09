def separation(my_list):
    concatenate = ''

    for i in my_list[:len(my_list)-1]:
        concatenate += i + ',' + ' '

    concatenate += 'and ' + my_list[len(my_list)-1]
    return concatenate
    
def run():

    my_list = []
    
    for i in range(5):
        element = input("Add an element to this list----> ")
        if element == '':
            continue
        else:
            my_list.append(element)
    
    if len(my_list) == 0:
        print('Error! empty list!')
    else:
        print(separation(my_list))

if __name__ == '__main__':
    run()


