from pydantic import BaseModel, Field


class EvaluatorOutput(BaseModel):
    feedback: str = Field(description="Feedback on the AI assistant's response")
    is_success_criteria_met: bool = Field(description="Whether the success criteria have been met")
    user_input_needed: bool = Field(description="True if more input is needed from the user, or clarifications, or the assistant is stuck")

