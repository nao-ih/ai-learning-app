from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# APIキーを環境変数から取得
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_learning_plan(subject):
    """指定された学習内容に基づいて、AIが学習プランを作成する"""
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "あなたは優秀な学習コーチです。"},
            {"role": "user", "content": f"{subject}を学ぶための最適な学習プランを作成してください。"}
        ]
    )
    return response.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        subject = request.form.get("subject")
        if subject:
            plan = generate_learning_plan(subject)
            return render_template("index.html", subject=subject, plan=plan)
    return render_template("index.html", subject=None, plan=None)

if __name__ == "__main__":
    app.run(debug=True)
