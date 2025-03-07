#title:larger than n
#author: michael stoll
#date: 3/6/2025
def compare_numbers():
    n = int(input('input n:'))
    number_list=[]
    for count in range(0, 8):
        number_list += [int(input('Enter number:'))]
    for number in number_list:
        if number > n:
            print(f'Number greater than {n}:', number)
compare_numbers()