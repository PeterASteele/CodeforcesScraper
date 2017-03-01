import pdfkit
import sys
from bs4 import BeautifulSoup
import urllib2


config = pdfkit.configuration(wkhtmltopdf='./wkhtmltox/bin/wkhtmltopdf')
def get_problem_statement(url,output_file):
    pd = pdfkit.from_url(url,output_file,configuration=config)


get_problem_statement("http://codeforces.com/contest/778/problem/A","A_file.pdf")
