password = input("Enter your password: ")

if len(password) >= 8:
    print("Password is long enough.")
else:
    print("Password is too short. It must be at least 8 characters.")
