print("Welcome to the caeser cypher")
again = "yes"
while again == "yes":
    action = input("Type \'encode\' to encrypt or \'decode\' to decrypt.\n")
    message = input("Type your message:\n")
    shift = int(input("Type your shift number:\n"))
    post = ""
    if(action == "encode"):
        for i in message:
            post += chr(ord(i) + shift)
        print(f"Here's the encoded result: {post}")
    else:
        for i in message:
            post += chr(ord(i) - shift)
        print(f"Here's the decoded result: {post}")
    again = input("Type \'yes\' if you want to go again otherwise type \'no\'.\n")