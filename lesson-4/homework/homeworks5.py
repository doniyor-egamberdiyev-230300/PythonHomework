def check_password(password):
    # Parol uzunligini tekshirish
    if len(password) < 8:
        print("Password is too short.")
        return

    # Katta harf borligini tekshirish
    if not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter.")
        return

    # Agar hamma shartlar bajarilsa
    print("Password is strong.")


# Foydalanuvchidan parol olish
password = input("Enter your password: ")
check_password(password)
