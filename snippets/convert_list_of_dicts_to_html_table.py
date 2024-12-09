def convert_list_of_dicts_to_html_table(headers, data):
    if headers:
        cells = [''.join([f'<th>{x}</th>' for x in headers])]
    else:
        cells = [''.join([f'<th>{x}</th>' for x in input['data'][0].keys()])]

    for row in data:
        cells.append(''.join([f'<td>{x}</td>' for x in row.values()]))

    table_rows = ''.join([f'<tr>{cell}</tr>' for cell in cells])
    
    return {
        'html_string': f'<div style="overflow-x: auto; white-space: nowrap;"><table border="1" style="width: 700px;"><table border="1">{table_rows}</table></div>'
    }
