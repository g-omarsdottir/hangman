
# Words to guess in a tuple (immutable)
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
print(words)





def welcome():
    """
    Function that welcomes the user to the game and explains the basic rules.
    """
    print("Welcome! Testing")

    print(
    """
    Welcome to a game of Hangman!
        
    You will get a set of blanks representing the number of letters in a word.
    Guess the word by entering one letter at a time and press enter.
            
    If you guess correctly, your letter(s) will appear on the blank(s).
            
    With each incorrect guess, one element will be added to the stick figure
    on the gallows, so choose wisely. 
            
    After 6 incorrect guesses, the stick figure is complete and it’s game over.
            
    Let the games begin!
            
    """
    )


def get_username():
    """
    Function to prompt the user to enter a username.
    Passes the username input for validation to the validate_username function.
    """
    while True:
        username_input = (
            input("Choose your username: ").strip().upper()
        )
        if validate_username(username_input):
            return username_input


def validate_username(username_input):
    """
    Validate the username input to ensure it is between 1 and 10 characters.
    """
    if " " in username_input or not username_input.isalpha():
        print("Invalid username. Please use alphabetic characters and no spaces.")
        return False
    elif len(username_input) < 1 or len(username_input) > 10:
        print("Invalid username. Please use between 1 and 10 characters.")
        return False
    else:
        return username_input


def get_user_guess():
    """
    Function to prompt the user to guess a letter.
    Passes the letter for validation to the validate_guess function.
    """
    while True:
        user_guess = input("Guess a letter: ").strip().upper()
        if validate_guess(user_guess):
            return user_guess


def validate_guess(user_guess):
    """
    Function that validates user input to ensure it is a single letter.
    Returns the validated letter or False if input is invalid.
    """
    if " " in user_guess or not user_guess.isalpha():
        print(f"'{user_guess}' is not a letter, try again.")
        return False
    elif len(user_guess) != 1:
        print("Enter a single letter.")
        return False
    # Add validation for used letters
    else:
        print(f"Let's see if {user_guess} works...")
        return user_guess


def main():
    """
    Function to run all game functions
    """
    welcome()
    username = get_username()
    guess = get_user_guess()


main()