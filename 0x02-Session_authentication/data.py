import json
import pandas as pd
import time
import os

# Fetch repositories data
data = pd.read_json("https://api.github.com/users/Jasiel-Stark8/repos")
df = pd.DataFrame(data)
Export = df.to_json(r'./new_data.json')
with open('./new_data.json') as f:
    repos = json.load(f)

url_list = ["https://api.codetabs.com/v1/loc?github=" + repos["full_name"][str(i)] for i in range(len(repos["full_name"]))]

def repo_data(count):
    data = pd.read_json(url_list[count])
    df = pd.DataFrame(data)
    
    # Check if directory exists and create it if it doesn't
    directory = 'data/repos'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    Export = df.to_json(directory + '/' + str(count) + '.json')

for i in range(len(repos["full_name"])):
    repo_data(i)
    time.sleep(10)  # Be careful with rate limits

# New function to calculate total Python lines
def calculate_python_lines():
    total_python_lines = 0
    for i in range(len(repos["full_name"])):
        file_path = 'data/repos/'+str(i)+'.json'
        if os.path.exists(file_path):
            with open(file_path) as f:
                repo_data = json.load(f)
                for lang_data in repo_data:
                    if "language" in lang_data and "linesOfCode" in lang_data and lang_data["language"].lower() == "python":
                        total_python_lines += lang_data["linesOfCode"]
    return total_python_lines

total_python_lines = calculate_python_lines()
print(f"Total Python lines of code: {total_python_lines}")