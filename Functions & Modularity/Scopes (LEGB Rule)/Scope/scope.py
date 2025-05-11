global_var = "I`m a  global variable"

""" 
def localFunk():
    local_var = "Im a local variable"
    print(local_var)
    print(globals)

localFunk()
print(global_var)
print(globals())# что значит globals
global_var = ["i am a global variable set outside of the function"]

 """
""" def localFunk():
    print(global_var)
    global_var.append("new string")
    global_var.append(3)
    global_var.append([3,4,5,6])
    print(id(global_var))

localFunk()
print(id(global_var))

 """


global_var = "I`m a  global variable"

def localFunk(global_var):
    print(global_var)
    global_var = "im a new cotents of the global var set inside the local function"
    print(id(global_var))

localFunk(global_var)
print(id(global_var))

def anotherFunktion():
    localFunk(global_var)
    localFunk(global_var)
    localFunk(global_var)
    localFunk(global_var)

anotherFunktion()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "subsettings": [1,2,3,4],
  "userprofile": {"username":"Me", "password":"[12345,'strong']"}
}
print(len(thisdict))
print(thisdict["subsettings"][-1])

print(thisdict["userprofile"]["password"][1])





settings = {"title" : "Whatever i want"}

def change_site_title(newTitle):
    settings["title"] = newTitle

#test cases
print(settings)
change_site_title("A new fancy title")
print(settings)











default_settings = {

    "title" : "Whatever"
}
def getTitle(dict = default_settings):


    def change(dict):
        settings["title"] = "newtitle"








settings = {
    "title" : "Whatever i want",
    "pages" : []
}
default_settings = {

    "title" : "Whatever",
    "pages": []
}

def get_pages(settings = default_settings):
    
    return settings["pages"]

def add_page(pages,settings = default_settings):
    settings ["pages"].append(get_pages)

home = {"title": "Home", "path": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "path": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))