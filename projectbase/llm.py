from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv(override=True)


llm = ChatDeepSeek(
    model="deepseek-v4-flash",
    max_tokens=128,
    temperature=0.3,
    extra_body={
        "thinking": {
            "type": "disabled"
        }
    }
)
