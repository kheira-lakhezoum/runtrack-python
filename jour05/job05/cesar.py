import string

message = "Jules César envahira l'Europe"
decalage = 3
alpha = string.ascii_letters

def code(x, y):

    conversion = str.maketrans(alpha, alpha[y:] + alpha[:y])
    message_code = x.translate(conversion)
    return message_code
    
print(f"Message original: {message}")
message_code = code(message, decalage)
print(f"Message codé: {message_code}")

