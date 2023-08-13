import gradio as gr
from transformers import pipeline

summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")

def predict(prompt):
    summary = summarizer(prompt)[0]["summary_text"]
    return summary

textbox = gr.Textbox(placeholder="Enter text to summarize", lines=6)
interface = gr.Interface(inputs=textbox, fn=predict, outputs="text",
                     title="Business Information Summarizer",
                     description="This web API presents an abstractive summary of the input text using a Large Language Model (LLM)",
                     allow_flagging="manual", flagging_options=["Useful", "Not Useful"])

with gr.Blocks() as demo:
    interface.launch()

demo.queue(concurrency_count=8)
demo.launch()
