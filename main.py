# jordan molina's code?
is_running = True

def encode_and_store(password_str):
    password_list = []
    encoded_password_list = []
    encoded_password_str = ""
    for char in password_str[:]:
        password_list.append(int(char))
    for num in password_list[:]:
        num += 3
        encoded_password_list.append(int(num))

    for num in encoded_password_list[:]:
        encoded_password_str += str(num)

    print('Your password has been encoded and stored!\n')
    print(encoded_password_str)
    return encoded_password_str
#Quinn's code for decoder function
def decoder(value):
    passcode = ''
    for digit in value:
        decoded_digit = str((int(digit) - 3) % 10)
        passcode += decoded_digit
    return passcode

while is_running:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')

    print('Please enter an option: ',end='')
    option_selection = input()

    if option_selection == '1':
        print('Please enter your password to encode: ', end='')
        password_str = input()
        passcode = encode_and_store(password_str)

    elif option_selection == '2':
        print(f'The encoded password is {passcode}, and the original password is {decoder(passcode)}')
        pass

    elif option_selection == '3':
        is_running = False
