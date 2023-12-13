import csv
import os

# Define the input and output file names
input_file = r'C:\VScode\URL\Vaishak.txt'
output_directory = r'C:\VScode\URL\chunks500\\'

# Create the output directory if it doesn't exist

os.makedirs(output_directory, exist_ok=True)

# Open the input .txt file for reading
with open(input_file, 'r') as file:
    data = file.readlines()

# Split the data into chunks of 2000 records each
chunk_size = 500
chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

# Define the header
header = "ID|url|Assign"

# Write each chunk to a separate .csv file
for i, chunk in enumerate(chunks):
    output_file = f'{output_directory}output_chunk_{i}.csv'

    # Open the output .csv file for writing
    with open(output_file, 'w', newline='') as csv_file:
        # Write the header row
        csv_file.write(header + '\n')

        # Write the data to the .csv file
        for line in chunk:
            csv_file.write(line.strip() + '\n')

print(f'Split the data into {len(chunks)} .csv files in the {output_directory} directory.')
