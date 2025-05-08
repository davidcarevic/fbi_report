from utils import isValidCase, checkPhone, saveReport

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
    cateData = isValidCase(query)
    if not cateData:
        print("Error: No matching FBI case found.")
        return
    len(data.get("items", []))


    #build report
    report = {
        "query": query,
        "phone": phone,
        "country": phoneData['region']
    }

    #save report in reports.json
    saveReport(report)
    print("Report submitted successfully.")
    print(f"Country detected: {phoneData['region']}")

if __name__ == "__main__":
    main()
