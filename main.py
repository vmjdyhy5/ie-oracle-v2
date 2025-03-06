#!/usr/bin/env python3

import json
import math
from collections import Counter

def get_best_question(remaining_classmates, properties, last_attr_used=None):
    """Select optimal property for next question using information gain.

    Args:
        remaining_classmates (list): Current candidate classmates
        properties (set): Available properties to consider
        last_attr_used (str, optional): Previously used property

    Returns:
        tuple: (attribute, value, info_gain) or (None, None, 0) if no valid split
    """
    n = len(remaining_classmates)
    if n <= 1:
        return None, None, 0

    candidates = []  # Each candidate is a tuple (attribute, value, info_gain)

    for attr in properties:
        value_counts = {}
        for classmate in remaining_classmates:
            classmate_value = classmate.get(attr)
            if classmate_value:
                if isinstance(classmate_value, list):
                    for v in classmate_value:
                        value_counts[v] = value_counts.get(v, 0) + 1
                else:
                    value_counts[classmate_value] = value_counts.get(classmate_value, 0) + 1
            
        for value, yes_count in value_counts.items():
            no_count = n - yes_count
            if yes_count == 0 or no_count == 0:
                continue

            # Calculate entropy before and after the split
            entropy_before = math.log2(n)
            p_yes = yes_count / n
            p_no = no_count / n
            entropy_after = - (p_yes * math.log2(p_yes)) - (p_no * math.log2(p_no))
            info_gain = entropy_before - entropy_after

            candidates.append((attr, value, info_gain))

    if not candidates:
        return None, None, 0


    # Sort candidates by information gain (highest first)
    candidates.sort(key=lambda x: x[2], reverse=False)

    for attr, value, info_gain in candidates:
        if attr != last_attr_used:
            return attr, value, info_gain

    # If all candidates repeat last_attr_used, return the best one
    return candidates[0]

def ask_question(remaining_classmates, last_attr_used=None):
    """Generate next yes/no question based on remaining candidates.

    Args:
        remaining_classmates (list): Current candidate classmates
        last_attr_used (str, optional): Previously used property

    Returns:
        tuple: (question, attribute, value) or (None, None, None)
    """
    if not remaining_classmates:
        return None, None, None

    # Gather all properties (excluding 'name')
    properties = set()
    for classmate in remaining_classmates:
        properties.update(classmate.keys())
    properties.discard("name")

    attr, value = get_best_question(remaining_classmates, properties, last_attr_used)
    if not attr:
        return None, None, None

    # Format a question based on the attribute
    if attr == "country":
        question = f"Is your classmate from {value}?"
    elif attr == "eye_color":
        question = f"Does your classmate have {value} eyes?"
    elif attr == "languages_spoken":
        question = f"Does your classmate speak {value}?"
    elif attr == "name_length":
        question = f"Does your classmate's name have {value} letters?"
    else:
        question = f"Is your classmate's {attr} {value}?"
    return question, attr, value

  
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