#!/usr/bin/env python3
import json
import math
from collections import Counter

def load_classmates(data_file="classmates.json"):
    """Load classmate data from JSON file.

    Args:
        data_file (str): JSON file path containing classmate data

    Returns:
        list: List of classmate dictionaries
    """
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading classmates: {e}")
        return []

def save_classmates(classmates, data_file="classmates.json"):
    """Save classmate data to JSON file.

    Args:
        classmates (list): List of classmate dictionaries
        data_file (str): Target JSON file path

    Returns:
        bool: Success status
    """
    try:
        with open(data_file, "w") as file:
            json.dump(classmates, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving classmates: {e}")
        return False

def filter_classmates(classmates, property_name, value, answer):
    """Filter classmates based on question response.

    Args:
        classmates (list): List of classmate dictionaries
        property_name (str): Property used in question
        value: Expected property value
        answer (bool): User's yes/no response

    Returns:
        list: Filtered classmate list
    """
    filtered = []
    for classmate in classmates:
        classmate_value = classmate.get(property_name)
        if classmate_value is None:
            filtered.append(classmate)
            continue

        if isinstance(classmate_value, list):
            has_value = (value in classmate_value)
        elif isinstance(classmate_value, str):
            has_value = (value == classmate_value)
        else:
            print(f"Unexpected property type: {type(classmate_value)} for property: {property_name}")
            has_value = False

        if (answer and has_value) or (not answer and not has_value):
            filtered.append(classmate)
    
    return filtered



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
