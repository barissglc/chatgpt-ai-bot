import openai
import gradio as gr

openai.api_key = "API kodunuzu yazın"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Yapay Zeka Asistanı ile Sohbet Et")
outputs = gr.outputs.Textbox(label="Cevap")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Yapay Zeka Asistanı",
             description="Bana istediğini sorabilirsin. .",
             theme="compact").launch(share=True)