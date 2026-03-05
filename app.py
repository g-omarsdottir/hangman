from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Hangman</title>
    <style>
    :root {
    color-scheme: light dark;
    }
    body {
        font-family: Arial, sans-serif;
        background: light-dark(#f5f7fa, #1e1e1e);
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }
    .card {
        background: light-dark(white, #2b2b2b);
        color: light-dark(#000, #eee);
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        max-width: 500px;
        text-align: center;
    }
    h1 {
        margin-top: 0;
    }
    a {
        display: inline-block;
        margin: 10px 0;
        text-decoration: none;
        color: white;
        background: #4CAF50;
        padding: 10px 16px;
        border-radius: 5px;
    }
    </style>
    </head>

    <body>
    <div class="card">
    <h1>Hangman (Python CLI Game)</h1>
    <p>This project is a command-line implementation of the classic Hangman game written in Python.</p>

    <p>
    <a href="https://hangman--gomarsdottir.replit.app">▶ Play the game on Replit</a>
    </p>

    <p>Source code:</p>
    <p>
    <a class="secondary" href="https://github.com/g-omarsdottir/hangman">GitHub Repository</a>
    </p>

    <p style="color:#666;font-size:14px;">This deployment serves as a minimal web entry point for the project.</p>
    </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=False)
