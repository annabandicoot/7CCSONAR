import csv
import os

directory_path = "/analysis"

csv_files = [f for f in os.listdir(directory_path) if f.endswith(".csv") and f.startswith("ip_results_")]

output_file = "merged_results_of_ips_geo.csv"
file_count = 0
with open(output_file, "w", newline='') as out_file:
    csv_writer = csv.writer(out_file)
    for csv_file in csv_files:
        with open(os.path.join(directory_path, csv_file), newline='') as in_file:
            csv_reader = csv.reader(in_file)
            if file_count == 0:  # Write the header row for the first file only
                csv_writer.writerow(next(csv_reader))
            for row in csv_reader:
                csv_writer.writerow(row)
        file_count += 1

print(f"Merged {file_count} files into {output_file}")
