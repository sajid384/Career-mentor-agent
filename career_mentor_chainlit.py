import google.generativeai as genai
import chainlit as cl

genai.configure(api_key="AIzaSyB8cvXddzU0gNdfM0DWsV-bFc3BzVB0V_Y")

class OpenAIWrapper:
    @staticmethod
    def chat(model, prompt):
        response = genai.GenerativeModel(model).generate_content(prompt)
        return response.text

@cl.on_message
async def main(message: cl.Message):

    field = message.content
    prompt = f"""
    Suggest best career paths in {field}.
    Then list key skills required for that field.
    Finally, give 3 real-world job roles in {field}.
    """
    response = OpenAIWrapper.chat("gemini-1.5-flash", prompt)
    await cl.Message(content=response).send()