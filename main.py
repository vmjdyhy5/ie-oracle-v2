#!/usr/bin/env python3
"""
This part focuses on the main game loop:
- main: Running the IE Oracle V2 game loop
"""

import json

def main():
    """Run the IE Oracle V2 game loop.
    
    Handles game initialization, question-answer flow, and new classmate addition.
    """
    print("Welcome to the IE Oracle V2!")
    print("Think of a classmate, and I'll try to guess who it is.")

    classmates = load_classmates()
    if not classmates:
        print("No classmates found.")
        if get_yes_no_input("Would you like to add a classmate?"):
            new_classmate = add_new_classmate()
            if new_classmate:
                classmates.append(new_classmate)
                save_classmates(classmates)
                print("Classmate added!")
        return

    remaining_classmates = classmates.copy()
    last_attr_used = None

    while len(remaining_classmates) > 1:
        question, attr, value = ask_question(remaining_classmates, last_attr_used)
        if not question:
            break

        answer = get_yes_no_input(question)
        remaining_classmates = filter_classmates(remaining_classmates, attr, value, answer)
        last_attr_used = attr
        print(f"Remaining possibilities: {len(remaining_classmates)}")

        if len(remaining_classmates) == 1:
            print(f"\nI guess your classmate is {remaining_classmates[0]['name']}!")
            if get_yes_no_input("Am I correct?"):
                print("Great!")
            else:
                print("Oops! Let's add your classmate to the database.")
                new_classmate = add_new_classmate()
                if new_classmate:
                    classmates.append(new_classmate)
                    save_classmates(classmates)
        elif len(remaining_classmates) > 1:
            print("\nI'm not sure who it is. Here are some possibilities:")
            for i, classmate in enumerate(remaining_classmates, start=1):
                print(f"{i}. {classmate['name']}")
            if get_yes_no_input("Would you like to add your classmate to the database?"):
                new_classmate = add_new_classmate()
                if new_classmate:
                    classmates.append(new_classmate)
                    save_classmates(classmates)
        else:
            print("I couldn't find any matching classmate.")
            if get_yes_no_input("Would you like to add your classmate to the database?"):
                new_classmate = add_new_classmate()
                if new_classmate:
                    classmates.append(new_classmate)
                    save_classmates(classmates)

    if get_yes_no_input("Would you like to play again?"):
        main()
    else:
        print("Thanks for playing!")
    return

if __name__ == "__main__":
    main()
