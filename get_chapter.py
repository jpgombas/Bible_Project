import os
import json

def get_chapter(translation, book, chapter):
    # check for book in OT and NT directory
    if os.path.exists('holybooks/OT/' + book + '/' + translation + '.json'):
        path = 'holybooks/OT/' + book + '/' + translation + '.json'
    elif os.path.exists('holybooks/NT/' + book + '/' + translation + '.json'):
        path = 'holybooks/NT/' + book + '/' + translation + '.json'
    else:
        return 
    # open the file
    with open(path, 'r') as file:
        data = file.read()
    
    # parse file
    json_data = json.loads(data)
    return json_data['text'][int(chapter)]