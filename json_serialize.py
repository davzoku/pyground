import json

samplemsg ={
    "content1":1,
    "content2":
        {
        "trueornot1": False,
        "trueornot2": True,
        }
}



s1=json.dumps(samplemsg)
print(s1)
with open("serialized_msg.json", "w") as f:
    f.write(s1)

