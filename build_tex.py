from book_def import bib_dict
from write_tex import write_book_margin, write_chapterbar, write_background, write_text, write_bookChapter

with open('gen1/gen_book_margin.tex', 'w') as file:
    file.write(write_book_margin("GEN"))

with open('gen1/gen2_chapterbar.tex', 'w') as file:
    file.write(write_chapterbar("AMP", "GEN", 2))

with open('gen1/gen2_background.tex', 'w') as file:
    file.write(write_background("GEN", 2))

with open('gen1/gen2_txt.tex', 'w') as file:
    file.write(write_text("AMP", "GEN", 2))

print(write_bookChapter("GEN", 2))