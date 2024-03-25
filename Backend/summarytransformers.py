from transformers import pipeline
summarizer = pipeline("summarization",  model="philschmid/bart-large-cnn-samsum")


def summarizetext(ARTICAL):
    return(summarizer(f'this text is extracted from a html page eleminate script text and other non importent text and summarise it into 4-5 paragraphs, text={ARTICAL}',do_sample=False)[0]['summary_text'])
    

