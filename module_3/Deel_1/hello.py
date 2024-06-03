def hello(numper):
    messages = ""
    for x in range(numper):
        messages = messages + f"Hello from function town {x+1}!\n"
    return messages

messages = hello(5)
print(messages)



