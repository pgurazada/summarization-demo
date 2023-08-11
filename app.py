import gradio as gr
from transformers import pipeline

summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")

def predict(prompt):
    summary = summarizer(prompt)[0]["summary_text"]
    return summary

textbox = gr.Textbox(placeholder="Enter text to summarize", lines=5)
iface = gr.Interface(fn=predict, inputs=textbox, outputs="text")

with gr.Blocks() as demo:
    iface.launch()

demo.launch()
