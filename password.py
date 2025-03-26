import hashlib

password = input("Введіть пароль: ")
confirm_password = input("Підтвердіть пароль: ")

if password == confirm_password:
    hash_object = hashlib.sha256(password.encode('utf-8'))
    hashed_password = hash_object.hexdigest()
    print("Пароль успішно підтверджено та захешовано:")
    print(hashed_password)
else:
    print("Паролі не співпадають. Спробуйте ще раз.")
