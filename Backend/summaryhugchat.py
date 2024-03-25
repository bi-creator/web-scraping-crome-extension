from hugchat import hugchat
from hugchat.login import Login
import json
import tiktoken
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
# Log in to huggingface and grant authorization to huggingchat
sign = Login('manjithreddy096@gmail.com', 'sx#jgcUhCHpq8Sp')
cookies = sign.login()

# Save cookies to the local directory
cookie_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)


chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

def summarizetext(text):
    try:
        print(len(encoding.encode(text)),'topic')
        query_result = chatbot.query(f'this text is extracted from a html page eleminate script text and other non importent text and summarise it into 4-5 paragraphs {text}')
        return(query_result) # or query_result.text or query_result["text"]
    except Exception as e:
        print(e)
        return "Something Went Wrong"


def topicextraction(titles):
    extractedtopics=chatbot.query(f'given is a list of titles, if any title seems related to another, form a dictionary with keys as topics and values as a list of titles which relate to same topic, here is the list {titles} and only return the dictionary not a text describing it so that i can convert the output text to a dictionary variable in the next line')
    print(extractedtopics)
    return json.loads(extractedtopics.text.replace("\\"," "))



def combinedsummary(summaryes):
    combinedsummary=chatbot.query(f'given a list of summaryes, summarize all the summaryes provided in a the list- {summaryes}')
    return(combinedsummary)
