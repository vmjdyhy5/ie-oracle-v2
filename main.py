#!/usr/bin/env python3
"""
This part focuses on the user interaction functions:
- get_yes_no_input: Getting validated yes/no input from the user
- add_new_classmate: Collecting and structuring new classmate data
"""

import json

def get_yes_no_input(prompt):
    """Get validated yes/no input from user.

    Args:
        prompt (str): Question to display

    Returns:
        bool: True for yes, False for no
    """
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        else:
            print("Please enter y or n.")

def add_new_classmate():
    """Collect and structure new classmate data.

    Returns:
        dict: New classmate information
    """
    print("\nLet's add a new classmate!")
    name = input("Enter the classmate's name: ").strip()
    country = input("Enter the classmate's country: ").strip()
    eye_color = input("Enter the classmate's eye color: ").strip()
    gender = input("Enter the classmate's gender: ").strip()
    languages = input("Enter languages spoken (comma-separated): ").strip()
    languages_spoken = [lang.strip() for lang in languages.split(",") if lang.strip()]
    name_length = len(name)
    return {
        "name": name,
        "country": country,
        "eye_color": eye_color,
        "gender": gender,
        "languages_spoken": languages_spoken,
        "name_length": name_length
    }
