from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv(override=True)


llm = ChatDeepSeek(
    model="deepseek-v4-flash",
    temperature=0.3,
    extra_body={
        "thinking": {
            "type": "disabled"
        }
    }
)
