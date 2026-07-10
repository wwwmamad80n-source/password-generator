import random
import string
while True:
    all_char = string.ascii_letters + string.digits + string.punctuation
    user_input = input(
        "How many characters long should the password be? or q for quiet:")
    if user_input == "q":
        break
    else:
        length = int(user_input)
        password_list = random.choices(all_char, k=length)
        password = "".join(password_list)
        print(f"Your generated password:{password}")

print("I hope you are satisfied with the generated password.")
