import sys

from decorator import input_error

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if not name in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return "Already have"

@input_error
def show_phone(args, contacts):
        name = args[0]
        if name in contacts:
            return contacts[name]
        return "Not found"

@input_error
def change_contact(args, contacts):
    name = args[0]
    if not name in contacts:
        return "Not found"
    else:
        name, phone = args
        contacts[name] = phone
        return "Contact change"

@input_error
def all_contact(contacts):
    if contacts:
        result = ""
        for k,v in contacts.items():
            result += f"{k} - {v}\n"
        return result.strip()
    else:
        return "Not found"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(all_contact(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
