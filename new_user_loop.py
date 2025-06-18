# This version of the script is more practical for muliple user creation neatly loaded from attached input_users.csv

import csv
from new_user_hardcoded import load_env_variables, create_user_payload, make_post_request

def load_data_from_csv(file_path):
    '''loads users from CSV and return a list of dictionaries'''
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            users = []
            for row in reader:
                if len(row) != 4:
                    print(f"Skipping invalid row: {row}")
                    continue
                
                name, given_name, family_name, email_address = row
                full_name = f"{given_name} {family_name}"
                user_tuple = (name, full_name, given_name, family_name, email_address)
                users.append(user_tuple)
    
        return users
    
    except Exception as e:
        print(f"Error loading the CSV: {e}")
        return []

def main():
    api_url, username, password = load_env_variables()
    users = load_data_from_csv("input_users.csv")
    for name, full_name, given_name, family_name, email_address in users:
        user_payload = create_user_payload(name, full_name, given_name, family_name, email_address)
        make_post_request(user_payload, api_url, username, password)

if __name__ == "__main__":
    main()
