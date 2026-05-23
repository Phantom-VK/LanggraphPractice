from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    model="deepseek-v4-flash",
    temperature=0.3,
    extra_body={
        "thinking": {
            "type": "disabled"
        }
    }
)
