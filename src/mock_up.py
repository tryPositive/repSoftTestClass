import subprocess
import time


# 1
def read_data_from_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
        return data
    except FileNotFoundError as e:
        raise e


# 2
def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise e


# 3
def perform_action_based_on_time():
    current_time = time.time()
    if current_time < 10:
        return "Action A"
    else:
        return "Action B"
