# Welcome to a game of Hangman

Mockup

Link to Live Project

This hangman game is an online command-line implementation of the classic word-guessing game Hangman, which is traditionally played with pen and paper. It is designed to test and train vocabulary and deductive skills in a playful way.

The word to guess is randomly generated from a list of animals for a fresh challenge each time. The number of wrong guesses is limited to the number of lines it takes to draw the hangman stick figure on the gallows. When the stick figure is complete, the stick figure is hanged and the game ends. If the word puzzle is solved before the stick figure hangs, the player wins and successfully completes game.


## Table of Contents

## Project and Site Owner Goals

Create a fun retro game using my acquired Pythons skills:
- Core Python Programming: effective use of Python's data types, variables, operators, and syntax.
- Problem-Solving: eesign a solution to break down the game logic into well-defined steps.
- Control Flow: implement conditional statements (if, elif, else) and loops (for, while) to manage the game's progression.
- Functions: create modular and reusable code blocks with functions encapsulating specific game mechanics. The goal is for each function to handle a single, well-defined task. This approach promotes cleaner code, easier maintainability and readability, and easier debugging during testing.
- User Interaction: design a command-line interface to gather user input and provide user feedback.

## User Experience

### Target Audience
- Word Game Enthusiasts: people who enjoy crossword puzzles, Scrabble, Wordle, or any game that involves vocabulary and wordplay.
- Language Learners: people looking for a fun way to practice their English vocabulary skills.
- Challenge Hunters: people enjoy a challenge and seek to improve their logical thinking and sharpen their deductive skills.
Casual Gamers: people looking for a simple, quick, and engaging game to play during short breaks or to pass the time avoiding boredom.
- Nostalgia Seekers: people who fondly remember playing Hangman with pen and paper and want to recapture that experience.

### First Time Visitors Goals

As a firs time user, I can
- play a familiar game online without having to download an app.
- understand the gameplay through simple instructions and clear feedback without having to learn complicated rules.
- get instant feedback and a sense of progress without complex strategies or lengthy gameplay.
- enjoy a game without needing a partner or scheduling a game session.

### Returning Visitors Goals

As a returning visitor, I want to:
- analyze my performance and spot areas for improvement.
- enjoy playing a game without needing a refresher on the rules.
- experience a fresh challenge each time thanks to the unpredictable nature of the computer's word choices.

### Frequent Visitors Goals
As a frequent visitor, I want to:
- enjoy a familiar game with a quick and engaging format for a mental break.
- see how fast I can improve my learning curve and sharpen my deductive and logical thinking skills.


## Design

The flowchart depicts the flow of the game logic:

![flowchart](/documentation/flowchart.png)

### Colors

Minimalistic color was added to the command-line interface with ANSI Escape Codes.

The bold green line on a black background was added to emphasise the user feedback to the the user's guess and the final game results message, while keeping the overall nostalgic retro atmosphere of such a command-line interface game. 

## Features

## Technology Used

### Languages Used

- Python
- HTML5
- JavaScript

### Frameworks, Libraries and Programs Used

- [GitHub](https://github.com/g-omarsdottir/hangman) to store code files.
- [Git](https://git-scm.com/) for version control.
- [Gitpod](https://www.gitpod.io/) as a Cloud Development Environment (CDE).
- [Heroku](https://www.heroku.com/) for deploying the project.
- [Code Institute template](https://github.com/Code-Institute-Org/p3-template) for Gitpod and this README.
- [Python Linter Validator](https://pep8ci.herokuapp.com/) according to the PEP 8 style guide for validating the Python code.
- [Draw.io](https://app.diagrams.net/) to create the flowchart of game logic for the project design.

## Testing

### Validator Testing

The Python code passed through the Python Linter Validator provided by the Code Institute without errors:

![validator-results](/documentation/validator-results.png)

### Manual Testing

### Testing User Stories

## Bugs

### Known Bugs

### Resolved Bugs

## Deployment and Local Development

### Deployment

### Local Development

## Credits

### Content

- [Chris Horton](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c) for the hangman image and the words to guess.
- [Stack Overflow](https://stackoverflow.com/questions/50504500/deprecationwarning-invalid-escape-sequence-what-to-use-instead-of-d) for declaration of a raw string for the hangman drawing. Adding an escape character "\" for each problem makes the the drawing, which is is created with characters, less readable.

### Acknowledgements