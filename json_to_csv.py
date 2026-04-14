import json
import csv

# Open JSON file
with open("Data.json", "r") as json_file:
    data = json.load(json_file)

# Open CSV file
with open("student.csv", "w", newline="") as csv_file:
    
# Create CSV writer
    writer = csv.writer(csv_file)
    
# Write header (keys from JSON)
    writer.writerow(data[0].keys())
    
# Write rows
    for item in data:
        writer.writerow(item.values())

print("File converted successfully!")