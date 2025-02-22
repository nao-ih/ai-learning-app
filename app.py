from flask import Flask, request, render_template
import openai
import os
import re

app = Flask(__name__)

# OpenAI APIキーを環境変数から取得
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_learning_plan(subject):
    """AIが学習プランを作成し、HTMLフォーマットで整形"""
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "あなたは優秀な学習コーチです。"},
            {"role": "user", "content": f"{subject}を学ぶための最適な学習プランを作成してください。"}
        ]
    )

    plan = response.choices[0].message.content

    # **改行とリスト化の処理**
    plan = re.sub(r'(\d+)\.\s', r'<br><strong>\1.</strong> ', plan)  # 番号リストを太字に
    plan = plan.replace("\n", "<br>")  # 改行をHTML用に変換

    return plan

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
