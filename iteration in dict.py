math={"john":88.0,"sam":77.0}
for value in math.values():
    print(value)
math={"john":88.0,"sam":77.0}
for key in math.keys():
    print(key)
eng={"rammos":34.0,"asensio":50}
sci={}
for eng in (math,eng): sci.update(eng)
print(sci)
      #concatenation of dictionaries#