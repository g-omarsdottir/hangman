from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Hangman (Python CLI Game)</h1>
    <p>This project is a command-line implementation of the classic Hangman game written in Python.</p>

    <p>
    ▶ <a href="https://replit.com/">Play the game on Replit</a>
    </p>

    <p>Source code:</p>
    <p>
    <a href="https://github.com/g-omarsdottir/hangman">GitHub Repository</a>
    </p>

    <p>This deployment serves as a minimal web entry point for the project.</p>
    """
