from subprocess import call, check_output
a = call('hcitool con', shell=True)
b = check_output(['hcitool', 'con'])
print("a")
print(b)