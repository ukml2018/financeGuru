#https://gilberttanner.com/blog/deploying-your-streamlit-dashboard-with-heroku/ 
#https://www.youtube.com/watch?v=nJHrSvYxzjE  --- deploying on heroku
from phi.agent import Agent
from phi.model.groq import Groq
import streamlit as st
#python -m streamlit run app.py
#import os
#import markdown2
from phi.tools.yfinance import YFinanceTools
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
#import groq
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Finance Guru App")
st.header("Investment model")
input=st.text_input("Enter Your Question: ",key="input")
#submit=st.button("Tell me the total calories")
input_prompt=""" 
   Use table to display financial data.
   Use Finance data to calculate average price and Variance of the stock
   USE https://corporatefinanceinstitute.com/  to calculate the CAPM
   Use variances to find the co-variance
   Find the weights based on highest portfolio mean, which is measured based on portfolio variance and weights of the individual stock
   Consider different weight combinations to consider optimum weight mix for highest return
   Generate the portfolio frontier graph
   Give the data output for the inventory portfolio analysis in the following format:
   Weight of Stock 1  |  Weight od Stock 2 | Portfolio Mean | Portfolio variance 
   Give the Financial summary of the calculated portfolio analysis
   For Non financial analysis give the output in non tabular format without any financial calculation
   A low P/E ratio compared to the industry average or historical levels may indicate an undervalued stock. Price-to-Book (P/B) Ratio: If the P/B ratio is lower than 1, it suggests the stock is trading below its book value, potentially indicating undervaluation
   For stock price analysis provide other stock data from similar industry in tabular format
 """

if st.button("Get Detailed Notes"):
 with open('tmp/finance.md', 'w', encoding='utf-8') as f:
    #    f.write("Testing")
    web_agent = Agent (
    name="Web Agent",
    #model = Groq(id="llama-3.3-70b-versatile"),
    model = Groq(id="llama3-70b-8192"),
    #model = OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always inclue sources"],
    show_tool_calls=True,
    markdown=True
    )
    
    finance_agent=Agent(
    #model = Groq(id="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
    model = Groq(id="llama-3.3-70b-versatile"),
    #model = OpenAIChat(id="gpt-4o"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations= True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    #instructions=["Use table to display data."],
    instructions=input_prompt,
    #instructions=["Display data in non tabular format."],
    #structured_outputs=True
    #save_response_to_file="tmp/finance.md",    
    #debug_mode=True
    )
    agent_team = Agent(
    team=[web_agent,finance_agent],
    instructions=["Always include sources","Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
    save_response_to_file="tmp/finance.md"
    )
    #agent.print_response("Write the performance of Infosys stock")
    #agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA")
    agent_team.print_response(input)
    with open('tmp/finance.md', 'r') as file:
        markdown_content = file.read()
    if markdown_content:
    #if agent.print_response(input):
        #summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        #st.write(agent.print_response(input))
        st.write(markdown_content)

