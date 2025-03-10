import re


def parse_log(log_lines):
    errors = []
    warnings = []

    for line in log_lines:
        if "ERROR" in line:
            errors.append(line.strip())

        elif "WARNING" in line:
            warnings.append(line.strip())

    return errors, warnings