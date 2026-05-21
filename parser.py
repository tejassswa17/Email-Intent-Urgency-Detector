from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal


class InputFormat(BaseModel):
    problem: str = Field(
        description="""
        Customer email or message that needs to be analyzed
        for intent, urgency, and tone classification.
        """
    )

class TicketAnalysis(BaseModel):

    intent: Literal[
        "Request",
        "Complaint",
        "Inquiry",
        "Information",
        "Feedback",
        "Unclear"
    ] = Field(
        description="Main purpose of the message"
    )

    urgency: Literal[
        "Low",
        "Medium",
        "High",
        "Critical",
        "Unclear"
    ] = Field(
        description="Priority level of the message"
    )

    tone: Literal[
        "Polite",
        "Neutral",
        "Urgent",
        "Angry",
        "Professional",
        "Unclear"
    ] = Field(
        description="Overall emotional tone of the message"
    )


parser = PydanticOutputParser(
    pydantic_object=TicketAnalysis
)