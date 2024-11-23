import os
import csv

def convert_spectra_to_csv(input_folder, output_file):
    # Open a CSV file to write the results
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(['Id', 'Wavelength', 'Intensity'])

        # Read each file in the input folder
        for filename in os.listdir(input_folder):
            if filename.endswith(".txt"):
                filepath = os.path.join(input_folder, filename)
                
                file_id = os.path.splitext(filename)[0]

                # Separate into variables
                with open(filepath, 'r') as file:

                    # Skip header
                    file.readline()

                    # Write to file
                    for line in file:
                        wavelength, intensity = line.split(',')
                        intensity = intensity.strip().strip('"') # Remove quotations that randomly appear
                        writer.writerow([file_id, wavelength.strip(), intensity])

    print(f"CSV file created at {output_file}")

# Use the function to process files in 'data/spectra'
convert_spectra_to_csv('spectra', 'combined_spectra_data.csv')