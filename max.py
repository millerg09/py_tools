import subprocess

# take what's on the clipboard and use it in function
p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
data = p.stdout.read()

x = data.encode()
x = x.split("\n")

# Convert from list of str to list of int
for i in range(0, len(x)):
    x[i] = float(x[i])
    #x[i] = float(x[i])

# find and print the minimum value
print(max(x))