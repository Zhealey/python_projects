def hello():
  print ("Hello")

def pack(one, two, three):
  return [one, two, three]

def eat_lunch(lunch_list):
  if len(lunch_list) == 0:
    print("My lunchbox is empty")
  else:
    for food in range(len(lunch_list)):
      if food == 0:
        print(f"First I eat my {lunch_list[0]}")
      else:
        print(f"Next I eat my {lunch_list[food]}")


hello()
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["banana"])
eat_lunch(["apple","sandwich","water","cookie"])
