from crewai import Agent, Task, Crew
from crewai_tools import TXTSearchTool, DallETool

class SocialMediaManagerAgent:
    def __init__(self):
        self.tool = TXTSearchTool(txt="output.txt")
        self.agent = Agent(
            role="Linkedin social media manager",
            goal=f"Increase engagement and audience in linkedin. Generate image for the content also",
            backstory="You are a linkedin expert who knows how to post small opinion and informative content that is fit for linkedin to imporve engagement and audience.",
            verbose=True,
            allow_delegation=False,
            tools=[self.tool],
            response_template="""<|start_header_id|>assistant<|end_header_id|>
                        {{ .Response }}<|eot_id|>""",
        )

        self.task = Task(
            description="Understand the context and create an opinion post for LinkedIn.",
            tools=[self.tool],
            agent=self.agent,
            expected_output="A small opinion post about the content. The output must not be in markdown format but a plain text format.",
        )

    def kickoff(self):
        crew = Crew(agents=[self.agent], tasks=[self.task])
        output = crew.kickoff()
        return output


class ImageCreatorAgent:

    def __init__(self):
        self.dalle_tool = DallETool(
            model="dall-e-3",
            size="1024x1024",
            quality="standard",
            n=1,
            image_description="Penguine saying hello",
        )
        self.agent = Agent(
            role="You are a photo creator",
            goal=f"Create photo according to the prompt",
            backstory="You are a photo creator",
            verbose=True,
            allow_delegation=False,
            tools=[self.dalle_tool],
        )

        self.task = Task(
            description="Understand the context and create photo",
            tools=[self.dalle_tool],
            agent=self.agent,
            expected_output="A photo url",
        )

    def kickoff(self):
        crew = Crew(agents=[self.agent], tasks=[self.task])
        output = crew.kickoff()
        return output
