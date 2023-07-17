import jinja2
import pdfkit
from datetime import datetime

today_date = datetime.today().strftime("%d %b, %Y")
my_name = "Zohaib"
country_zip= "Hyderabad"
checkin = "2023-02-02"
checkout = "2023-03-03"
rooms = "1"
adults = "1"
children = "0"
email = "zoha0004@gmai.com"
phonenumber = "7516413413"

context = {
    'today_date': today_date,
    'my_name': my_name,
    'country_zip': country_zip,
    'checkin': checkin,
    'checkout': checkout,
    'rooms': rooms,
    'adults': adults,
    'children': children,
    'email': email,
    'phonenumber': phonenumber
}


template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'invoice.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
output_pdf = 'invoice.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config, css='invoice.css')