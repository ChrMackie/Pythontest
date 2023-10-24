def print_options():
    print("Select an option:")
    print("1. Study")
    print("2. Walk dog")
    print("3. Watch TV")
    print("4. Eat lunch")
    print("5. Go Sleep")
    print("6. Exit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print_options()
    user_choice = get_user_choice()

    if user_choice == 6:
        print("Goodybye!!")
        exit()

    print(f"You selected Option {user_choice}")

if __name__ == "__main__":
    main()

