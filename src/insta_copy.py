import os
import json
from typing import List, Dict

def load_user_data(data_type: str) -> List[Dict[str, str]]:
    if data_type == "followers":
        input_file: str = os.path.join("data", "connections", "followers_and_following", "followers.json")
        data_key = None
    elif data_type == "following":
        input_file: str = os.path.join("data", "connections", "followers_and_following", "following.json")
        data_key = "relationships_following"
    elif data_type == "pending_follow_requests":
        input_file: str = os.path.join("data", "connections", "followers_and_following", "pending_follow_requests.json")
        data_key = "relationships_follow_requests_sent"
    else:
        raise ValueError("data_type must be \"followers\", \"following\", or \"pending_follow_requests\".")

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            json_data = json.load(f)

        data = json_data[data_key] if data_key else json_data

        users: List[Dict[str, str]] = []
        for item in data:
            if "string_list_data" in item and item["string_list_data"]:
                user_info = item["string_list_data"][0]
                users.append({"username": user_info["value"], "href": user_info["href"]})

        return users

    except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
        print(f"error with {data_type}: {e}")
        return []

def write_csv_file(users: List[Dict[str, str]], filename: str) -> None:
    os.makedirs("output", exist_ok=True)
    output_file: str = os.path.join("output", filename)

    with open(output_file, "w", encoding="utf-8") as f:
        for i, user in enumerate(users, 1):
            f.write(f"{i},{user["username"]},{user["href"]}\n")

def process_user_data(data_type: str) -> int:
    users: List[Dict[str, str]] = load_user_data(data_type)
    write_csv_file(users, f"{data_type}.csv")
    return len(users)

def main() -> None:
    print(f"followers: {process_user_data("followers")}")
    print(f"following: {process_user_data("following")}")
    print(f"pending follow requests: {process_user_data("pending_follow_requests")}")

    followers_usernames: set[str] = {user["username"] for user in load_user_data("followers")}
    following_usernames: set[str] = {user["username"] for user in load_user_data("following")}

    not_following_back_usernames: set[str] = following_usernames - followers_usernames
    not_following_back_users: List[Dict[str, str]] = [user for user in load_user_data("following") if user["username"] in not_following_back_usernames]

    write_csv_file(not_following_back_users, "not_following_back.csv")

    print(f"not following back: {len(not_following_back_users)}")

if __name__ == "__main__":
    main()
