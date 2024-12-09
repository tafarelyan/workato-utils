import pandas as pd

def main(input):
    excel_file_url = input['excel_file_url']
    sheet_name = input.get('sheet_name', 0)
    
    df = pd.read_excel(excel_file_url, sheet_name=sheet_name, dtype=str)
    df.fillna('', inplace=True)
    
    return {
        'data': df.to_dict(orient='records')
    }
