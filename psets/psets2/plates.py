def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2<=len(s)<=6:
        return False
    if s[0].isdigit():
        return False
    if s[1].isdigit():
        return False
    for char in s:
        if char in ["!","?",".",","," "]:
            return False
    first_digit_index=-1
    for i, char in enumerate(s):
        if char.isdigit():
            first_digit_index=i
            break
    if first_digit_index == -1:
        return True
    if s[first_digit_index]== "0":
        return False
    if not s[first_digit_index:].isdigit():
        return False

    return True
main()
