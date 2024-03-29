import snscrape.modules.twitter as snt
import pandas as pd
from pymongo import MongoClient
import json
import streamlit as st
import datetime as dt
from PIL import Image

st.set_page_config(page_title="Twitter Scrapping",page_icon=Image.open(r'C:\Users\SINDHIYA\Downloads\Scrap.jpg'))
st.title(":red[Welcome to our page:exclamation::exclamation::exclamation:]")

st.image("data:image/png;base64,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",width=600)

st.markdown(":blue[Lets Scrap tweets from Twitter :smile:!!!! Enter your search inputs below:]")



tag= st.text_input(":red[Enter the Keyword/Hashtag to scrap:]")

tweet_count=st.number_input(":red[Enter the count of tweets to scrap:]",step=1)

from_date=st.date_input(":red[Select From Date:date:]")
to_date=st.date_input(":red[Select To date:date:]")
tweets=[]
search_tweets= st.button("Click to Search_Tweets")

if search_tweets:
    st.write('Tweets related to your search inputs ')
    Scrap=snt.TwitterSearchScraper(("tag from_date to_date"))
    for tweet in Scrap.get_items():
        if len(tweets)==tweet_count:
            break
        else:
            req_data=[ tweet.date,tweet.id,tweet.url,tweet.rawContent,tweet.user.username,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.source,tweet.likeCount]

            tweets.append(req_data)
        
    df=pd.DataFrame(tweets,columns=["Date","ID","URL","Tweet Content","User","Reply Count","Retweet Count","Language","Source","Like Count"])

    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiD3skIiEahU2uhOuTOdroi6S_-7XaS7fv9w&usqp=CAU")

    st.write(df)
    
    df.to_csv(f"{tag}_Tweets.csv",index=False)
    

    df.reset_index(inplace=True)
    Data_dict =df.to_dict(orient="records")

    display= pd.read_csv(f"{tag}_Tweets.csv")
    

    client= MongoClient("localhost",27017)
    db=client.Twitter_Scrap
    

   
    Data_json= json.dumps(Data_dict,default=str)
    
    Upload= st.checkbox("Click to store the data in DB")

    if Upload:
        db.scrap.insert_many(Data_dict)
    

    data_format = display.to_csv(index=False).encode("utf-8")

    
    Download_1= st.download_button("Download json",data=df.to_json(),
                                file_name=f"{tag}_Tweets.json")
    if Download_1:

        st.success('Your file is sucessfully downloaded',icon="✅")


    Download=st.download_button("Download CSV",data=data_format,
                                file_name=f"{tag}_Tweets.csv",mime="text/csv")

    if Download:
        st.success('Your file is sucessfully downloaded',icon="✅")


        st.text("Thanks for using our page.Visit us again !!!")
        


        
st.markdown("**Was this page helpful?**")
col1,col2=st.columns(2)
with col1:
    st.button(":thumbsup:  Yes")
with col2:
    st.button(":thumbsdown:  No")
        




   

  
