from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

from the_sidekick.models import EvaluatorOutput
from webscraperagent.tools import playwright_tools

load_dotenv(override=True)


worker_llm = ChatDeepSeek(
    model="deepseek-v4-flash",
    temperature=0.3,
    extra_body={
        "thinking": {
            "type": "disabled"
        }
    }
)
worker_llm_with_tools = worker_llm.bind_tools(playwright_tools)

evaluator_llm = ChatDeepSeek(
    model="deepseek-v4-flash",
    temperature=0.3,
    extra_body={
        "thinking": {
            "type": "disabled"
        }
    }
)

evaluator_llm_with_output = evaluator_llm.with_structured_output(EvaluatorOutput)
