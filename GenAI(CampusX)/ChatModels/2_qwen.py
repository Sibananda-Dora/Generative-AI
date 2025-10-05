# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="Qwen/Qwen3-0.6B")
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)