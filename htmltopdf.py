from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

name = input("Enter name: ")
role = input("Enter role: ")
address = input("Enter address: ")
template_vars = {"name" : name, "role" : role, "address" : address}

def export_pdf(file_name, template_vars):
    import_path = os.path.join(os.path.dirname(__file__), 'templates')
    export_path = os.path.join(os.path.dirname(__file__), 'exports/')

    env = Environment(loader = FileSystemLoader(searchpath = import_path))
    template = env.get_template(file_name + ".html")
    html_out = template.render(template_vars)
    HTML(string = html_out).write_pdf(export_path + file_name + ".pdf")

export_pdf("template_1", template_vars)
export_pdf("template_2", template_vars)