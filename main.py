from nicegui import ui
import pandas as pd
import math
import os

def split_excel(file_path, rows_per_file):
    df = pd.read_excel(file_path)
    num_blocks = math.ceil(len(df) / rows_per_file)
    output_dir = os.path.join(os.path.dirname(file_path), 'splits')
    os.makedirs(output_dir, exist_ok=True)
    for i in range(num_blocks):
        start_row = i * rows_per_file
        end_row = (i + 1) * rows_per_file
        split_df = df.iloc[start_row:end_row]
        split_df.to_excel(os.path.join(output_dir, f"split_file_{i+1}.xlsx"), index=False)
    return output_dir, num_blocks

uploaded_file = None

def handle_upload(e):
    global uploaded_file
    temp_path = os.path.join(os.getcwd(), e.name)
    with open(temp_path, 'wb') as f:
        f.write(e.content.read())
    uploaded_file = temp_path
        
def run_split(rows):
    if not uploaded_file:
        ui.notify('Por favor, envie um arquivo Excel primeiro.', color='negative')
        return
    try:
        output_dir, num_blocks = split_excel(uploaded_file, int(rows))
        ui.notify(f'{num_blocks} arquivos gerados em: {output_dir}', color='positive')
    except Exception as ex:
        ui.notify(f'Erro: {ex}', color='negative')

ui.label('Divisor de Excel')
ui.upload(on_upload=handle_upload, label='Selecione o arquivo Excel (.xlsx)')
rows_input = ui.number('Linhas por arquivo', value=500, min=1)
ui.button('Dividir', on_click=lambda: run_split(rows_input.value))

ui.run()