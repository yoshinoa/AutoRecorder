
def get_information() -> (str, int, str):
    link = input("What's your zoom link?\n")
    print(f"\033[92mZoom link is\033[0m {link}")
    while True:
        try:
            meeting_hour = int(input("What time does your meeting start? (0-23)\n"))
        except ValueError:
            meeting_hour = int(input("Incorrect value, input again.\n"))
        break
    print(f"\033[92mStart time is {meeting_hour}\033[0m")
    passcode = input("If there is a passcode enter it now.\n")
    if passcode != "":
        print(f"\033[92mPasscode is {passcode}.\033[0m")
    else:
        print(f"\033[92mNo passcode recorded.\033[0m")
    return link, meeting_hour, passcode
