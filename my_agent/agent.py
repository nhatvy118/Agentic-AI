import os
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm  

# GitHub Models is OpenAI-compatible. Use LiteLlm with provider=openai.
gh_model = LiteLlm(
    provider="azureml",
    model="openai/gpt-4.1-mini",              
    api_key=os.getenv("GITHUB_TOKEN"),       
    base_url="https://models.github.ai/inference",
)

root_agent = LlmAgent(
    model=gh_model,
    name="root_agent",
    instruction="You are a helpful assistant that answers questions.",
)