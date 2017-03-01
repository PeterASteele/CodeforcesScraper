import pdfkit
import sys
from bs4 import BeautifulSoup
import urllib2
import re
config = pdfkit.configuration(wkhtmltopdf='./wkhtmltox/bin/wkhtmltopdf')
def get_problem_statement(url,output_file):
    url_results = urllib2.urlopen(url).read()
    soup = BeautifulSoup(url_results)
    val = soup.find("div", attrs={"class": re.compile('ttypography')})
    head_val = soup.find("head")
    for v in head_val.findAll("script"):
      v.extract()
    for v in head_val.findAll("link"):
      v.extract()
    for v in val.findAll("div", attrs= {"class" : re.compile('sample-tests')}):
      v.extract()
    val.find("div", attrs={"class" : re.compile("title")}).extract()
    val.find("div", attrs={"class" :  re.compile("time-limit")}).extract()
    val.find("div", attrs={"class" :  re.compile("memory-limit")}).extract()
    val.find("div", attrs={"class" :  re.compile("input-file")}).extract()
    val.find("div", attrs={"class" :  re.compile("output-file")}).extract()
    html_string = "<html>" + unicode(head_val.prettify()) + "<body>" + unicode(val.prettify()) + "</body></html>"
    print(html_string.encode(encoding="UTF-8", errors="ignore"))
  #pdfkit.from_string(html_string, output_file, configuration=config)

if __name__ == "__main__":
	argv = sys.argv
	get_problem_statement(sys.argv[1],sys.argv[2])
