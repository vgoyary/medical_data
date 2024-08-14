import json
import pandas as pd

data = []

with open('train.json') as f:
    for line in f:
        try:
            # Try to load each line as a JSON object
            data.append(json.loads(line))
        except json.JSONDecodeError:
            # Handle or log errors
            print("Error decoding JSON")

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('output.csv', index=False)
