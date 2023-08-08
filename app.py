from transformers import pipeline
import gradio as gr

model = pipeline("summarization")1

def predict(prompt): 2
    summary = model(prompt)[0]["summary_text"]
    return summary

with gr.Blocks() as demo: 3
    textbox = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
    gr.Interface(fn=predict, inputs=textbox, outputs="text")

demo.launch()
