import re
"""Checks if the given strings match the specified regex pattern."""

def test_regex(pattern, test_strings, description):
    
    print(f"📌 {description}\nPattern: {pattern}\n")
    compiled_pattern = re.compile(pattern)

    for string in test_strings:
        match = compiled_pattern.search(string)
        
        result = "✅ Match" if match else "❌ No match"
        print(f"Test: {string} → {result}")
    print("\n" + "-"*50 + "\n")

# 1. colou?r → Matches both "color" and "colour"
test_regex(r"colou?r", ["color", "colour", "colorr", "colouur"], "Allows 'u' to be optional in 'color'")

# 2. Email validation for gmail.com or deliveryhero.com
test_regex(r"(\W|^)[\w.-]{0,25}@(gmail|deliveryhero)\.com(\W|$)",
           ["test@gmail.com", "hello@deliveryhero.com", "user@yahoo.com", "invalid-email"],
           "Valid emails must end with @gmail.com or @deliveryhero.com")

# 3. Password (6-12 characters, at least one digit, uppercase, and lowercase letter)
test_regex(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,12}$",
           ["Hello1", "pass123", "HELLO1", "ValidP4ss", "short", "WayTooLongPassword123"],
           "Password: 6-12 chars, at least one number, uppercase, and lowercase letter")

# 4. HEX color code (3 or 6 valid hex characters)
test_regex(r"^#?([a-f0-9]{6}|[a-f0-9]{3})$",
           ["#fff", "123abc", "#123456", "ggg999", "12"],
           "HEX color code: Must be 3 or 6 characters (0-9, a-f)")

# 5. Text that ends with "done"
test_regex(r"done$", ["task done", "almost done", "done today", "completed"], "Text must end with 'done'")
