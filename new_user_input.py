# This script uses the funcs defined in new_user_hardcoded.py and takes the new user info as console input

from new_user_hardcoded import load_env_variables, create_user_payload, make_post_request

def get_user_input():
    '''prompts user to input name, first_name, last_name, email of new user, returns tuple (name, full_name, given_name, family_name, email_address)'''
    name = input("Enter username: ").strip()
    given_name = input("Enter first name: ").strip()
    family_name = input("Enter last name: ").strip()
    while True:
        email_address = input("Enter email address: ")
        if "@" in email_address and "." in email_address:
            break
        print("Invalid email address. Please try again.")

    full_name = f"{given_name} {family_name}"

    return (name, full_name, given_name, family_name, email_address)
            
def main():
    api_url, username, password = load_env_variables()
    name, full_name, given_name, family_name, email_address = get_user_input()
    user_payload = create_user_payload(name, full_name, given_name, family_name, email_address)
    make_post_request(user_payload, api_url, username, password)

if __name__ == "__main__":
    main()