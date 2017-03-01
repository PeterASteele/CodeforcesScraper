import pdfkit
import sys
from bs4 import BeautifulSoup
import urllib2



def get_problem_statement(url):
    pd = pdfkit.from_url(url,"test_output")


get_problem_statement("http://codeforces.com/contest/778/problem/A")