from fastapi import FastAPI,Response, status
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime,timedelta
import pytz
from pydantic import BaseModel
from summaryhugchat import summarizetext,topicextraction,combinedsummary
from dbfun import insertsummaryandsite,inserttopic,getonlysites,getonlytopics
# from summarytransformers84k import summarizetext
# from summarytransformers import summarizetext

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)
class domData(BaseModel):
    domCOntent:str
    url:str
    title:str


class domDataalltabs(BaseModel):
    domCOntentalltabs:list
    urls:list
    titles:list



@app.post('/addDOMdata')
def addDOMdata(domData:domData):
    summary=summarizetext(domData.domCOntent)
    print(summary)
    topicid=inserttopic(domData.title,summary.text)
    insertsummaryandsite(domData.url,summary.text,domData.title,topicid)
    return summary.text



@app.post('/addDOMdataalltabs')
def addDOMdata(domData:domDataalltabs):
    # summary=summarizetext(domData.domCOntent)
    # print(summary)
    # insertsummaryandsite(domData.url,summary.text,domData.title)
    alldoc={}
    for title,url,domcontent in zip(domData.titles,domData.urls,domData.domCOntentalltabs):
        alldoc[title]={"url":url,"dom":domcontent}
    topics=topicextraction(domData.titles)
    print(topics)
    for key in topics:
        summaryes=[]
        for a in topics[key]:
            summary=summarizetext(alldoc[a]['dom'])
            print(summary)
            summaryes.append(summary.text)
            alldoc[a]['summ']=summary.text
        topicsummary=combinedsummary(summaryes)
        print(topicsummary)
        topicid=inserttopic(key,topicsummary.text)
        for a in topics[key]:
            insertsummaryandsite(alldoc[a]['url'],alldoc[a]['summ'],a,topicid)



    return 


@app.get('/getalltopics')
def getalltop():
    topics=getonlytopics()
    sites=getonlysites()
    return {'topics':topics,'sites':sites}