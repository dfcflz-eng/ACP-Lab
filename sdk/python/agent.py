import json


class Agent:

    def __init__(self, file):
        with open(file) as f:
            self.profile=json.load(f)


    def introduce(self):

        print(
            "Hello, I am",
            self.profile["name"]
        )

        print(
            "My skills:"
        )

        for skill in self.profile["capabilities"]:
            print(
                "-",
                skill["name"]
            )



if __name__=="__main__":

    agent=Agent(
        "../../schemas/agent.json"
    )

    agent.introduce()
