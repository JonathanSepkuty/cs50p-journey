def convert(text):
    text=text.replace(":(","🙁")
    text=text.replace(":)","🙂")
    return text
def main():
    user=input(" type something using emoticons")
    print(convert(user))
main()

    






