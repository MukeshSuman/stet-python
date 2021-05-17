import urllib
import re
from bs4 import BeautifulSoup

def getAllATage(html):
    soup = BeautifulSoup(html)
    tags = soup("input")
    results = {}
    for tag in tags:
        if tag.get("name") == "strDisplayProfile":
            results[tag.get("name")] = tag.get("value")
        elif tag.get("name") == "sessChk":
            results[tag.get("name")] = tag.get("value")
    return results


def getResHtmlAllInput(html):
    soup = BeautifulSoup(html)
    tags = soup.find_all("input")
    results = {}
    for tag in tags:
        results[tag.get("name")] = tag.get("value")
    return results


def dataFromXml(xml):
    results = {}
    content = xml
    bs_content = BeautifulSoup(content, "lxml")
    child = bs_content.find_all('field')
    pdfidentifier = bs_content.find_all('pdfidentifier')
    results["identifiers"] = []
    if pdfidentifier:
        for pdfid in pdfidentifier:
            identifier = pdfid.get_text()
            value = re.findall(r'\d+', identifier)[0]
            if value:
                results["identifiers"].append(value)
    else:
        results["identifiers"] = []

    for field in child:
        keyVar = ""
        key = field.find('htmldisplayname').get_text()
        value = field.find('value').get_text()
        keyVar = field.find('htmlname').get_text()
        if key == " ":
            key = field.find('htmlname').get_text()
        if not key:
            key = field.find('htmlname').get_text()
        value = value.replace('<![CDATA[', '')
        value = value.replace(']', '')
        value = value.replace('>', '')
        results[key] = value
    return results
