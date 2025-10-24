import subprocess
import os
import shutil



def run_flask_migrations():
    
    
    commands = [
        ["flask", "db", "init"],
        ["flask", "db", "migrate", "-m", "Initial migration."],
        ["flask", "db", "upgrade"]
    ]
    
    if os.path.exists("./migrations"):
        shutil.rmtree("./migrations")

    for cmd in commands:
        print(f"Executing: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(result.stderr)
            print("Error occurred. Stopping.")
            break

