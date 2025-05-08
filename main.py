from utils import getCase, checkPhone, saveReport
from pprint import pprint

def main():
    print("=== Witness Report Submission ===")
    
    #data inputs
    query = input("Enter name or case title: ").strip()
    phone = input("Enter your phone number: ").strip() 

    #phone check
    phoneData = checkPhone(phone)
    if not phoneData:
        print("Error: Invalid phone number.")
        return

    #data fetch and check
    caseData = getCase(query)
    if not caseData:
        print("Error: No matching FBI case found.")
        return

    #extract first matching case
    matched_case = caseData.get("items", [])[0]  # pick the first match

    #build report
    report = {
        "query": query,
        "phone": phone,
        "country": phoneData['region'],
        "case": {
            "uid": matched_case.get("uid", ""),
            "title": matched_case.get("title", ""),
            "description": matched_case.get("description", ""),
            "image": matched_case.get("images", [{}])[0].get("original", "")
        }
    }

    #save report in reports.json
    saveReport(report)
    print("Report submitted successfully.")
    print(f"Country detected: {phoneData['region']}")

if __name__ == "__main__":
    main()
