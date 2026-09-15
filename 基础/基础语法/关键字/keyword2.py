name: str = ""

def set_name(_name: str):
  global name
  if not name:
    name = _name

def get_name():
  return name