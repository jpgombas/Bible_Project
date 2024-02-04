from book_def import bib_dict
from write_tex import write_book_margin, write_chapterbar, write_background, write_text, write_bookChapter, write_tex_main, write_reflection_page
from get_chapter import getNChapters

nchapters = getNChapters("AMP", "GEN")

with open('gen/gen_book_margin.tex', 'w') as file:
    file.write(write_book_margin("GEN"))

with open('gen/gen.tex', 'w') as file:
    file.write(write_tex_main("AMP", "GEN"))

for i in range(1, nchapters+1):
    with open('gen/gen'+str(i)+'_chapterbar.tex', 'w') as file:
        file.write(write_chapterbar("AMP", "GEN", i))

    with open('gen/gen'+str(i)+'_background.tex', 'w') as file:
        file.write(write_background("GEN", i))

    with open('gen/gen'+str(i)+'_txt.tex', 'w') as file:
        file.write(write_text("ESV", "GEN", i))

    with open('gen/gen'+str(i)+'_reflection.tex', 'w') as file:
        file.write(write_reflection_page("GEN", i))



