from book_def import bib_dict
from write_tex import write_book_margin, write_chapterbar, write_background, write_text, write_bookChapter, write_tex_main, write_reflection_page
from get_chapter import getNChapters
import os
import shutil

def build_bible(translation):

    if not os.path.exists("tex_bible"):
        os.makedirs("tex_bible")


    shutil.copy('templates/preamble.tex', 'tex_bible/preamble.tex')

    with open('tex_bible/bible.tex', 'w') as file:
        file.write(write_tex_main(translation))

    for book in bib_dict:
        lbook = book.lower()
        nchapters = getNChapters(translation, book)

        with open('tex_bible/'+lbook+'_book_margin.tex', 'w') as file:
            file.write(write_book_margin(book))

        for i in range(1, nchapters+1):
            with open('tex_bible/'+lbook+str(i)+'_chapterbar.tex', 'w') as file:
                file.write(write_chapterbar(translation, book, i))

            with open('tex_bible/'+lbook+str(i)+'_background.tex', 'w') as file:
                file.write(write_background(book, i))

            with open('tex_bible/'+lbook+str(i)+'_txt.tex', 'w') as file:
                file.write(write_text(translation, book, i))

            with open('tex_bible/'+lbook+str(i)+'_reflection.tex', 'w') as file:
                file.write(write_reflection_page(book, i))

build_bible("ESV")

