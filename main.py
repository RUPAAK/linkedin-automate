# from crewai_tools import ScrapeWebsiteTool
import os
from agents import SocialMediaManagerAgent, ImageCreatorAgent

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# scrape_tool = ScrapeWebsiteTool(
#     website_url="https://www.freecodecamp.org/news/how-cdns-improve-performance-in-front-end-projects",
# )
# text = scrape_tool.run()


# with open("output.txt", "w") as file:
#     file.write(text)

# # Instantiate the agents
# data_analyst_agent = SocialMediaManagerAgent()
# # content_creator_agent = ImageCreatorAgent()


# data_analyst_output = data_analyst_agent.kickoff()
# # content_creator_output = content_creator_agent.kickoff()

print("Data Analyst Output:")
# print(data_analyst_output)
