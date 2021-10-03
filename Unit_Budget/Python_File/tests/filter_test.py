import pytest
import requests
import json
import csv
import ast

def readCsv():
    data=list()
    with open('testcase.csv','r') as f:
        reader=csv.reader(f)
        next(reader)
        for each in reader:
           data.append(each)
    return data

@pytest.mark.parametrize('data',readCsv())
def test(data):
    r = requests.get(url=data[0], params=ast.literal_eval(data[1]))
    # print(r.text)
    assert json.loads(r.text) == json.loads(data[2])


if __name__ == '__main__':
    pytest.main(["-s","-v","test.py"])
