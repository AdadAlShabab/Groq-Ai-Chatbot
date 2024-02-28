import gradio as gr
import os
from groq import Groq  # Ensure Groq library supports this usage
from dotenv import load_dotenv

load_dotenv()

os.getenv("GROQ_API_KEY")
def fetch_response(user_input):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "you are a helpful assistant. Take the input from the users and try to provide as detailed response as possible. Provide proper expamples to help the user. Try to mention references or provide citations to make it more detail oriented."},
            {"role": "user", "content": user_input},
        ],
        model="mixtral-8x7b-32768",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stop=None,
        stream=False
    )
    return chat_completion.choices[0].message.content

iface = gr.Interface(fn=fetch_response, inputs="text", outputs="text", title="Fastest AI Chatbot By Adad Al Shabab", description="Ask a question and get a response.")
iface.launch()