import winreg

# Reference: https://stackoverflow.com/questions/18044937/is-there-a-way-to-find-the-path-of-an-application-with-standard-libraries

# TODO: Improve success rate
#    Tip1: learn more about reg
#    Tip2: use Total Uninstall

excutable = 'Evernote.exe'
handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                        r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\\" + excutable)
num_values = winreg.QueryInfoKey(handle)[1]
for i in range(num_values):
    print(winreg.EnumValue(handle, i))
