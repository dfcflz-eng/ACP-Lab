import json


class Message:

    def __init__(
        self,
        msg_type,
        sender,
        content
    ):

        self.data = {

            "type": msg_type,

            "protocol": "ACP/0.1",

            "from": sender,

            "content": content

        }


    def to_json(self):

        return json.dumps(
            self.data,
            indent=2
        )


if __name__ == "__main__":

    msg = Message(
        "HELLO",
        "agent_001",
        "Hello Agent"
    )


    print(
        msg.to_json()
    )
