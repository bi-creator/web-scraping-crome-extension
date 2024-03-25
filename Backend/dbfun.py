import psycopg2
import datetime
from psycopg2.extras import RealDictCursor
conn = psycopg2.connect(database = "webscraping", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "manjith",
                        port = 5432)




# def getallusers():
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM users;')
#     rows = cur.fetchall()
#     conn.commit()
#     conn.close()
#     for row in rows:
#         print(row)


def inserttopic(topicname,summary):
    sql = """INSERT INTO topic(topicname,topicsummary,timestamp)
             VALUES(%s,%s,%s) RETURNING id;""" 
    ct=datetime.datetime.now()
    try:
        with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (topicname,summary,ct))

                # commit the changes to the database
                data=cur.fetchone()
                conn.commit()
                return data[0]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    

    
def insertsummaryandsite(url,summary,title,topicid):
    sql = """INSERT INTO sites(site_url,site_summary,user_id,title,timestamp,topic_id)
             VALUES(%s,%s,%s,%s,%s,%s);"""
    ct=datetime.datetime.now()
    try:
        with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (url,summary,1,title,ct,topicid))

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    




# def getalltopics():
#     sql="""select tc.id,topicname,topicsummary,si.title as site_title,si.site_url,si.site_summary from public.topic tc
#         join public.sites si on tc.id = si.topic_id where si.user_id='1'"""
    
#     cur = conn.cursor(cursor_factory=RealDictCursor)
#     cur.execute(sql)
#     rows = cur.fetchall()
#     conn.commit()
#     conn.close()
#     return rows


def getonlytopics():
    sql="""select id,topicname,topicsummary from public.topic"""
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(sql)
    rows = cur.fetchall()
    return rows


def getonlysites():
    sql="""select id,topic_id,title as site_title,site_url,site_summary from public.sites"""
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(sql)
    rows = cur.fetchall()
    return rows
    
