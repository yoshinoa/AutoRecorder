
def get_information() -> (str, int, str):
    link = input("What's your zoom link?\n")
    print(f"Zoom link is {link}")
    while True:
        try:
            meeting_hour = int(input("What time does your meeting start? (0-23)\n"))
        except ValueError:
            meeting_hour = int(input("Incorrect value, input again.\n"))
        break
    print(f"Start time is {meeting_hour}")
    passcode = input("If there is a passcode enter it now.\n")
    if passcode != "":
        print(f"Passcode is {passcode}.")
    else:
        print(f"No passcode recorded.")
    return link, meeting_hour, passcode
