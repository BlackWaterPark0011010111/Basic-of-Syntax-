from log_parser import parse_logs
from report import create_report

def main():
    log_file = input("Enter the log file path: ")
    
    try:
        with open(log_file, 'r') as file:
            logs = file.readlines()
    except FileNotFoundError:
        print("File not found")
        return
    except Exception as e:
        print(f"Error: {e}")
        return
    
    errors, warnings = parse_logs(logs)

    if errors or warnings:
        report = create_report(errors, warnings)
        with open('log_report.txt', 'w') as report_file:
            report_file.write(report)
        print("reporrt created successfully")
    else:
        print("no errors or warnings found")

if __name__=="__main__":
    main()