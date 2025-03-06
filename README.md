# IE Oracle V2

This is a simple Akinator-style game that tries to guess which classmate you're thinking of by asking a series of questions about their properties.

## How It Works

1. The program asks you questions about a classmate you're thinking of.
2. Based on your answers, it narrows down the possibilities.
3. After a few questions, it tries to guess which classmate you're thinking of.
4. If it can't guess correctly, you can add the classmate to the database.

## Properties Used

The game uses the following properties to identify classmates:
- Country of origin
- Eye color
- Gender
- Languages spoken
- Number of letters in name

## How to Run

```
python akinator.py
```

## Requirements

- Python 3.6 or higher
- No external libraries required

## Data Storage

Classmate data is stored in a file called `classmates.json`. This file is created automatically if it doesn't exist.

## Adding New Classmates

You can add new classmates to the database:
1. When the program fails to guess correctly
2. When prompted at the end of a game

## Example

```
Welcome to the IE Oracle V2!
Think of a classmate, and I'll try to guess who it is.

Does your classmate have brown eyes? (y/n): y
Remaining possibilities: 3

Is your classmate from Egypt? (y/n): y
Remaining possibilities: 1

I think your classmate is Ahmed!
Was I correct? (y/n): y
Great! I guessed it correctly!

Would you like to play again? (y/n): n
Thanks for playing the IE Oracle V2! 
