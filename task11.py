oy = int(input("Oy raqamini kiriting (1-12): "))

if oy in [12, 1, 2]:
    print("Qish")
elif oy in [3, 4, 5]:
    print("Bahor")
elif oy in [6, 7, 8]:
    print("Yoz")
elif oy in [9, 10, 11]:
    print("Kuz")
else:
    print("Notogri oy raqami kiritildi")
