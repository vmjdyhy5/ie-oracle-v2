#!/usr/bin/env python3
"""
This part focuses on the core data handling functions:
- load_classmates: Loading classmate data from JSON
- save_classmates: Saving classmate data to JSON
- filter_classmates: Filtering classmates based on question responses
"""

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
