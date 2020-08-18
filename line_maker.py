import subprocess

# take what's on the clipboard and use it in function
p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
data = p.stdout.read()

x = data.encode()
x = x.split(",")

print (x)

print (len(x))