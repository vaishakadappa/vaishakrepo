import csv
import os

# Define the input and output file names
input_file = r'C:\URL\Vaishak.txt'
output_directory = r'C:\URL\chunks\\'

# Create the output directory if it doesn't exist

os.makedirs(output_directory, exist_ok=True)

# Open the input .txt file for reading
with open(input_file, 'r') as file:
    data = file.readlines()

# Split the data into chunks of 2000 records each
chunk_size = 2000
chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

#define the header 
header = ["ID", "url", "Assign"]

# Write each chunk to a separate .csv file
for i, chunk in enumerate(chunks):
    output_file = f'{output_directory}2000_chunks_{i}.csv'
    
    # Open the output .csv file for writing
    with open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the header row if it's the first chunk
        csv_writer.writerow(header)

        # Write the data to the .csv file
        for line in chunk:
            csv_writer.writerow(line.strip().split('|'))

print(f'Split the data into {len(chunks)} .csv files in the {output_directory} directory.')
