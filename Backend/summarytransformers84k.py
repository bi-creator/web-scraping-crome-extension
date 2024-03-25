from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")



def summarizetext(text):
    inputs = tokenizer(f"{text}", return_tensors="pt")
    outputs = model.generate(**inputs)
    print(tokenizer.batch_decode(outputs, skip_special_tokens=True)[0])
