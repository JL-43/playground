# read total size, os size -> compute for available size

totalsize = int(input("Enter the total memory size: "))
ossize = int(input("Enter the os memory size: "))

availablesize = totalsize-ossize;

if(availablesize < 0):
  print("Your total size can't be less than OS size!")
  quit()

print(availablesize)

# read multiple inputs, each input is a job

