# Welcome to a game of Hangman

![preview](/documentation/preview.png)

[View the Live Project Here](https://hangman-word-puzzle-78ef7f810338.herokuapp.com/)

This hangman game is an online command-line implementation of the classic word-guessing game Hangman, which is traditionally played with pen and paper. It is designed to test and train vocabulary and deductive skills in a playful way.

The word to guess is randomly generated from a list of animals for a fresh challenge each time. The number of wrong guesses is limited to the number of lines it takes to draw the hangman stick figure on the gallows. When the stick figure is complete, the stick figure is hanged and the game ends. If the word puzzle is solved before the stick figure hangs, the player wins and successfully completes game.


## Table of Contents

- [Project and Site Owner Goals](#project-and-site-owner-goals)
- [User Experience](#user-experience)
- [Design](#design)
- [Features](#features)
- [Technology Used](#technology-used)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment and Local Development](#deployment-and-local-development)
- [Credits](#credits)

## Project and Site Owner Goals

My goal with this Python Hangman game is to craft a nostalgic, engaging word-guessing game using my acquired Pythons skills:

- Logical Thinking: 
    - Design the flowchart for the code logic according to the gameplay.
- Core Python Programming: 
    - Effective use of Python's data types, variables, operators, and syntax.
- Control Flow: 
    - Implement conditional statements and loops to manage the game's progression.
- Functions: 
    - Create modular and reusable code blocks with functions encapsulating specific game mechanics and validation of user input. 
- Clean Code: 
    - Functions should at best handle a single, well-defined task easier maintainability readability, and easier debugging.
    - Encapsulation of code structure: grouping constants, variables, as well as general and game functions.
- User Interaction: 
    - Gather user input, provide user feedback, and give the user control over the game progression using a command-line interface.

## User Experience

### Target Audience

- **Word Game Enthusiasts:** People who enjoy crossword puzzles, Scrabble, Wordle, or any game that involves vocabulary and wordplay.
- **Language Learners:** People learning English as a foreign language and are looking for a fun way to practice their English vocabulary skills.
- **Challenge Hunters:** People enjoy a challenge and seek to improve their logical thinking and sharpen their deductive skills.
- **Casual Gamers:** People looking for a simple, quick, and engaging game to play during short breaks or to pass the time avoiding boredom.
- **Nostalgia Seekers:** People who fondly remember playing Hangman with pen and paper and want to recapture that experience, or people who enjoy playing retro computer games, similar to the interaction with the good old Commador 64.

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

### User Choices for Game Control

Throughout the game, the user is provided with choices, if and how to proceed with the game. 

### Informative User Feedback

The game provides clear and informative feedback to the user throughout the gameplay experience. 

For instance, if the user enters invalid input, the game will display a message explaining the error and provide instructions on how to enter valid input.

<details>
<summary>Click for image</summary>

![invalid user input](/documentation/invalid-input.png)
</details>

### Start Screen

The game opens with a welcoming message and display of a hangman's gallows as a reference to the game's name and theme.

The initial prompt asks if the user wants to play.

<details>
<summary>Click for image</summary>

![start screen](/documentation/start-screen.png)
</details>

- **No:** If the user chooses "no," the choice made is confirmed and playful goodbye message indicates that the user is welcome to play again at another time.

- **Return Option:** The user is presented with the choice to return to the game menu in case of an unintended input or a change of heart.

    <details>
    <summary>Click for image</summary>

    ![play-no](/documentation/play-no.png)
    </details>

- **Yes:** If the user chooses "yes," the choice made is confirmed and a choice is presented to read the game rules before moving forward.

    <details>
    <summary>Click for image</summary>

    ![play-yes](/documentation/play-yes.png)
    </details>

### Game Rules

- **Yes:** If the user chooses to read the rules, the game displays a clear set of guidelines on how to play the game. 

- **Personalized Experience:** The user is prompted to enter a username to proceed, adding a touch of personalization to the gameplay.

    <details>
    <summary>Click for image</summary>

    ![rules](/documentation/rules.png)
    </details>

- **No:** If the user chooses to skip the rules, the choice made is confirmed and the user is prompted to enter a username to proceed.

    <details>
    <summary>Click for image</summary>

    ![rules-no](/documentation/rules-no.png)
    </details>

### Game Start

Upon successful username entry, the game kicks off:

**Welcome Message:** The player is greeted with a personalized welcome message, setting the tone for an engaging experience.

**Hangman Drawing:** The empty gallows appear, creating a sense of anticipation. The Hangman drawing visualizes the user’s performance during the game. 

**Word Puzzle:** The word to guess is represented by dashes, indicating the length of the secret word.

**Game Status:** The player is informed of the remaining guesses and already guessed letters.

**Word Challenge:** A clear prompt invites the player to make a guess.

<details>
<summary>Click for image</summary>

![game-start](/documentation/game-start.png)
</details>

### Responsive Gameplay

Each guess triggers immediate and informative user feedback and updates the display of the game status accordingly.

**Informative User Feedback:** the guessed letter is displayed and whether the guess is correct or incorrect. 

**Visual Clarity:** A decorative colored line visually separates this feedback from the game status for improved user experience. This allows the user to concentrate on the word puzzle while making the feedback easy to spot.

<details>
<summary>Click for image</summary>

![visual-seperator](/documentation/visual-separator.png)
</details>

### Evolving Game State

**Hangman Drawing:** The stick figure on the gallows progresses if the guess is incorrect. 

**Guesses Left:** The number of guesses left updates if the guess is incorrect. 

If an already used letter is entered, the game state remains the same and the user is prompted to try again.

**Used Letters:** The list updates after each guess.

**Word Puzzle:** If the guess is correct, the word puzzle updates, revealing the letter in its proper place.

<details>
<summary>Click for image</summary>

![responsive-gameplay](/documentation/responsive-gameplay.png)
</details>

### Game Completion

The game ends when the user has successfully solved the word puzzle or if the user runs out of guesses.

#### Game Victory

When the user correctly guesses the entire word, the user wins and the game concludes with:

- **User Feedback:** A clear message congratulates the user on the victory.

- **Game Status:** The user can review the list of used letters and the number of guesses left. The drawing visualizes that the stick figure was not hanged on the gallows symbolizing the user’s success.

- **Word Puzzle:** The word, that the user correctly guessed, is displayed.

- **Rematch Option:** The user is offered the choice to play again for a shot at a different word.

    <details>
    <summary>Click for image</summary>

    ![user-won](/documentation/user-won.png)
    </details>

#### Game Over

When a user runs out of guesses, the user loses and the game concludes with:

- **User Feedback:** A clear message indicates the user has lost. 

    The completed Hangman drawing displays the hanged stick figure on the gallows, reinforcing this gloomy outcome.

- **Game Status:** The user can review the number of guesses left and the list of used letters.

- **Word Puzzle:** The word to guess is revealed allowing the user to analyze the performance.

- **Rematch Option:** The user is offered the choice to play again for a shot at a different word.

    <details>
    <summary>Click for image</summary>

    ![user-lost](/documentation/user-lost.png)
    </details>

### Play Again

At game conclusion, the user is presented with the option to play again.

- **Yes:** If the user chooses to play again, the game provides the following:

    - **Start Screen:** The user proceeds to the start screen and a message confirms the user's choice to restart the game.

    - The user is prompted for a choice to play the game.

        <details>
        <summary>Click for image</summary>

        ![again-yes](/documentation/again-yes.png)
        </details>

    - **Yes:** If the user chooses to play, the game resets, 
        - clearing previous guesses and the word puzzle, 
        - restoring the initial number of guesses, 
        - and providing the user with a fresh new word challenge.

- **No:** Exiting the Game. If the user chooses not to play again, the game provides the following:

    - **Friendly Farewell:** The choice not to play again is confirmed and a playful goodbye message indicates that the user is welcome to play again at another time.

    - **Return Option:** The user is presented with the choice to return to the game menu in case of an unintended input or a change of heart.

        <details>
        <summary>Click for image</summary>

        ![again-no](/documentation/again-no.png)
        </details>

### Features Left to Implement

- Add a decorative website to frame the command-line interface with a retro archive theme using HTML, CSS and Javascript.

Due to the tight time schedule, the emphasis in this project was on solely on putting my Python skills to test and achieve solid, clean Python code. 

## Technology Used

### Languages Used

- Python
- HTML5
- JavaScript
- Markdown for this README

### Frameworks, Libraries and Programs Used

- [GitHub](https://github.com/g-omarsdottir/hangman) to store code files.
- [Git](https://git-scm.com/) for version control.
- [Gitpod](https://www.gitpod.io/) as a Cloud Development Environment (CDE).
- [Heroku](https://www.heroku.com/) for deploying the project.
- [Code Institute template](https://github.com/Code-Institute-Org/p3-template) for Gitpod and this README.
- [Python Linter Validator](https://pep8ci.herokuapp.com/) according to the PEP 8 style guide for validating the Python code.
- [Diffchecker](https://www.diffchecker.com/) to compare versions for troubleshooting.
- [Draw.io](https://app.diagrams.net/) to create the flowchart of game logic for the project design.
- [Table Magic](https://stevecat.net/table-magic/) to create tables for this README.

## Testing

### Validator Testing

The Python code passed through the Python Linter Validator provided by the Code Institute without errors:

![validator-results](/documentation/validator-results.png)

### Manual Testing

Tests were performed on the deployed live project.

| Feature                             | Test case                                                             | Outcome                                                                      |
|-------------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------------|
| Game initiation                     | User chooses to play                                                  | Prompt to display rules                                                      |
| Game initiation                     | User chooses not to Play                                              | Exits game - Option return to menu                                           |
| Game initiation                     | Invalid user input (neither “y” nor “n”)                              | Error message with instructions - - Prompt repeats                           |
| Game initiation                     | User chooses not to play                                              | Exits game - Option return to menu                                           |
| Game initiation for returning users | User chose to play again                                              | Game state is reset – Word to guess is new                                   |
| Display rules                       | User chooses to read rules                                            | Rules displayed - Prompt to enter username                                   |
| Display rules                       | User chooses to skip rules                                            | Prompt to enter username                                                     |
| Display rules                       | Invalid user input (neither “y” nor “n”)                              | Error message with instructions - - Prompt repeats                           |
| Enter username                      | User enters valid username                                            | Game starts - Prompt to guess                                                |
| Enter username                      | Invalid user input (non-alphabetic - space - empty - characters < 10) | Error message with instructions - - Prompt repeats                           |
| Enter guess                         | Correct guess                                                         | User feedback - Game state updates - - Prompt repeats while guesses left > 0 |
| Enter guess                         | Incorrect guess                                                       | User Feedback - Game state updates - - Prompt repeats while guesses left > 0 |
| Enter guess                         | Incorrect guess - guesses left = 0                                    | Game completion                                                              |
| Enter guess                         | Invalid user input (non-alphabetic – space - empty)                   | Error message with instructions - - Prompt repeats                           |
| Game completion                     | User chooses to play again                                            | User feedback - Game initiation                                              |
| Game completion                     | User chooses to not to play again                                     | Game exits - Option return to menu                                           |
| Game Completion                     | Invalid user input (neither “y” nor “n”)                              | Error message with instructions - - Prompt repeats                           |
| Option return to menu               | User presses enter to return to menu                                  | Game initiation - Prompt to play                                             |

### Testing User Stories

## Bugs

### Known Bugs

There are no known bugs.

### Resolved Bugs

| Bug                   | Description                                                                                                                  | Solution Applied                                                     | Result |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|--------|
| Premature end of game | Incorrect comparison in win condition of correctly guessed letters with unique letters in word in cases of duplicate letters | Compare set of correctly guessed letters with set of letters in word | Solved |
| Enter invalid guess   | Only input text prompting for a guess displayed on terminal                                                                  | Add else statement to display game if input is invalid               | Solved |
| Enter invalid guess   | Returning the boolean value instead of a string                                                                              | Add while True loop to return guess only if input is valid           | Solved |

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

- [Chris Horton](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c) for the code used to create the hangman image and the list of words to guess.
- [Stack Overflow](https://stackoverflow.com/questions/50504500/deprecationwarning-invalid-escape-sequence-what-to-use-instead-of-d) for declaration of a raw string for the hangman drawing. Adding a backslash as an escape character " \ " for each issue makes the the drawing, which is is created with characters, less readable.
- [Ali Spittel](https://www.myhatchpad.com/insight/7-practical-tips-for-writing-clean-code/) for insights on how to write clean code.
- [The Code Institute walkthrough project Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/blob/master/05-deployment/01-deployment-part-1/run.py) for inspiration to structure functions to handle single tasks and control the flow of the game logic using a main function.
- [Kylie Ying](https://github.com/kying18/hangman/blob/master/hangman.py) for inspiration to update the word puzzle with correctly guessed letters using a list comprehension and display the updated word puzzle to the user using the method join.

### Acknowledgements

- My mentor, Mitko Bachvarov, for his guidance and valuable advice.
- My friend, Stephan Reich, for support in troubleshooting and guidance to achieve clean code.
- My fellow students at Code Institute, especially [Amir Shkolnik](https://github.com/AmirShkolnik) for support with styling the project with color, and Niclas Hugdahl, for support with troubleshooting.
- My Code Institute course facilitator [Kristyna Wach](https://github.com/Cushione) for guidance, untiring motivation and encouragement.
- The Slack community for motivation.
