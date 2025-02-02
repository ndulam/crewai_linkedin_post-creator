from crewai import Task
from textwrap import dedent
from agents import linkedin_scraper_agent, web_researcher_agent, doppelganger_agent

# Define a task to scrape LinkedIn posts
scrape_linkedin_task = Task(
    description=dedent(
        "Scrape a LinkedIn profile to get some relevant posts"),  # Task description
    expected_output=dedent("A list of LinkedIn posts obtained from a LinkedIn profile"),  # Expected output
    agent=linkedin_scraper_agent,  # Agent responsible for the task
)

# Define a task to perform web research on Llama 2 and Llama 3 comparison
web_research_task = Task(
    description=dedent(
        "Get valuable and high quality web information about the comparison between Llama 2 and Llama 3"),  # Task description
    expected_output=dedent("Your task is to gather high quality information about the comparison"
                           " between Llama 2 and Llama 3"),  # Expected output
    agent=web_researcher_agent,  # Agent responsible for the task
)

# Define a task to create a LinkedIn post comparing Llama 2 and Llama 3
create_linkedin_post_task = Task(
    description=dedent(
        "Create a LinkedIn post comparing Llama 2 and Llama 3 following the writing-style "
        "expressed in the scraped LinkedIn posts."  # Task description
    ),
    expected_output=dedent("A high-quality and engaging LinkedIn post comparing Llama 2 and Llama 3."
                           " The LinkedIn post must follow"
                           " the same writing-style as the one expressed in the scraped LinkedIn posts"),  # Expected output
    agent=doppelganger_agent,  # Agent responsible for the task
)

# Set the context for the LinkedIn post creation task
create_linkedin_post_task.context = [scrape_linkedin_task, web_research_task]