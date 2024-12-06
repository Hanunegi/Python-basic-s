from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

n = random.randint(1, 100)
guesses = 0

# Enhanced HTML Template with Improved Styling for Hover Effect
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guess the Number Game</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #000000; /* Black background */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #FFFFFF; /* White text color */
        }
        .container {
            text-align: center;
            background-color: #1e1e1e; /* Dark grey background */
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
            width: 400px;
        }
        h1 {
            font-size: 2.5em; /* Larger heading font size */
            margin-bottom: 20px;
            color: #FFD700; /* Gold color for heading */
        }
        p {
            font-size: 2.4em; /* Larger paragraph font size */
            margin: 20px 0;
        }
        input[type="number"] {
            padding: 12px;
            width: 85%;
            margin-bottom: 20px;
            border: 2px solid #ccc;
            border-radius: 8px;
            font-size: 1.3em; /* Larger font size for input */
            background-color: #333;
            color: #FFFFFF;
        }
        button {
            padding: 15px 30px;
            background-color: #4CAF50; /* Initial green color */
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1.3em; /* Larger font size for button */
            cursor: pointer;
            transition: background-color 0.3s, transform 0.2s;
        }
        button:hover {
            background-color: #FF4500; /* New hover color: orange-red */
            transform: scale(1.1); /* Slight zoom effect on hover */
        }
        button:active {
            background-color: #FF6347; /* Color change on click: tomato */
            transform: scale(1.05); /* Slight reduction on click */
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Guess the Number Game</h1>
        <p>{{ message }}</p>
        <form method="post">
            <input type="number" id="guess" name="guess" min="1" max="100" placeholder="Enter your guess" required>
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def guess_number():
    global guesses, n
    message = ""
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            guesses += 1
            if guess > n:
                message = "Please enter a lower number."
            elif guess < n:
                message = "Please enter a higher number."
            else:
                message = f"Congratulations! You've guessed the number {n} correctly in {guesses} attempts!"
                n = random.randint(1, 100)
                guesses = 0
        except ValueError:
            message = "Invalid input. Please enter a number."
    else:
        message = "Guess a number between 1 and 100."

    return render_template_string(html_template, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
