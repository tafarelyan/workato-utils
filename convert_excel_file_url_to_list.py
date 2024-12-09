import pandas as pd

def convert_excel_file_url_to_list_of_dicts(excel_file_url, sheet_name=0):
    df = pd.read_excel(excel_file_url, sheet_name=sheet_name, dtype=str)
    df.fillna('', inplace=True)
    
    return {
        'data': df.to_dict(orient='records')
    }
