pip install liac-arff

import pandas as pd
import arff

def convert_arff_to_csv(arff_files, output_csv):
    # Initialize an empty DataFrame to store all data
    all_data = pd.DataFrame()
    
    for file in arff_files:
        # Load the ARFF file
        with open(file, 'r') as f:
            data = arff.load(f)
        
        # Convert to pandas DataFrame
        df = pd.DataFrame(data['data'], columns=[attr[0] for attr in data['attributes']])
        
        # Append to the all_data DataFrame
        all_data = pd.concat([all_data, df], ignore_index=True)
    
    # Save the combined DataFrame to CSV
    all_data.to_csv(output_csv, index=False)
    print(f"Data successfully saved to {output_csv}")

# List of ARFF files to be converted
arff_files = ["path/to/2017.arff", "path/to/2018.arff", "path/to/2019.arff", "path/to/2020.arff"]

# Output CSV file path
output_csv = "path/to/Visegrad_Group_Companies_Dataset.csv"

# Convert ARFF to CSV
convert_arff_to_csv(arff_files, output_csv)

