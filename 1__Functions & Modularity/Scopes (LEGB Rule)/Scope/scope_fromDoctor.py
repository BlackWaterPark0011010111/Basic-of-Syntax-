#global_var = ["I am a global variable set outside of the function"]
global_var = "I am a global variable set outside of the function"

# def localFunc(global_var):
#     print(global_var)
#     print(id(global_var))
#     # global_var.append("New string")
#     # global_var.append("Another element")
#     # global_var.append(3)
#     # global_var.append([3, 4, 5, 6])
#     global_var = "I am a new contents of the global var set inside the local function"
#     print(global_var)
#     print(id(global_var))

# # localFunc(global_var)
# # print(global_var)
# # print(id(global_var))

# def anotherFunction():
#     localFunc(global_var)
#     localFunc(global_var)
#     localFunc(global_var)

# anotherFunction()

# settings =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "whatever": "Ford",
#   "subsettings": [1, 2, 3, 4],
#   "userProfile": {"username": "Paul", "password": [12345, 'strong']},
#   "brand": "New brand - a repeated key"
# }
# print(len(settings))

# #accessing list as a value
# print(settings["subsettings"][-1])

# # #accessing dict
# # print(settings["userProfile"]["password"][1])

# settings2 = dict(my = "keyValue", value = 23, pair = True, list = [1, 2, 4], brand = "New brand - a repeated key")
# print(settings["brand"])
# # print(settings["subsettings"])
# # print(settings2["pair"])
# # print(settings2.get("pair"))
# settings2["my"] = 132
# print(settings2)
# # settings2.update({"my":23432})
# # print(settings2)

# for key, value in settings2.items():
#     print(f"Settings2 contain the following elements: Key: {key} and value: {value}")

# for x in settings2:
#     print(f"Settings2 contain the following elements: Key: {x} and value: {settings2[x]}")

# Excercise 1
# Define a global variable named settings as a dictionary with a key title that contains a string of your choice
# then create a function named change_site_title that takes one argument of type String and 
# assigns it to the key title in the global variable settings.
# settings = {
#     "title" : "The title in the old dictionary"
# }

# def change_site_title(newTitle):
#     settings["title"] = newTitle

# #Test cases
# print(settings)
# change_site_title("A new fancy title")
# print(settings)

#Ex2
# Keep the previous code 
# and define now a global variable named default_settings as a dictionary with a key title, 
# then create a function named get_title that takes one argument as a dictionary that defaults 
# to default_settings and returns the content of the key title in the given dictionary.

# settings = {
#     "title" : "My original title"
# }

# default_settings = {
#     "title" : "My original title"
# }

# def get_title(dict = default_settings):
#     return dict["title"]

# def change_site_title(newTitle):
#     settings["title"] = newTitle

# #test cases
# print(get_title(settings))
# print(get_title())
# change_site_title("A new fancy title")
# print(get_title(settings))
# print(get_title())

#Excercise 3
#Add a key "pages" to your previous settings and default_settings dictionaries.
# Now, define two functions named get_pages and add_page. 
# They will both have a parameter settings that will default to default_settings.
# The function get_pages will simply return the list stored in the key pages of the given settings dictionary.
# The function add_page will have an additional positional argument that will be the page as a dictionary. 
# The function will append this argument to the pages key of the given settings dictionary.
settings = {
    "title" : "My original title",
    "pages" : []
}

default_settings = {
    "title" : "My original title",
    "pages" : []
}

def get_pages(settings = default_settings):
    return settings["pages"]

def add_page(pages, settings = default_settings):
    listName = settings["pages"]
    listName.append(pages)

#Test cases
home = {"title": "Home", "path": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "path": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))


#Excercise 4

# Create a new function named print_user_profile that will take 4 parameters:
# gender: a String indicating the gender of the user. The values available should be male and female. The default value should be female.
# first: a String with the first name of the user. The default value should be John if the gender is male but it should be Jane if the gender is female.
# last: a String with the last name of the user. The default value should be Doe.
# pictures: a List of strings with the name of the picture files. The default value should be an empty list.

#This function will add a common header picture to all profiles and 
# then it will print on screen the name of the person and 
# its list of pictures (including the common header). Example:

# The user {first} {last} has the following pictures:
# common_header.png
# {user_picture1.png}
# {user_picture2.png}

# If the user has no pictures it should print only the common_header.png file name.

def print_user_profile(gender="female", first="Jane", last="Doe", pictures = []):
    profileInfo = f"The user {first} {last} has the following pictures:"
    profileInfo = profileInfo + "\ncommon_header.png"
    print(profileInfo)

    if pictures: #alternative if len(pictures==0)
       for x in pictures:
           print(x)

# Test cases
test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}
print_user_profile(**test_data1) #print_user_profile(gender="male", etc.)
print_user_profile(**test_data2)
print_user_profile(**test_data3)
print_user_profile(**test_data2)