import os
import json


def create_user_name_map(dataset_folder):
    user_name_map = {}

    # Iterate through files in the dataset folder
    for filename in os.listdir(dataset_folder):
        if filename.endswith(".jpg"):
            # Extract user ID from the filename
            # Assuming filenames are in the format "user_{ID}.jpg"
            user_id = filename.split("_")[1].split(".")[0]

            # Take the name of the person as the input
            person_name = input(f"Enter the name of the Person {user_id}: ")

            # Map user ID to person's name
            user_name_map[f"user_{user_id}"] = person_name

    return user_name_map


dataset_folder = "./dataset"
jsonFilePath = "./Users.json"
user_name_map = create_user_name_map(dataset_folder)
print(user_name_map)
with open(jsonFilePath, "w") as file:
    json.dump(user_name_map, file)
