python build_tex.py
cd tex_bible
pdflatex -interaction=batchmode bible.tex
mv bible.pdf ..
cd ..
