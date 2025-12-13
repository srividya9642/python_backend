text = input("Enter a string: ")

result = ""

for ch in text:
    if 'a' <= ch <= 'z':         # lowercase → uppercase
        result += chr(ord(ch) - 32)
    elif 'A' <= ch <= 'Z':       # uppercase → lowercase
        result += chr(ord(ch) + 32)
    else:
        result += ch             # keep numbers/symbols as is

print("String after swapping case:", result)
