"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

Names dataset
"""
import requests

def extract(url="https://github.com/tokern/piicatcher/blob/aa15f90bd25a45fc7b3ab75c52be71d714b8b57a/tests/samples/sample-data.csv", 
            file_path="data/DataSet_withNames.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



