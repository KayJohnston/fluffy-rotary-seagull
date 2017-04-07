import subprocess

given_name = input('Given name: ')
surname = input('Surname: ')

filename = 'crude.ps1'

with open(filename,'w') as opened:
    opened.write('Import-Module ActiveDirectory\n')
    line = '$results = Get-ADUser -filter {(Surname -eq \"' + surname + '\") -and (GivenName -eq \"' + given_name + '\")}\n'
    opened.write(line)

    opened.write('ForEach ($user in $results) {\n')
    opened.write('Write-Host $user.SamAccountName\n')
    opened.write('}\n')
    
subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./crude.ps1\";", "&hello"])

##dave = subprocess.Popen(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./crude.ps1\";", "&hello"], stdout = subprocess.PIPE)
##
##erica = dave.communicate()
