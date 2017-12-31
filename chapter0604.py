from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
csvReader = csv.DictReader(dataFile) # CSV 파일의 각 행을 리스트 객체가 아니라 딕셔너리 객체로 반환.

for row in csvReader:
    print("The album \""+row["Name"]+"\" was released in "+str(row["Year"]))

# for row in csvReader:
#     print(row)
