import os
import json
from book_def import bib_dict
from get_chapter import get_chapter

nam2 = get_chapter("AMP","NAM","2")
for verse in nam2['text']:
    print(verse['text'])
# directory = 'holybooks/EN/OT/'


# for key in json_data[0]['text'][0].keys():
#     print(key, type(json_data[0]['text'][0][key]))

# print(json_data[0]['text'][0]['text'][0])

# for book in json_data:
#     if book['name'] == 'Genesis':
#         print(book['name'])
       
# for verse in json_data[0]['text'][0]['text']:
#     print(verse['text'])

# for i, key in enumerate(bib_dict):
#     if (i+1)%22==0:
#         print("\hyperlink{dummy}{"+key+"}\\\\\hline")
#     else:
#         print("\hyperlink{dummy}{"+key+"}\n&")