import csv
import datetime

# Define the input and output file names
input_file = 'resolution_raw.csv'
output_file = 'resolution_parsed.csv'

# Define a function to convert timestamp to yyyy-mm-dd format
def convert_timestamp(timestamp):
    try:
        timestamp_parts = timestamp.split()
        if len(timestamp_parts) > 0:
            date_obj = datetime.datetime.strptime(timestamp_parts[0], '%Y-%m-%d')
            return date_obj.strftime('%Y-%m-%d')
        else:
            return None
    except ValueError:
        return None  # Return None for timestamps that cannot be parsed

# Open the input CSV file and create an output CSV file
with open(input_file, 'r') as csv_in, open(output_file, 'w', newline='') as csv_out:
    reader = csv.DictReader(csv_in)
    fieldnames = reader.fieldnames

    # Create a writer for the output CSV file
    writer = csv.DictWriter(csv_out, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        # Convert 'start_at', 'end_at', and 'membership_end_at' columns to yyyy-mm-dd format
        row['created_at'] = convert_timestamp(row['created_at'])
        row['updated_at'] = convert_timestamp(row['updated_at'])
        row['started_at'] = convert_timestamp(row['started_at'])
        row['ended_at'] = convert_timestamp(row['ended_at'])

        # Write the modified row to the output CSV file
        writer.writerow(row)

print(f'Conversion complete. Output saved to {output_file}')
