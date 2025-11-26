user=input("Input: ")
for char in user:
    if char.lower() in {"a","e","i","o","u"}:
        user=user.replace(char,"")

print("Output :",user)
