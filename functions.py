
def get_information() -> (str, int, str):
    link = input("What's your zoom link?\n")
    print(f"Zoom link is {link}")
    while True:
        try:
            meeting_hour = int(input("What hour does your meeting start? (0-23)\n"))
        except ValueError:
            meeting_hour = int(input("Incorrect value, input again.\n"))
        break
    print(f"Start time is {meeting_hour}")
    while True:
        try:
            meeting_minute = int(input("What minute does your meeting start? (0-60)\n"))
        except ValueError:
            meeting_minute = int(input("Incorrect value, input again.\n"))
        break
    while True:
        try:
            meeting_length = int(input("How long is your meeting (minutes)\n")) * 60
        except ValueError:
            meeting_length = int(input("Incorrect value, input again.\n")) * 60
        break
    passcode = input("If there is a passcode enter it now.\n")
    passcode = input("If there is a passcode enter it now.\n")
    if passcode != "":
        print(f"Passcode is {passcode}.")
    else:
        print(f"No passcode recorded.")
    return link, meeting_hour, meeting_minute, meeting_length, passcode
