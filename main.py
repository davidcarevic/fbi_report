from utils import getCase, checkPhone, saveReport, getClientIP
from pprint import pprint

def main():
    print("=== Witness Report Submission ===")
    
    #data inputs
    query = input("Enter name or case title: ").strip()
    phone = input("Enter your phone number: ").strip()
    
    #clientIP
    clientIP =getClientIP()

    #run both checks
    phoneData = checkPhone(phone)
    caseData = getCase(query)
    hasError = False

    if not phoneData['valid']:
        print("Error: Invalid phone number.")
        hasError = True

    if  not caseData or caseData.get('items') == []:
        print("Error: No matching FBI case found.")
        hasError = True

    if hasError:
        return  #exit early if either check failed

    #extract first matching case
    matched_case = caseData.get("items", [])[0]  # pick the first match

    #build report
    report = {
        "query": query,
        "phone": phone,
        "phoneCountry": phoneData['region'],
        "clientIP": clientIP,
        "case": {
            "uid": matched_case.get("uid", ""),
            "title": matched_case.get("title", ""),
            "description": matched_case.get("description", ""),
            "image": matched_case.get("images", [{}])[0].get("original", ""),
            "details": matched_case.get("details", "")
        }
    }

    #save report in reports.json
    saveReport(report)
    print("Report submitted successfully.")

if __name__ == "__main__":
    main()
