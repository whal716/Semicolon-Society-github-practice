from fastapi import FastAPI

app = FastAPI()

# sample user info
@app.get("/user/status")
def get_status(user_id: str):

    return {
        "user_id": user_id,
        "is_paid": True,
        "has_bot_access": True
    }

# sample AI chat
@app.post("/chat")
def chat_with_ai(message: dict):

    user_input = message.get("text")
    return {"reply": f"Backend received input '{user_input}'，AI thinking..."}
