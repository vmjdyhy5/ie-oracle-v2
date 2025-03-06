# Implementation Guide for Classmate Akinator

This guide provides hints and suggestions for implementing each function in the `akinator.py` file.

## Function Implementation Hints

### `load_classmates(data_file="classmates.json")`

This function should:
1. Check if the data file exists
2. If it exists, open it and load the JSON data
3. If it doesn't exist or there's an error, call `get_sample_data()` to get sample data
4. Return the loaded data as a list of dictionaries

### `save_classmates(classmates, data_file="classmates.json")`

This function should:
1. Open the data file in write mode
2. Write the classmates list as formatted JSON
3. Handle any potential errors with try/except

### `get_sample_data()`

This function should:
1. Return a list of dictionaries with sample classmate data
2. Include at least 5 classmates with different properties
3. Each classmate should have all the required properties (name, country, eye_color, gender, languages, name_length)

### `get_unique_values(classmates, property_name)`

This function should:
1. Create an empty set to store unique values
2. Loop through each classmate in the list
3. If the property is "languages", add each language to the set
4. For other properties, add the property value to the set
5. Convert the set to a list and return it

### `ask_question(remaining_classmates, asked_properties)`

This function should:
1. Define a list of properties and question templates
2. Filter out properties that have already been asked
3. If all properties have been asked, pick a random one
4. Otherwise, pick a random property that hasn't been asked
5. Get unique values for the chosen property
6. Pick a random value
7. Format and return the question, property name, and value

### `filter_classmates(classmates, property_name, value, answer)`

This function should:
1. Create a new list to store filtered classmates
2. Loop through each classmate in the list
3. If the property is "languages", check if the value is in the classmate's languages list
4. For other properties, check if the classmate's property value matches the given value
5. Add the classmate to the filtered list if the condition matches the answer (True/False)
6. Return the filtered list

### `get_yes_no_input(prompt)`

This function should:
1. Display the prompt with a "(y/n)" suffix
2. Get input from the user
3. Convert the input to lowercase and strip whitespace
4. Return True for "y" or "yes", False for "n" or "no"
5. If the input is invalid, ask again

### `add_new_classmate()`

This function should:
1. Prompt the user for each property (name, country, eye_color, gender)
2. For languages, keep asking until the user enters an empty string
3. Calculate name_length automatically from the name
4. Return a dictionary with all the properties

### `main()`

This function should:
1. Display a welcome message
2. Load the classmates data
3. Initialize variables (remaining_classmates, asked_properties, etc.)
4. Loop through asking questions and filtering classmates
5. Make a guess when only one classmate remains or after a maximum number of questions
6. If the guess is wrong, offer to add the new classmate
7. Ask if the user wants to play again
8. Save any new classmates to the data file

## Tips for Implementation

- Use error handling (try/except) for file operations
- Keep the code simple and focused on the task
- Test each function individually before integrating them
- Use meaningful variable names
- Add comments to explain complex logic
- Follow the docstring specifications for each function 
