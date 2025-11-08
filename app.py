from flask import Flask, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def time_calculator():
    now = datetime.now()
    now_str = now.strftime("%H:%M:%S")
    future_time = None
    selected_minutes = None

    if request.method == 'POST':
        selected_minutes = int(request.form.get('minutes'))
        future_time = (now + timedelta(minutes=selected_minutes)).strftime("%H:%M:%S")

    options = ""
    for i in range(5, 61, 5):
        selected = "selected" if selected_minutes == i else ""
        options += f'<option value="{i}" {selected}>{i} minutes</option>\n'

    return f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Time Calculator</title>
            <style>
                body {{
                    color: #31694E;
                    background-color: #F0E491;
                    font-family: Arial;
                    padding: 20px;
                }}
                select {{
                    padding: 5px;
                    font-size: 16px;
                    border-radius: 6px;
                }}
            </style>
        </head>
        <body>
            <h2>Welcome to the Time Calculator Application</h2>
            <p>Hope this will improve your performance!</p>
            <hr>

            <form method="POST">
                <p>Current Time: <b>{now_str}</b></p>
                <label for="minutes">Choose the wait time:</label><br>
                <select id="minutes" name="minutes" onchange="this.form.submit()">
                    {options}
                </select>
            </form>

            <p style="margin-top:20px;">
                {f"Wait time gonna be: <b>{now_str} + {selected_minutes} minutes = {future_time}</b>" if future_time else "Please select a wait time above."}
            </p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
