from io import BytesIO

import markdown
from markdown.extensions.codehilite import CodeHiliteExtension

from pygments import highlight
from pygments.lexers import PythonLexer, TextLexer
from pygments.formatters import HtmlFormatter


from weasyprint import HTML


def markdown_to_html(md_text):
    # output_dir.mkdir(parents=True, exist_ok=True)
    # file_name = input_path.name.split(".md")[0]
    # output_path = output_dir/f"{file_name}.pdf"

    # with open(input_path, 'r', encoding="utf-8") as f:
    #     md_text = f.read()

    # vs_code_css_path = repo.scripts_dir/"css"/"vscode.css"
    # with open(vs_code_css_path, "r") as f:
    #     vscode_css = f.read()

    md_html = markdown.markdown(md_text,
        extensions=[
            CodeHiliteExtension(guess_lang=False),
            'fenced_code', ])

    full_html = f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
        {HtmlFormatter(style='default').get_style_defs('.codehilite')}
        </style>
    </head>
    <body>
    {md_html}
    </body>
    </html>"""

    return full_html
