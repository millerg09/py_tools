import subprocess

# take what's on the clipboard and use it in function
p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
data = p.stdout.read()

x = data.encode()
x = x.split("\n")

# Convert from list of str to list of int
for i in range(0, len(x)):
    x[i] = int(x[i])
    #x[i] = float(x[i])

# sum the array
sum_x = sum(x)

# find the number of objects in the array
len_x = len(x)

# calculate and print the average
avg = sum_x / len_x
print(avg)