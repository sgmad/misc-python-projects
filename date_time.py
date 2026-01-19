import os
import random
import json
import time
from datetime import datetime
import pytz

def run_logic():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Error: config.json not found.")
        return False

    raw_forced_mode = os.getenv("FORCED_MODE", "").strip()
    if raw_forced_mode and raw_forced_mode != "none":
        mode_name = raw_forced_mode
    else:
        mode_name = config.get("active_mode", "standard")
    
    tz = pytz.timezone(config.get("timezone", "Asia/Manila"))
    now = datetime.now(tz)
    date_str = now.strftime('%Y-%m-%d')
    today_name = now.strftime('%A')

    if date_str in config.get("blackout_dates", []):
        print(f"Skipping: {date_str} is a holiday.")
        return False

    if mode_name not in config.get("modes", {}):
        print(f"Error: Invalid mode '{mode_name}'.")
        return False

    mode_settings = config["modes"][mode_name]
    day_settings = mode_settings["schedule"].get(today_name, mode_settings["schedule"]["Default"])
    
    if random.random() < day_settings["probability"]:
        num_commits = random.randint(day_settings["min"], day_settings["max"])
        
        if num_commits <= 0:
            return False

        messages = [
            "Update Library System GUI to include book search functionality",
            "Refactor Minimart item class to improve attribute encapsulation",
            "Implement MySQL database connection for Admission System records",
            "Add error handling for file input in the student portal script",
            "Update PyQt6 signal-slot logic for better button responsiveness",
            "Refine validation logic for university admission requirements",
            "Enhance data persistence for library inventory using JSON storage",
            "Update calculator GUI layout for improved user accessibility",
            "Implement recursive search algorithm for book category indexing",
            "Fix floating point precision error in Minimart total calculation",
            "Update laboratory assignment on file handling and data parsing",
            "Refactor student record management using list comprehensions",
            "Enhance GUI styling for the login window using QSS stylesheets",
            "Update object-oriented structure for the inventory management system",
            "Implement exception handling for database connectivity issues",
            "Update helper functions for string formatting in the report generator",
            "Refactor data structure for admission status tracking logic",
            "Add unit tests for the discount calculation logic",
            "Update documentation for the Python programming lab exercises",
            "Improve performance of the record filtering algorithm in GUI",
            "Implement password hashing for the local user authentication script",
            "Update logic for dynamic item pricing based on quantity",
            "Refactor legacy code for improved compliance with PEP 8 standards",
            "Add support for exporting student records to CSV format",
            "Update main window geometry and title settings in PyQt script"
        ]
        
        os.system('git config user.email "scmad@proton.me"')
        os.system('git config user.name "sgmad"')
        
        print(f"Mode: {mode_name} | Day: {today_name} | Executing {num_commits} commits...")
        
        for i in range(num_commits):
            current_time_obj = datetime.now(tz)
            current_iso = current_time_obj.isoformat()
            
            os.environ["GIT_AUTHOR_DATE"] = current_iso
            os.environ["GIT_COMMITTER_DATE"] = current_iso
            
            with open("activity.txt", "a") as f:
                f.write(f"Record {i+1}/{num_commits} at {current_iso} (PHT)\n")
            
            os.system("git add activity.txt")
            commit_msg = random.choice(messages)
            os.system(f'git commit -m "{commit_msg}"')
            
            if i < num_commits - 1:
                wait_time = random.randint(45, 240)
                print(f"Committing... Next step in {wait_time}s")
                time.sleep(wait_time)
                
        return True
    
    return False

if __name__ == "__main__":
    run_logic()
