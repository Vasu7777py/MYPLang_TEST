
import Comand

while True:
    text = input("Comand > ")
    result, error = Comand.run("<stdio>", text)
    if error:
        print(error.as_string())
    else:
        print(result)
