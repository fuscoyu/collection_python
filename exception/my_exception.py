class Myexception(Exception):
      pass

try:
    raise Myexception("my exception")
except Exception as e:
    print(e)
