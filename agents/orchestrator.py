from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

# Mock LLM setup for simulated safe banking environments
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

class AgentResponse(BaseModel):
    user_status: str = Field(description="Either 'Struggling' or 'Normal'")
    intervention_required: bool = Field(description="True if the bank needs to guide the user")
    action_type: str = Field(description="'Tooltip', 'Voice_Assist', or 'None'")
    guidance_text: str = Field(description="The localized, simplified instruction for the user")

def analyze_user_behavior(page_id, time_spent_seconds, user_action_history):
    """
    Simulates the Friction & Navigation Agents analyzing application telemetry data.
    """
    system_prompt = (
        "You are the SBI Co-Pilot Digital Adoption Engine. Analyze the user's application telemetry. "
        "If they spend too long on complex pages (like Insurance or Fixed Deposits) without moving forward, "
        "flag them as 'Struggling' and provide a simplified, patient walkthrough text in Hindi/English."
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "Page: {page_id}\nTime Spent: {time_spent_seconds}s\nHistory: {history}")
    ])

    structured_llm = llm.with_structured_output(AgentResponse)
    chain = prompt | structured_llm

    return chain.invoke({
        "page_id": page_id,
        "time_spent_seconds": time_spent_seconds,
        "history": user_action_history
    })
