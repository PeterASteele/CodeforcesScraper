import pdfkit
import sys
from bs4 import BeautifulSoup


config = pdfkit.configuration(wkhtmltopdf='./wkhtmltox/bin/wkhtmltopdf')
def get_problem_statement(url,output_file):
    pd = pdfkit.from_url(url,output_file,configuration=config)

if __name__ == "__main__":
	argv = sys.argv
	get_problem_statement(sys.argv[1],sys.argv[2])
