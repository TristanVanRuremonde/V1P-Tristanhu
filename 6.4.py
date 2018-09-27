def new_password(oldpassword, newpassword):
    if str(oldpassword) != str(newpassword) and len(oldpassword) > 5:
        print(True)
    else:
        print(False)

print(new_password("JAhallo", "grotehamer"))

