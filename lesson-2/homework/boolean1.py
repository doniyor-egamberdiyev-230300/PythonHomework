username = input("Enter your username: ").strip()
pasword = input("Enter your password: ").strip()

if username and pasword:
    print(f"Login successfully!")
else:
    print("Username and password cannot be empty!")