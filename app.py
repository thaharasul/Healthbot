from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":

        question = request.form["question"]

        prompt = f"""
You are an AI Healthcare Assistant.

Answer only general health-related questions.

Provide:
- General health guidance
- Basic health tips
- Healthy lifestyle advice

Do not diagnose diseases with certainty.

If the user mentions severe symptoms, advise consulting a healthcare professional.

Question:
{question}
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "tinyllama",
                "prompt": prompt,
                "stream": False
            }
        )

        answer = response.json()["response"]

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=True)