import pytz
from flask import Flask, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def time_calculator():
    ottawa_timezone = pytz.timezone('America/Toronto')
    now = datetime.now(ottawa_timezone)
    now_str = now.strftime("%I:%M:%S %p")

    future_time = None
    selected_minutes = None

    if request.method == 'POST':
        selected_minutes = int(request.form.get('minutes'))
        future_time = (now + timedelta(minutes=selected_minutes)).strftime("%I:%M:%S %p")

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
                    font-size: 30px;
                }}
                select {{
                    padding: 12px;
                    font-size: 20px;
                    border-radius: 6px;
                }}
                footer {{
                    text-align: center;
                    font-size: 9px;
                }}
            </style>
        </head>
        <body>
            <div style="max-width: 600px; margin: 0 auto;">
                <h2>Welcome to the Time Calculator Application</h2>
                <p>Have a good shift, okay!</p>
                <hr>
                <div style="background: #BBC863; padding: 20px; border-radius: 12px;">
                    <form method="POST">
                        <p>Current Time: <b id="current-time" style="font-size: 22px">{now_str}</b></p>
                        <label for="minutes">Choose the <b><i>wait time</i></b>:</label><br>
                        <select id="minutes" name="minutes" onchange="this.form.submit()">
                            {options}
                        </select>
                    </form>

                    <p style="margin-top:20px;">
                        {f"Wait time is <b>{future_time}</b>" if future_time else "Please select a wait time above."}
                    </p>
                </div>
            </div>

            <footer><br><p>Made by Ten <i>:P</i></p></footer>

            <script>
                function updateTime() {{
                    const now = new Date();
                    const options = {{
                        hour: '2-digit',
                        minute: '2-digit',
                        second: '2-digit',
                        hour12: true
                    }};
                    document.getElementById('current-time').textContent = now.toLocaleTimeString('en-US', options);
                    
                }}
                setInterval(updateTime, 1000); // Update every 1 second
                updateTime(); 
            </script>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
