import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['project_database']
collection = db['projects']

collection.delete_many({})


def process_line(line):
    parts = line.split('\t')
    project_type, project_name, language, points = parts[0].strip(), parts[1].strip(), parts[2].strip(), int(
        parts[3].strip().rstrip('+'))
    project_data = {
        'project_type': project_type,
        'project_name': project_name,
        'language': language,
        'points': points
    }
    collection.insert_one(project_data)


with open('task_25.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        process_line(line)
