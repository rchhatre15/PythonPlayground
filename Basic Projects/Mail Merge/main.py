with open("./Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

for name in names:
    with open("./Input/Letters/starting_letter.txt", mode="r") as file:
        lines = file.readlines()
    lines[0] = lines[0].replace("[name]", name.strip())

    with open(f"./Output/ReadyToSend/{name}", mode="w") as file:
        for line in lines:
            file.write(line)
