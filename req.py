import requests
import json
import urllib
from myBeautifulSoup import getAllATage, dataFromXml, getResHtmlAllInput
from rwfile import write_found, write_not_found, write_worng, write_url, write_login_and_pdf_url, write_login_id_and_pass
s = requests.session()

baseUrl = "https://cdn3.digialm.com/EForms/"
comData = "formId=66709&orgId=1631"
comDataObj = {
    "formId": "66709",
    "orgId": "1631"
}

pdfFolderPath = "stet-pdf/"


def getResPage(userid, data, rUrl):
    targetUrl = baseUrl + "loginAction.do"
    response1 = s.post(targetUrl, data=data)
    if response1.status_code == 200:
        dataObj = getAllATage(response1._content)
        if dataObj:
            if dataObj['strDisplayProfile']:
                xml = dataFromXml(dataObj['strDisplayProfile'])
                if xml:
                    xml["sessChk"] = dataObj['sessChk']
                    xml["app_seq_no"] = data['app_seq_no']
                    xml["formId"] = comDataObj['formId']
                    xml["orgId"] = comDataObj['orgId']
                    write_found(userid, xml)
                    uData = {
                        "userid": xml["Application No"],
                        "dob": xml["Date of Birth (dd/MMM/yyyy)"],
                        "category": xml["Category"],
                        "courses": xml["Courses"],
                        "gender": xml["Applicant Gender"]

                    }
                    write_login_id_and_pass(userid, uData)
                    pdfUrl = generatePDFUrl(xml)
                    download_file(pdfUrl, userid)
                    loginAndPdfUrl = {
                        "loginUrl": rUrl,
                        "pdfUrl": pdfUrl
                    }
                    write_login_and_pdf_url(userid, loginAndPdfUrl)
            else:
                print("errer => ", dataObj)
        else:
             print("errer => in getResPage")


def login(userid, password, isDateLast):
    hitUrl = "loginAction.do?subAction=ValidateUser"
    url = baseUrl + hitUrl + "&" + comData + \
        "&userid=" + userid + "&confData=" + password
    response = s.post(url)
    status = 0
    if response.status_code == 200:
        rUrl = response.url
        checkResHtmlA = getResHtmlAllInput(response._content)
        if checkResHtmlA:
            if "error_message" in checkResHtmlA:
                if checkResHtmlA["error_message"] == "* The login id and password combination does not match. ":
                    status = 3
                    if isDateLast:
                        notFound = write_not_found(userid)
                elif checkResHtmlA["error_message"] == "* Incorrect Credentials.":
                    status = 2
                    worngId = write_worng(userid, "worngList.json")
                else:
                    print("error_message => ", checkResHtmlA["error_message"])
            else:
                if "formId" in checkResHtmlA:
                    if checkResHtmlA["formId"] == "Default":
                        status = 2
                        worngId = write_worng(userid, "formIdDefaultError.json")
                    else:
                        status = 1
                        # print("Login success", userid, password)            
                        write_url(userid, rUrl)
                        getResPage(userid, checkResHtmlA, rUrl)
        else:
            print("checkResHtmlA data not found")
    else:
        print("response.status_code", response.status_code)
    return status

    # response_dict = (response.__dict__)


def generatePDFUrl(fData):
    data = fData
    URL = baseUrl + "GeneratePDF?formId="+data["formId"]+"&orgId=" + data["orgId"]+"&appSeqNo=" + data["app_seq_no"] + "&subAction=generatePDF&identifier=" + \
        data["identifier"] + "&checksum="+data["checksum"]+"&entityId=" + \
        data["entityId"]+"&sessChk="+data["sessChk"]+"&eicuListing="
    return URL


def download_file(download_url, filename):
    response = s.get(download_url,  stream=True)
    with open(pdfFolderPath + filename + ".pdf", 'wb') as f:
        f.write(response.content)


# login("STET167962", "21111995", isDateLast=True)
# login("STET235656", "21111996", isDateLast=True)
