import csv 
import json 
import requests


url = 'http://0.0.0.0:8000/api/vessels/'

with open('./data-fs-exercise.csv', encoding='utf-8') as csvf:
    # open text file to write responses to 
    with open("file.txt", "a") as f: 
        csvReader = csv.DictReader(csvf)
        headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
        for row in csvReader:
            # remove spaces from keys
            clean_row = {row.replace(" ", ""): v for row, v in row.items()}
            
            # stringify dict
            vessel_str = json.dumps(clean_row)
        
            # get response from request and write to dict
            response = requests.post(url, json.loads(vessel_str))
            f.write(response.text)
            f.write("\n")


            # This solution clearly has a lot to be desired. To get rid of the data upload bottleneck, 
            # a future solution would include bulk csv imports for the backend. 