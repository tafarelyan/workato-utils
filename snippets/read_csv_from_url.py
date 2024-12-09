import csv
from io import StringIO
import requests

def read_csv_from_url(url):
    response = requests.get(url)
    csv_content = StringIO(response.content.decode('utf-8')) 
    return [row for row in csv.DictReader(csv_content)]
