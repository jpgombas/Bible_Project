import os
import json
from book_def import bib_dict
from get_chapter import getChapterText
from write_tex import write_book_margin, write_chapterbar, write_background

# nam2 = get_chapter("AMP","NAM","2")
# for verse in nam2['text']:
#     print(verse['text'])
# directory = 'holybooks/EN/OT/'

gen2 = getChapterText("AMP","GEN","2")

text = ""
for i, verse in enumerate(gen2['text']):
    text+="$^{"+str(i+1)+"}$ "+verse['text']+"\n"

# print(write_book_margin("EXO"))
with open('gen1/gen2_chapterbar.tex', 'w') as file:
    file.write(write_chapterbar("GEN", 2, len(gen2['text'])))

with open('gen1/gen2_txt.tex', 'w') as file:
    file.write(text)

with open('gen1/gen2_background.tex', 'w') as file:
    file.write(write_background("GEN", 2))

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