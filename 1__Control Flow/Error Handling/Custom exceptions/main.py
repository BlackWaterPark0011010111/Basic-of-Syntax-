class MyError(Exception):
    pass
try:
    raise MyError("Myc custom error")
except MyError as e:
    print("gotcha: ",e)

raise MyError("someth went wrong")

class Error(Exception):
    def __init__(self, age):
        self.age=age
        super().__init__(f"U`re 'age' {age}  toooo small 4 registration")

    def 