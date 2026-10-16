vorige_letter = 0

message = "Hello world!"

for x in message:
    if vorige_letter != x:
        vorige_letter = 0
        print(x)