a = int(input("1-tomonni kiriting: "))
b = int(input("2-tomonni kiriting: "))
c = int(input("3-tomonni kiriting: "))

if a == b == c:
    print("teng tomonli uchburchak")
elif a == b or b == c or a == c:
    print("Teng yonli")
else:
    print("Turli tomonli")
