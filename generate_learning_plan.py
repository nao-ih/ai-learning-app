import openai
import os

# APIキーを環境変数から取得
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_learning_plan(subject):
    """指定された学習内容に基づいて、AIが学習プランを作成する"""
    client = openai.OpenAI()  # 最新のAPIクライアントを使う
    response = client.chat.completions.create(
        model="gpt-4o",  # 🔥 gpt-4-turbo → gpt-4o に変更
        messages=[
            {"role": "system", "content": "あなたは優秀な学習コーチです。"},
            {"role": "user", "content": f"{subject}を学ぶための最適な学習プランを作成してください。"}
        ]
    )
    return response.choices[0].message.content

# ユーザー入力を受け取る
if __name__ == "__main__":
    subject = input("学びたい内容を入力してください: ")
    plan = generate_learning_plan(subject)
    print("\n🔹 学習プラン:\n")
    print(plan)
