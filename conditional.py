# creating our first password checker

# defining variables

user_name="kayal"
password="k123"

# define inputs

input_user_name=input("whats your user name?")
input_password=input("whats your password?")


# conditions

if input_user_name == user_name and input_password == password:
    print(f"Login sucessfull {user_name}")
elif input_user_name != user_name and input_password == password:
    print("Invalid username")
elif input_user_name == user_name and input_password != password:
    print("Invalid password")
else:
    print("Sorry no match found")