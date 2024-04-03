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

The project was deployed using Heroku.

### Deployment

#### Deployment using Heroku

To deploy the repository:
- Log into Heroku and navigate to the dashboard.
- Navigate to the button “New” in the top right corner and select “Create New App” from the navigation dropdown menu.
- Enter a name for the app. The name of the app must be unique and cannot be identical to any other app deployed by other users on Heroku.
- Select your region, “United States” or “Europe”, from the navigation dropdown menu.
- Click on the button “Create App”.
- Navigate to “Settings” on the top navigation menu.
- In the section “Config Var”, click on the button "Reveal Config Vars".
- Click on “Add a new Config Var” and enter the following:
    - As “key”: PORT 
    - As “value”: 8000
- (In case of sensitive information in creds.json, add applicable code as Config Var as well. This is not the case for deployment of this project.)
- In the section “Buildpacks”, click on the button "Add Buildpacks".
- Select Python by clicking on the Python image and click “Save”.
- Again, click on the button "Add Buildpacks".
- Select node.js by clicking on the node.js image and click “Save”.
    - Make sure that the buildpacks are in this  order, with Python on top, and node.js underneath.
    - If not, click on the Buildpack and drag and drop it to change the order.
- Navigate to section “Deploy” on the top navigation menu.
- Select "GitHub" as the deployment method.
- Search for the repository to be deployed by using the search bar and click “Connect”.
- Select the repository branch to be deployed.
- Choose “Manual” or “Automatic” deployment.
    - Manual deployment must be manually re-deployed after pushing new changes to the repository.
- Click the button “View” to open the link to the [deployed project](https://hangman-word-puzzle-78ef7f810338.herokuapp.com/). 

### Local Development

#### Local Clone

To clone the repository:
- Log in to GitHub and navigate to the repository of [this project](https://github.com/g-omarsdottir/hangman) 
- Click on the green button "Code" to open the dropdown menu, select "Clone with HTTPS, SSH or GitHub CLI" and copy the link provided.
- Open "Terminal" (or "Git Bash") in your code editor.
- Change the current working directory to the location where you want the cloned directory to be made.
- Type "git clone" in the terminal and then paste the URL copied on GitHub in step 2, above.
- Press "Enter" and your local clone will be created.

#### Fork

To fork the repository:
- Log in to Github and navigate to the repository of [this project](https://github.com/g-omarsdottir/hangman).
- Click the button "Fork" in the top right corner to open dropdown menu and select "Create a new fork".

## Credits

### Content

- [Chris Horton](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c) for the hangman image and the words to guess.
- [Stack Overflow](https://stackoverflow.com/questions/50504500/deprecationwarning-invalid-escape-sequence-what-to-use-instead-of-d) for declaration of a raw string for the hangman drawing. Adding a backslash as an escape character " \ " for each issue makes the the drawing, which is is created with characters, less readable.

### Acknowledgements