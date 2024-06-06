from crewai import Crew, Process
from agents import researcher,writer
from tasks import research_task,write_task
import streamlit as st

crew = Crew(
  agents=[researcher, writer],
  tasks=[research_task, write_task],
  process=Process.sequential,
)

st.title("Blog Generator")
st.text("Enter any Tech related topic for the blog")

topic = st.text_input("Enter topic")
paragraph = st.text_input("How many paragraphs should the blog contain?")


if topic and paragraph:
  result = crew.kickoff(inputs={'topic': topic,'paragraph':paragraph})
  st.write(result)