def analyze_input(user_input):
    if user_input.isdigit():
        number = int(user_input)
        if number == 0:
            return "You enter 0"
        elif number < 0:
            return f"You enter negative {'fractional' if '.' in user_input else 'integer'} number: {number}"
        else:
            return f"You enter positive {'fractional' if '.' in user_input else 'integer'} number: {number}"
    else:
        if '.' in user_input:
            try:
                number = float(user_input)
                if number == 0:
                    return "You enter 0"
                elif number < 0:
                    return f"You enter negative fractional number: {number}"
                else:
                    return f"You enter positivefractional number: {number}"
            except ValueError:
                return f"You entered the wrong number: {user_input}"
        else:
            return f"You have entered an incorrect number: {user_input}"

def main():
    while True:
        user_input = input("Enter a number or exit to finish: ").strip().lower()
        if user_input in ['вихід', 'exit', 'quit', 'e', 'q']:
            print("Bye!")
            break
        else:
            print(analyze_input(user_input))

if __name__ == "__main__":
    main()
