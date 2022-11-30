import csv 
import json 
import requests


url = 'http://0.0.0.0:8000/api/vessels/'

with open('./data-fs-exercise.csv', encoding='utf-8') as csvf:
    # open text file to write responses to 
    with open("file.txt", "a") as f: 
        csvReader = csv.DictReader(csvf)
        headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
        all_rows = []
        for row in csvReader:
            # remove spaces from keys
            clean_row = {row.replace(" ", ""): v for row, v in row.items()}
            
            # stringify dict
        
            all_rows.append(clean_row)
            # get response from request and write to dict
        all_json_obj = json.dumps(all_rows)
        hdr = {"Content-Type": "application/json"}

        response = requests.post(url, all_json_obj, headers=hdr)
        
        f.write(response.text)
        f.write("\n")

        for row, subresponse in zip(all_rows, response):
            subresponse = json.loads(subresponse)
            
            input()


            # This solution clearly has a lot to be desired. While it currently uploads all of the data at once 
            # It takes a bit to do so. To get rid of the data upload bottleneck, 
            # a future solution would include bulk csv imports from the backend using a django management command for db seeding, 
            # but currently there are not model level data validations and that would have to be created first. 