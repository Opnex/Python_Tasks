def email_slicer(email):
    if '@' in email and '.' in email.split("@",)[1]:
        username, domain = email.split('@')
        return username, domain
    else:
        return None, None
    
detail = input("Enter your email: ")

username, domain = email_slicer(detail)


if username and domain:
    print(f"{username} {domain}")
else:
    print("Invalid Email")