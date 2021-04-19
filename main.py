from subprocess import call, check_output
output = check_output(['hcitool', 'con']).decode("utf-8") 
lines = output.split(">")

devices = []
for d in range(1, len(lines)):
    mac = lines[d].strip().split(" ")[1] #ziska mac adresu
    name = check_output(["hcitool", "name", mac]).decode("utf-8").rstrip()
    devices.append((mac, name))

for i in devices:
    print(i)