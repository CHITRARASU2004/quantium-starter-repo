import pandas as pd
import glob

# Get all CSV files from data folder
files = glob.glob("data/*.csv")

all_data = []

for file in files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "Pink Morsels"]

    # Create sales column
    df["sales"] = df["quantity"] * df["price"]

    # Keep only required columns
    df = df[["sales", "date", "region"]]

    all_data.append(df)

# Combine all CSV files
final_df = pd.concat(all_data)

# Save output
final_df.to_csv("output.csv", index=False)

print("Processing complete. Output saved as output.csv")