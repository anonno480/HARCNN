import os
import csv

# Path to the folder containing your images
folder_path = r"C:\Users\USER\Desktop\Research For Everyone\Testing"

# Path to the directory where you want to save the CSV file
output_directory = r"C:\Users\USER\Desktop\Research For Everyone\CSVFILES"

# Ensure the output directory exists, if not create it
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Path to the CSV file you want to create
csv_file = os.path.join(output_directory, "Testing.csv")

# Activity label
# activity_label = "Lying"  # You can change this label based on your activity

# List to store data rows for CSV
data_rows = []

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust file extensions as needed
        # Extract just the filename without the full path
        image_name = os.path.splitext(filename)[0]
        # Add filename and activity to the data rows
        data_rows.append([image_name])#, activity_label])

# Write data to CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Image'])#, 'Activity'])
    # Write data rows
    writer.writerows(data_rows)

print("Dataset CSV file created successfully!")
