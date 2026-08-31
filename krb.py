from flask import Flask, render_template_string
import webbrowser
from threading import Timer

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Thank You KRB ❤️</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #111827, #1e1b4b);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            width: 100%;
            max-width: 750px;
            text-align: center;
        }

        h1 {
            font-size: 45px;
            margin-bottom: 10px;
        }

        .subtitle {
            color: #cbd5e1;
            font-size: 18px;
            margin-bottom: 30px;
        }

        .card {
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 20px;
            padding: 25px;
            margin: 15px 0;
            backdrop-filter: blur(10px);
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
            background: rgba(255,255,255,0.13);
        }

        .card h2 {
            margin: 0 0 10px;
        }

        .card p {
            color: #dbeafe;
            font-size: 17px;
        }

        button {
            margin-top: 25px;
            padding: 14px 28px;
            border: none;
            border-radius: 30px;
            font-size: 17px;
            font-weight: bold;
            cursor: pointer;
            background: white;
            color: #111827;
        }

        button:hover {
            transform: scale(1.05);
        }

        #message {
            margin-top: 20px;
            font-size: 20px;
            display: none;
        }

        .heart {
            animation: beat 1s infinite;
            display: inline-block;
        }

        @keyframes beat {
            50% {
                transform: scale(1.25);
            }
        }
    </style>
</head>

<body>

<div class="container">

    <h1>
        <span class="heart">❤️</span>
        THANK YOU KRB
        <span class="heart">❤️</span>
    </h1>

    <div class="subtitle">
        A small thank-you page made with Python & Flask
    </div>

    <div class="card">
        <h2>🙏 Thank You!</h2>
        <p>
            Thank you KRB for your amazing content
            and for putting so much effort into your videos.
        </p>
    </div>

    <div class="card">
        <h2>🌟 Keep Inspiring</h2>
        <p>
            Your videos entertain, motivate and inspire us.
            Keep creating amazing content!
        </p>
    </div>

    <div class="card">
        <h2>🔥 Keep Growing</h2>
        <p>
            Wishing KRB more subscribers, more success
            and many more amazing videos.
        </p>
    </div>

    <div class="card">
        <h2>💖 From a Fan</h2>
        <p>
            This is just a small way of saying:
            THANK YOU KRB!
        </p>
    </div>

    <button onclick="showThanks()">
        💌 One More Thanks
    </button>

    <div id="message">
        🚀 Keep shining, KRB! ❤️
    </div>

</div>

<script>
function showThanks() {
    document.getElementById("message").style.display = "block";
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)


def open_browser():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(host="127.0.0.1", port=5000, debug=False)
