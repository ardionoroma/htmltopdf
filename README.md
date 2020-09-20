# htmltopdf
Convert HTML templates to PDF with only inserting the data once.

Confused of inserting same data into various template? Afraid of mistakes because you tired of inserting data many times? This simple program will help you fill the various template by only inserting the data once.

How to use:
1. Prepare the templates in HTML format. If you have the templates in Microsoft Word format, please convert it to HTML first. Hopefully this program can convert the .docx format to HTML in the future.
2. Place the templates inside the **templates** folder.
3. Specify the variables inside the HTML templates, surrounded by **"{{"** and **"}}"**.
4. Specify the variables inside the program, load the templates, and call the **export_pdf()** function as much as the templates you have.
5. Run! Execute the program with **"python htmltopdf.py"**, insert the variables with data you want, and voila! The same data you inserted will be filled in all templates you have.

Written in ![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

Libraries used: **jinja2**, **weasyprint**

The template examples used here were from:
- http://fe.uny.ac.id/sites/fe.uny.ac.id/files/SURAT%20PERJANJIAN%20KONTRAK%20KERJASAMA.docx
- https://www.lamudi.co.id/journal/wp-content/uploads/2015/03/Contoh-Surat-Perjanjian-Sewa-Rumah-Lamudi-Indonesia.doc
