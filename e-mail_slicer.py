e_mail = input("Enter your e-mail id : \n")

index = e_mail.index("@")
username = e_mail[0:index]

domain = e_mail[index + 1:]

print(f"Your username is {username} and domain is {domain}")