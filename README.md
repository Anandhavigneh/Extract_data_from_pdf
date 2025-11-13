Extract Data From PDF (Human-Friendly README)

This is a small Python script that helps you quickly extract text from any PDF file.
You don’t need to manually open the PDF — the script will automatically find it and read it for you.

 What This Script Does

Looks for a PDF file automatically in the script folder

Or you can pass a PDF path manually

Reads the PDF safely using PyPDF2

Shows:

Total number of pages

Text from the first page

Simple. Clean. Easy.

Install Requirements

Just install PyPDF2:

pip install PyPDF2

How to Use
Method 1: Auto-detect PDF

Just put your PDF file in the same folder as pdf.py and run:

python pdf.py


The script will find the PDF and extract its text.

Method 2: Give PDF path

Run this:

python pdf.py myfile.pdf


or full path:

python pdf.py D:\files\report.pdf

What Output Looks Like

Example:

3
Welcome to the Report
This document explains the monthly performance...


First line → number of pages
Next lines → extracted text from page 1

If Something Goes Wrong

The script will show friendly messages such as:

"No PDF found" → There is no PDF in the folder

"Error: PDF file not found" → Wrong path

"Error reading PDF" → PDF is damaged or locked

This helps you know exactly what the problem is.

About the Code

The script first tries to find any .pdf near the script

If not found, it checks the current working directory

You can also pass the file manually

It uses PyPDF2 to read and extract text

It is lightweight and works for most normal PDFs.

Contributions

If you want to improve or add features, feel free to send a pull request.

If you want, I can also create a PRO README with:
 Badges
 GIF demo
 Logo
 Examples folder
 Advanced PDF text extraction

Just tell me!