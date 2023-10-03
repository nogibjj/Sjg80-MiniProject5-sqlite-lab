"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or
CSV formats tend to work well

Names dataset
"""
import requests

def extract(url="https://github.com/nogibjj/Sjg80-MiniProject5-sqlite-lab"
    "/blob/6c2ab2fb3e8c193f60cf683b8668e71ce03d0f89/DataSet_withNames.csv",
            file_path="data/DataSet_withNames.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path





