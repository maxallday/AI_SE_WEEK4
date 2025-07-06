from flask import Flask, render_template_string, request, redirect, url_for
# This code creates a simple Flask application with a login page.
app = Flask(__name__)  # creating a Flask application instance
#html login page template
login_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login-container {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        input[type="text"], input[type="password"] {
            width: 90%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        input[type="submit"] {
            background-color: #28a745;
            border-radius: 5px;
            font-size: 16px;
            color: white;
            border: none;
            onmouseclick:
            transition: background-color 0.3s ease;
            padding: 10px 15px;
            cursor: pointer;
        }
</style>       
</head>
<body>
  <div class="login-container">
    <h2>Login</h2>
    <form method="POST" action="/">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <input type="submit" value="Login">
        <p style="color:{{ color }}">{{ message }}</p>

    </form>
 </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    color = "black"
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]
        if user == "admin" and pwd == "1234":
            message = "Login successful!"
            color = "green"
        else:
            message = "Invalid credentials."
            color = "red"
    return render_template_string(login_html, message=message, color=color)

if __name__ == "__main__":
    app.run(debug=True)
