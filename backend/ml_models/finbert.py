from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="ProsusAI/finbert"
)

text = "Markets are crashing amid recession fears"

result = classifier(text)

print(result)