#Connected to github :D



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
      print("No variable \"", e, "\" found")

    
  else:
    print("Syntax not understood.")

while True:
  code = input(">> ")
  readcode()
  