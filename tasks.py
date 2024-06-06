from crewai import Task
from agents import tool,researcher,writer
# Research task
research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),
  expected_output='A comprehensive {paragraph} paragraphs long report on the latest {topic} trends.',
  tools=[tool],
  agent=researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A {paragraph} paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)