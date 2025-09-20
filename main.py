import pandas as pd
import math

# Load the Excel file
df = pd.read_excel(r"C:\GDrive\Documentos\Clientes\Caberj\Whatsapp-sender\20250919_votacaoCaberj\importacao.xlsx")

# Define the number of rows per split file
rows_per_file = 500

# Calculate the number of blocks (files)
num_blocks = math.ceil(len(df) / rows_per_file)

# Iterate and save each block to a new Excel file
for i in range(num_blocks):
    start_row = i * rows_per_file
    end_row = (i + 1) * rows_per_file
    split_df = df.iloc[start_row:end_row]
    split_df.to_excel(f"split_file_{i+1}.xlsx", index=False)