email = input("Email manzilini kiriting: ")
if "@" in email and "." in email.split("@")[-1] and " " not in email:
    print("Email manzili togri")
else:
    print("Email manzili notogri")
