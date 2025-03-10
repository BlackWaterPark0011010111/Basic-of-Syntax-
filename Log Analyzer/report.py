def create_report(errors,warnings):
    report = "Log Analysis Report\n"
    report=+ "=" * 50 + "\n"

    if errors:
        report+= "Error:.n"
        for error in errors:
            report +=f"- {error}\n"
    else:
        report += "No erros found\n"
    report +="\n"

    if warnings:
        report +="Warning:\n"
        for warning in warnings:
            report += f"- {warning}\n"
    else:
        report +="No warnings found\n"

    report+="=" * 50 + "\n"
    return report