vorige_letter = ""

message = "Hello world!"

for x in message:
    if vorige_letter != x:
        vorige_letter = x
        print(x)