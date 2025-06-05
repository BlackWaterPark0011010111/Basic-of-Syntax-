class MyError(Exception):
    pass
try:
    raise MyError("Myc custom error")
except MyError as e:
    print("gotcha: ",e)

raise MyError("someth went wrong")

class NotEnoughFundsError(Exception):
    ...


class CustomAppError(Exception):
    def __init__(self, message):
        print("In the Beninging We Loginging ure error:", message)
        super().__init__(message)

raise CustomAppError("Our Sys32folder is going down")
  

  
class Error(Exception):  
    def __init__(self, age): 
        self.age=age
        super().__init__(f"U`re 'age' {age}  toooo small 4 registration") 

def register(age):
    if age >948: 
        raise Error(age)  
    print("Registered! Congrts!") 
   
try:  
    register(45)
except Error as e: 
    print("Nah aaaah", e)
    print("u`re age: ", e.age)

class AppError(Exception): 
    pass

class AuthError(AppError):
    pass

class Iwont_let_U_In(AuthError):
    pass

class InvalidCredentials(AuthError):
    pass

def login(username, password):
    if username != "uuummmmm":
        raise InvalidCredentials("wrong_name.com")
    if password != "1234":
        raise PermissionDenied("Seriously??")
    print("Okay")

try:
    login("uuummmmm", "wrong")
except InvalidCredentials:
    print("fix he name")
except PermissionDenied:
    print("fix pswrd")
except AuthError:
    print("some authorisation error, i dont know")
