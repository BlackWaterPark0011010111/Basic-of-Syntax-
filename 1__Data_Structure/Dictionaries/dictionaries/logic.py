roles = {
    "ST": "Student",
    "REST": "Registered student",
    "AL": "Alumni",
    "AN": "Anonymous",
    "TE": "Teacher",
    "AD": "Admin"
}

users = [
    {"name": "Holly", "role": roles["ST"]},
    {"name": "Peter", "role": roles["ST"]},
    {"name": "Luke", "role": roles["ST"]},
    {"name": "Janis", "role": roles["TE"]},
    {"name": "Aretha", "role": roles["TE"]},
    {"name": "Ringo", "role": roles["AD"]}
]

modules = [
    {"title": "Computer basics", "teacher": "Janis", "registered": ["Peter"], "alumni": ["Luke", "Holly"]},
    {"title": "Python basics", "teacher": "Janis", "registered": ["Holly"], "alumni": [], "requirement": "Computer basics"},
    {"title": "Django basics", "teacher": "Aretha", "registered": [], "alumni": [], "requirement": "Python basics"}
]

module_permissions = {
    roles["AN"]: ["describe"],
    roles["ST"]: ["describe"],
    roles["REST"]: ["describe", "read", "comment"],
    roles["AL"]: ["describe", "read"],
    roles["TE"]: ["describe", "read"],
    roles["AD"]: ["describe", "read", "write", "comment"]
}

def get_user_by_name(user_name):
    for user in users:
        if user["name"].lower() == user_name.lower():
            return user
    return None

def get_module_by_name(module_name):
    for module in modules:
        if module["title"].lower() == module_name.lower():
            return module
    return None

def has_permission(user_name, module_name, permission):
   
    user = get_user_by_name(user_name)
    module = get_module_by_name(module_name)

    if not user or not module:
        return False

    role = user["role"]

# check for anonymous 
    if role == roles["AN"]:
        return permission in module_permissions[roles["AN"]]

# check for teacher
    if role == roles["TE"]:
        if user_name == module["teacher"]:
            return permission in module_permissions[roles["AD"]]
        else:
            return permission in module_permissions[roles["TE"]]

#check registered student and alumni
    if role == roles["ST"]:
        if user_name in module["registered"]:
            return permission in module_permissions[roles["REST"]]
        elif user_name in module["alumni"]:
            return permission in module_permissions[roles["AL"]]
        else:
            return permission in module_permissions[roles["ST"]]

#check admin (AD)
    if role == roles["AD"]:
        return permission in module_permissions[roles["AD"]]

    return False

# Test 
for permission in module_permissions[roles["AD"]]:
    for module in modules:
        print(f"Can {permission.upper()} on {module['title'].upper()}?")
        print("Anonymous", has_permission("Somebody", module["title"], permission))
        for user in users:
            print(user["name"], has_permission(user["name"], module["title"], permission))
