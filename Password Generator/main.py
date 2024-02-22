import random as rd

# definindo o gerador de senhas
def password_generator(size):
    letters = 'abcdefghijklmnopqrstuvxwyz'
    word = rd.choices(letters, k=size)
    new_word = ''
    
    # o método choices retorna uma lista com as letras
    # o laço for transforma as listas numa unica string
    for letter in word:
        new_word = new_word + letter
    
    return new_word


num = int(input('Enter the number of digits in the password: '))
num_password = int(input('Enter the number of passwords you want: '))

for i in range(0, num_password):
    password = password_generator(num)
    print('\nYour password is: ', password)
    print('\n','-' * 20)
