from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Hello! Welcome to the Flask App </h2>
    <p>Try these URLs:</p>
    <ul>
        <li>/uppercase?name=pavan</li>
        <li>/reverse?name=pavan</li>
        <li>/count?name=pavan</li>
        
    </ul>
    """

# 1️ Uppercase Function
@app.route("/uppercase")
def uppercase_name():
    name = request.args.get("name", "Guest")
    return f"<h1>{name.upper()}</h1>"

# 2️ Reverse the Name
@app.route("/reverse")
def reverse_name():
    name = request.args.get("name", "Guest")
    return f"<h1>{name[::-1]}</h1>"

# 3️ Count Characters
@app.route("/count")
def count_characters():
    name = request.args.get("name", "")
    return f"<h1>Character Count: {len(name)}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
