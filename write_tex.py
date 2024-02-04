from book_def import bib_dict
from get_chapter import getNChapters, getChapterText

# Write the tex file
def write_bookChapter(book, chapter):
    text = ""
    text += "\\hypertarget{"+book.lower()+str(chapter)+"}{\\include{"+book.lower()+str(chapter)+"_background}}\n\n"
    text += "\\input{"+book.lower()+str(chapter)+"_chapterbar}\n\n"
    text += "\\medskip\n"
    text += "\\input{"+book.lower()+str(chapter)+"_txt}\n\n"
    text += "\\newpage\n"

    return text

# Book margin writer
def write_book_margin(book):
    text = "\\fontsize{2}{8}\selectfont%\n"
    text += "\\rotatebox[origin=tr]{90}{%\n"
    text += "\\renewcommand{\\arraystretch}{1.4}%\n"
    text += "\\fbox{%\n"
    text += "\\begin{tabularx}{18.5cm}{*{21}{Y|}Y}%\n"
    for i, testbook in enumerate(bib_dict):
        if testbook == book:
            text += "\t\\cellcolor{black}{\\textcolor{white}{"+testbook+"}}\n"
            text += "\t&\n"
        elif i == len(bib_dict)-1:
            text += "\t\\hyperlink{dummy}{REV}%\n"
        elif (i+1)%22==0:
            text += "\t\\hyperlink{dummy}{"+testbook+"}\\\\\hline\n"
        else:
            text += "\t\\hyperlink{dummy}{" + testbook + "}\n"
            text += "\t&\n"
    
    text += "\\end{tabularx}%\n}%\n}%"
    return text

# Background writer
def write_background(book, chapter):
    text = r'''
\backgroundsetup{
scale=1,
color=black,
opacity=1,
angle=0,
position=current page.north,
vshift=-0.5\paperheight,
contents={
    \begin{minipage}[t][\paperheight][t]{\paperwidth}
    \centering%
    \vspace{0.5cm}%
    \begin{minipage}[t]{0.9\paperwidth}%
        \begin{adjustwidth}{0cm}{0cm}%
        {\fontsize{15}{5}\selectfont \textbf{''' + bib_dict[book] + ''' ''' + str(chapter) + '''}} \\hfill Note Page % REPLACE
        \medskip%
        \hrule height 1pt
        \end{adjustwidth}%
    \end{minipage}
    \\begin{minipage}[b][19.7cm][b]{0.7\\textwidth}%
        \\include{'''+book.lower()+'''_book_margin}%    % REPLACE
    \\end{minipage}%
    \\begin{minipage}[b]{0.3\\textwidth}%
        \\begin{adjustwidth}{0.5cm}{0.5cm}
            \\Repeat{38}{\\myTodoLineGray}
            \\vspace{5mm}
        \\end{adjustwidth}%
    \\end{minipage}%
    \\end{minipage}%
}
}
    '''
    return text

# Chapterbar writer
def write_chapterbar(translation, book, chapter):
    chapterlimit = getNChapters(translation, book) + 1
    text = "\\fbox{%\n"
    text += "\\begin{tabularx}{8.7cm}{*{11}{C}}\n"
    # Calculate the start and end values for the range
    start = max(1, chapter - 5)
    end = start + 11
    if end > chapterlimit:
        end = chapterlimit
        start = end - 11
    
    # Create the range of integers
    chapter_range = range(start, end) 
    
    for i in chapter_range:
        if chapter == chapterlimit-1 and i == chapterlimit-1:
            text += "\t\\cellcolor{black}{\\textcolor{white}{"+str(i)+"}}\n"
        elif i == int(chapter):
            text += "\t\\cellcolor{black}{\\textcolor{white}{"+str(i)+"}}\n"
            text += "\t&\n"
        elif i==chapter_range[-1]:
            text += "\t\\hyperlink{"+book.lower()+str(i)+"}{"+str(i)+"}\n"
        else:
            text += "\t\\hyperlink{"+book.lower()+str(i)+"}{"+str(i)+"}\n"
            text += "\t&\n"

    text += "\\end{tabularx}\n}"
    return text

# Text writer
def write_text(translation, book, chapter):
    text_data = getChapterText(translation,book,chapter)
    text = ""
    for i, verse in enumerate(text_data['text']):
        if i==0:
            text+=verse['text']+"\n"
        else:
            text+="$^{"+str(i+1)+"}$ "+verse['text']+"\n"
    return text

def write_tex_main(translation, book):
    nchapters = getNChapters(translation, book)
    text = ""
    text += "\\include{preamble}\n\n"
    text += "\\begin{document}\n\n"
    for i in range(1, nchapters+1):
        text += write_bookChapter(book, i)
    text += "\\end{document}"
    
    return text