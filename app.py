from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/gpt-access")
def gpt_access():
    user_agent = request.headers.get("User-Agent", "")
    
    # 특정 봇 UA 확인 (선택적 조건)
    allowed = any(bot in user_agent.lower() for bot in ["python", "curl", "bot", "gpt", "openai"])
    
    if allowed:
        return jsonify({
            "message": "안녕 GPT, 접근이 허용되었어!",
            "user_agent": user_agent
        })
    else:
        return jsonify({
            "message": "이 경로는 봇 전용이야. 접근은 감지되었지만, UA 확인이 필요해.",
            "user_agent": user_agent
        }), 403

if __name__ == "__main__":
    app.run()
