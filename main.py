from subprocess import call
a = call('hcitool con', shell=True)
print("a")
print(a)