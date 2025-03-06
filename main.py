#!/usr/bin/env python3
"""
This part focuses on the question selection logic:
- get_best_question: Selecting the optimal property for the next question using information gain
"""

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
