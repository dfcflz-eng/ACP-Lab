# ACP Python SDK


Experimental Python implementation
for Agent Communication Protocol.


## Current Features


- Agent identity loading
- Message generation


## Example


```python

from message import Message


msg = Message(
"HELLO",
"agent_a",
"Hello"
)

print(msg.to_json())

