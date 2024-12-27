#https://gilberttanner.com/blog/deploying-your-streamlit-dashboard-with-heroku/ 
#https://www.youtube.com/watch?v=nJHrSvYxzjE  --- deploying on heroku
from phi.agent import Agent
from phi.model.groq import Groq
import streamlit as st
#python -m streamlit run <app name>
import os
import markdown2
from phi.tools.yfinance import YFinanceTools
#import groq
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Finance Guru App")
st.header("Investment model")
input=st.text_input("Enter Your Question: ",key="input")
#submit=st.button("Tell me the total calories")
#input_prompt=""" """

if st.button("Get Detailed Notes"):
    
    agent=Agent(
    #model = Groq(id="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations= True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use table to display data."],
    #instructions=["Display data in non tabular format."],
    structured_outputs=True,
    save_response_to_file="tmp/finance.md",
    #debug_mode=True
    )
    #agent.print_response("Write the performance of Infosys stock")
    #agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA")
    agent.print_response(input)
    with open('tmp/finance.md', 'r') as file:
        markdown_content = file.read()
    if markdown_content:
        #summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(markdown_content)

