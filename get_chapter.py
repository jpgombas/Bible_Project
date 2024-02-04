import os
import json

def getChapterText(translation, book, chapter):
    # check for book in OT and NT directory
    if os.path.exists('holybooks/OT/' + book + '/' + translation + '.json'):
        path = 'holybooks/OT/' + book + '/' + translation + '.json'
    elif os.path.exists('holybooks/NT/' + book + '/' + translation + '.json'):
        path = 'holybooks/NT/' + book + '/' + translation + '.json'
    else:
        return 
    # open the file
    with open(path, 'r') as file:
        return json.loads(file.read())['text'][int(chapter)]