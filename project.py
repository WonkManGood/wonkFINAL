import csv as c

# /// Validates you have cipher and returns it as a dictionary.
def open_cipher():
    try:
        cipher_open = open('./dictionary.csv', 'r')
        cipher = list(c.DictReader(cipher_open))
    except:
        raise(LookupError('Couldn\'t find cipher. Validate build with source and/or run program in build folder.'))
    
    return cipher

def main():
    clear()
    wonkCIPHER = open_cipher()


# /// Prompts user for usage of program and returns function's results.
    print('''
    │  wonkCIPHER: -- 0.1
    │  a simple visual cipher - inspired by randomart in recent ssh builds


    Encrypt String:    0
    Decrypt String:    1
    Generate Random:   2

    Print valid character: 9
    ''')
    
    choice = input("Choice (0-2): ")
    match choice:
        case '0':
            clear()
            print(encrypt(input("Enter string: ")))
        case '1':
            output = decrypt()
            clear()
            print(f'''
│
│   {output}
│

                ''')
        case '2':
            clear()
            print(random())
        case 'frog':
            clear()
            print('''
  @..@
 (----)     # /// :sunglasses:
( >__< )
^^ ~~ ^^
''')
        case '9':
            valid_characters = []
            for row in wonkCIPHER:
                valid_characters.append(row['input'])
            print(valid_characters)
        case _:
            main()


def encrypt(i):
    clear()
    i = str(i)
    if 0 < len(i) <= 25: pass
    else: raise ValueError("Length must be 1-25 characters.") # checks length
    
    # /// hardcoded cipher in this function for pytesting
    try:
        cipher_open = open('./dictionary.csv', 'r')
        cipher = list(c.DictReader(cipher_open))
    except:
        raise(LookupError('Couldn\'t find cipher. Validate build with source and/or run program in build folder.'))

    q = [] # placeholder for output
    for iterate in range(len(i)): # this loop took me like 2 hours to do for some reason, only to find out it was an issue with open_cipher :(
        for row in cipher:
            if i[iterate] == row['input']:
                q.append(row['output'])
    i = str('').join(q)

    output = []
    box_length = (14)
    output.append(f'┌' + ('─' * box_length) + '┐\n')
    if len(i) <= 10:
        box_length = (len(i) + 4)
        difference = (10 - len(i))
        output.append(f'│  '+ i + (difference * ' ') + '  │\n')
        for _ in range(4):
            output.append(f'│' + (' ' * (box_length + difference)) + '│\n')
        output.append(f'└' + ('─' * (box_length + difference) + '┘\n'))#                                  } there was probably a better way to do this, but my brain couldnt figure it without more packages
    elif 10 < len(i) <= 20:
        difference = (20 - len(i))
        output.append(f'│  ' + i[0:10] + '  │\n')
        output.append(f'│  ' + i[10:] + (difference * ' ') + '  │\n')
        for _ in range(3):
            output.append(f'│' + (' ' * (box_length)) + '│\n')
        output.append(f'└' + ('─' * box_length) + '┘\n')
    elif 20 < len(i) <= 30:
        difference = (30 - len(i))
        output.append(f'│  ' + i[0:10] + '  │\n')
        output.append(f'│  ' + i[10:20] + '  │\n')
        output.append(f'│  ' + i[20:] + (difference * ' ') + '  │\n')
        for _ in range(2):
            output.append(f'│' + (' ' * (box_length)) + '│\n')
        output.append(f'└' + ('─' * box_length) + '┘\n')
    elif 30 < len(i) <= 40:
        difference = (40 - len(i))
        output.append(f'│  ' + i[0:10] + '  │\n')
        output.append(f'│  ' + i[10:20] + '  │\n')
        output.append(f'│  ' + i[20:30] + '  │\n')
        output.append(f'│  ' + i[30:] + (difference * ' ') + '  │\n')
        for _ in range(1):
            output.append(f'│' + (' ' * (box_length)) + '│\n')
        output.append(f'└' + ('─' * box_length) + '┘\n')
    elif 40 < len(i) <= 50:
        difference = (50 - len(i))
        output.append(f'│  ' + i[0:10] + '  │\n')
        output.append(f'│  ' + i[10:20] + '  │\n')
        output.append(f'│  ' + i[20:30] + '  │\n')
        output.append(f'│  ' + i[30:40] + '  │\n')
        output.append(f'│  ' + i[40:] + (difference * ' ') + '  │\n')
        output.append(f'└' + ('─' * box_length) + '┘\n')
    output.append('   wonkCIPHER\n')

    return (''.join(output))

                

def decrypt():
    clear()
    lines = []

    # /// Prompts user for each line of their cipher.
    print('''
The following will ask you for the 5 lines
of your cipher. Please enter line by line. If
a line is empty, simply press enter.

          ''')
    for i in range(1, 6):
        line = input(f"Line {i}: ")
        lines.append(str(line))
    lines = ''.join(lines)

    temp = [] #      } i couldnt figure a better way to shift values back and forth.
    output = []

    # /// Decrpyts.
    cipher = open_cipher()
    for iter in range(len(lines)):
        temp.append(lines[iter])
        if len(temp) == 2:
            for row in cipher:
                if ''.join(temp) == row['output']: output.append(row['input'])
            temp = []
    if len(''.join(output)) != (len(lines) / 2): raise ValueError("Incorrect characters found. Re-enter cipher.")
    return(''.join(output))



def random():
    cipher = open_cipher()
    import random as r
    length = r.randint(1, 25)
    i = []
    for iter in range(length):
        pos = r.randint(1, length)
        i.append(cipher[pos]['output'])
    i = ''.join(i)
    
    output = []
    box_length = (14)
    output.append(f'┌' + ('─' * box_length) + '┐\n')
    if len(i) <= 10:
        box_length = (len(i) + 4)
        difference = (10 - len(i))
        output.append(f'│  '+ i + (difference * ' ') + '  │\n')
        for _ in range(4):
            output.append(f'│' + (' ' * (box_length + difference)) + '│\n')
        output.append(f'└' + ('─' * (box_length + difference) + '┘\n'))
    elif 10 < len(i) <= 20:
        difference = (20 - len(i))
        output.append(f'│  ' + i[0:10] + '  │\n')
        output.append(f'│  ' + i[10:] + (difference * ' ') + '  │\n')
        for _ in range(3):
            output.append(f'│' + (' ' * (box_length)) + '│\n')
        output.append(f'└' + ('─' * box_length) + '┘\n')
    elif 20 < len(i) <= 30:
        difference = (30 - len(i))
        output.append(f'│  ' + i[0:10] + '  │\n')
        output.append(f'│  ' + i[10:20] + '  │\n')
        output.append(f'│  ' + i[20:] + (difference * ' ') + '  │\n')
        for _ in range(2):
            output.append(f'│' + (' ' * (box_length)) + '│\n')
        output.append(f'└' + ('─' * box_length) + '┘\n')
    elif 30 < len(i) <= 40:
        difference = (40 - len(i))
        output.append(f'│  ' + i[0:10] + '  │\n')
        output.append(f'│  ' + i[10:20] + '  │\n')
        output.append(f'│  ' + i[20:30] + '  │\n')
        output.append(f'│  ' + i[30:] + (difference * ' ') + '  │\n')
        for _ in range(1):
            output.append(f'│' + (' ' * (box_length)) + '│\n')
        output.append(f'└' + ('─' * box_length) + '┘\n')
    elif 40 < len(i) <= 50:
        difference = (50 - len(i))
        output.append(f'│  ' + i[0:10] + '  │\n')
        output.append(f'│  ' + i[10:20] + '  │\n')
        output.append(f'│  ' + i[20:30] + '  │\n')
        output.append(f'│  ' + i[30:40] + '  │\n')
        output.append(f'│  ' + i[40:] + (difference * ' ') + '  │\n')
        output.append(f'└' + ('─' * box_length) + '┘\n')
    output.append('   wonkCIPHER\n')
    return(''.join(output))


# /// Used to keep terminal looking clean.
def clear():
    from os import system, name
    if name == 'nt': system('cls')
    else: system('clear')


if __name__ == "__main__":
    main()
