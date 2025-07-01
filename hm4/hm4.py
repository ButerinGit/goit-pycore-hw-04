def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").lower().split()
        if not user_input:
            print("Invalid command.")
            continue
        command = user_input[0]
        args = user_input[1:]

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) < 2:
                print("Error: Provide name and phone.")
            else:
                contacts[args[0]] = args[1]
                print("Contact added.")
        elif command == "change":
            if len(args) < 2:
                print("Error: Provide name and new phone.")
            elif args[0] not in contacts:
                print("Error: Contact not found.")
            else:
                contacts[args[0]] = args[1]
                print("Contact updated.")
        elif command == "phone":
            if len(args) < 1:
                print("Error: Provide a name.")
            elif args[0] in contacts:
                print(contacts[args[0]])
            else:
                print("Error: Contact not found.")
        elif command == "all":
            if contacts:
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
            else:
                print("No contacts saved.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
