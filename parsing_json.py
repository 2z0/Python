#압축파일을 압축 해제한 후 , 그 안의 json 파일 내용 파싱하기
import json, zipfile

ext = zipfile.ZipFile('.zip').extract('package.json')

with open(ext, "r", encoding="utf8") as f:
    contents = f.read()
    json_data = json.loads(contents)

print(json_data["name"])
print(json_data["keywords"])
print(json_data["author"])
