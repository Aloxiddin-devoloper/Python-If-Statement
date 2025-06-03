
raqam = input("Telefon raqamini kiriting (masalan: 90xxxxxxx): ")

kod = raqam[:2]

if kod in ["90", "91"]:
    operator = "bellayn"
elif kod in ["93", "94"]:
    operator = "usell"
elif kod in ["88", "97"]:
    operator = "mobiuz"
elif kod in ["95", "99"]:
    operator = "uzmobile"
else:
    operator = "Nomalum operator"

print(f"Operator: {operator}")


