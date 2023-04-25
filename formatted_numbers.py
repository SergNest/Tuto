def formatted_numbers():
  list = []
  # list.append("|{0:<10}|{0:^10}|{0:>10}|".format("decimal", "hex", "binary"))
  print("|{:<10}|{:^10}|{:>10}|".format("decimal", "hex", "binary"))
  for i in range(16):
    print("|{0:<10d}|{0:^10x}|{0:>10b}|".format(i))
    # list.append("|{0:<10d}|{0:^10x}|{0:>10b}|".format(i))
  # return list
    

print(formatted_numbers())
