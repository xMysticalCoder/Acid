#Connected to github :D
# Go to version control for more info
# PLEASE add a comit every time you add something.
# Link to github: ://github.com/xMysticalCoder/acid.
# I invited NILL2021 (I think thats you)
class colors:

  syntax_error = '\033[91m'
  Reset = '\033[0m'

print("Acid Version 1.01")
variables = dict()
def readcode():
  if code.startswith("p(\"") and code.endswith("\")"):
    print(code[3:-2])
  elif code.startswith("v "):
    r = code.split()
    variables[r[1]] = r[-1]
    print(variables)
  elif code.startswith("p(") and code.endswith(")"):
    e = code[2:-1]
    try:
      print(variables[e])
    except:
      print(colors.syntax_error + "No variable \"", e, "\" found" + colors.Reset)

    
  else:
    print(colors.syntax_error + "Syntax not understood." + colors.Reset)

while True:
  code = input(">> ")
  readcode()
  