ball = int(input("Imtihon ballini kiriting (0-100): "))

if 90 <= ball <= 100:
    print("A")
elif 80 <= ball <= 89:
    print("B")
elif 70 <= ball <= 79:
    print("C")
elif 60 <= ball <= 69:
    print("D")
elif 0 <= ball <= 59:
    print("F")
else:
    print("Notogri ball kiritildi")
