prompt = "\nList things that need to be done "
prompt += "\nEnter 'done' when you are finished: "
list = []

while True:
    note = input(prompt)

    if note == "done":
        break
    else: 
        list.append(note)
print(list)