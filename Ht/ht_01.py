def analyze_input(user_input):
    number = user_input.replace(',', '.')
    if number.isdigit():
        number = int(number)
        return (f'You enter {'negative ' if number < 0 else 'positive '}'
                f'{'fractional' if '.' in user_input else 'integer'} number: {number}')
    elif '.' in user_input:
        if all(char.isdigit() or char in ['.', ','] for char in user_input):
            number = float(number)
            return (f'You enter {'negative' if number < 0 else 'positive'}'
                    f'{'fractional' if '.' in user_input else 'integer'} number: {number}')
    return f'You have entered an incorrect number: {user_input}'

def main():
    while True:
        user_input = input('Enter a number or exit to finish: ').strip().lower()
        if user_input in ['вихід', 'exit', 'quit', 'e', 'q']:
            print('Bye!')
            break
        else:
            print(analyze_input(user_input))

if __name__ == "__main__":
    main()
