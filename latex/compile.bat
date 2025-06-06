@echo off
cd /d "C:\Users\User\Documents\L2-Ongoing\May task\N56501\latex"

echo Compiling LaTeX document...

rem First compilation
pdflatex -interaction=nonstopmode main.tex

rem Second compilation for references
pdflatex -interaction=nonstopmode main.tex

rem Third compilation for final
pdflatex -interaction=nonstopmode main.tex

echo.
echo Compilation complete!

rem Check if PDF was created
if exist main.pdf (
    echo PDF created successfully: main.pdf
    rem Copy to parent directory with descriptive name
    copy main.pdf "..\Korean_Malay_Causatives_Study.pdf"
    echo PDF copied to: Korean_Malay_Causatives_Study.pdf
) else (
    echo ERROR: PDF creation failed!
)

pause