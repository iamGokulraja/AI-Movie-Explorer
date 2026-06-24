import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
import os

def answerPrompt(question,result):
    answer = f"""
        Question :{question}
        
        Database Result:{result}

        answer the question using the database result about 2-3 lines.
        Tell about the Result movie's plot line story or actors info or any addtionaly information
        IF you Explain about the story , stictly mentioned hero names correctly and story also correctly according to the movies
        Rules:
          1. do not response 'User Safety :Safe' 
          2.Just Generated the result movies one line plot or story
    """
    return answer

st.title("AI Movie Explorer")

engine = os.getenv("DATABASE_URL")
question = st.text_input("Ask Movie Question")

if st.button("Enter"):
  if question.strip():
    try:
      load_dotenv()
      apiKey = os.getenv("API_KEY")
      client = OpenAI(api_key= apiKey , base_url="https://openrouter.ai/api/v1")
      prompt = f"""
       Generate ONLY PosterSQL SQL.

       Rules:
       1. Always add spaces.
       2. Always use SELECT properly.
       3.Use Double quotes for columns.
       4.Return only Executable SQL
       5.Don't add any extra text with query return Pgadmin Query only example query:
      SELECT "Moviename","Hero_Rating" FROM "Dataset" ORDER BY "Hero_Rating" DESC LIMIT 5
      6.Gave me like example query only.
       7. Don't Generate like following: ```sql
          SELECT "MovieName","Genre","Rating","Director","Actor","PeopleVote"
          FROM "Dataset"
          ORDER BY "Hero_Rating", "movie_rating", "PeopleVote" DESC
          LIMIT 5;
          ```
       8. Gave me like these :
            SELECT "MovieName","Genre","Rating","Director","Actor","PeopleVote"
            FROM "Dataset"
            ORDER BY "Hero_Rating", "movie_rating", "PeopleVote" DESC
            LIMIT 5; 
         9.Don't Geneate User Safety
           safety
           Also DON'T Explain



         Table:
         "Dataset"

         Columns:
          MovieName
          Genre
          Rating
          Director
          Actor
          PeopleVote
          Year
          Hero_Rating
          movie_rating
          content_rating

        
        Question:
             {question}

           RETURN SQL Only.
          """
        
        
      response = (client.chat.completions.create(model="meta-llama/llama-3-8b-instruct" , 
        messages=[
         {
            "role":"user",
            "content":prompt
          }
        ]))


        
     #st.write(response)
      sql = (response.choices[0].message.content)
      sql=(sql.replace(" ``` sql","").replace(" ``` ","").strip())
        
      st.code(sql)

      result = pd.read_sql(sql , engine)
        
      st.dataframe(result)

      ansprompt = answerPrompt(question,result.to_string(index=False))
      try:
        ai_response = (client.chat.completions.create(model="openrouter/free" , 
        messages=[
         {
            "role":"user",
            "content":ansprompt
          }
        ]))
        st.write("AI Response")
        st.success(ai_response.choices[0].message.content)
      
      except Exception as e:
        st.error(str(e))
        
    except Exception as e:
      st.error(str(e))

  else:
    st.error("Please Enter a Question")