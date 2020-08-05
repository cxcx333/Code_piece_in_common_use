import winreg
import re


class InstalledSoftwareInfo:
    """获取电脑上已安装软件的名称、路径、版本等信息"""

    def __init__(self):
        def get_installed_softwares(hive, flag):
            aReg = winreg.ConnectRegistry(None, hive)
            aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                                  0, winreg.KEY_READ | flag)

            count_subkey = winreg.QueryInfoKey(aKey)[0]

            software_list_ = []

            for i in range(count_subkey):
                software_ = {}
                try:
                    asubkey_name = winreg.EnumKey(aKey, i)
                    asubkey = winreg.OpenKey(aKey, asubkey_name)
                    software_['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

                    try:
                        software_['path'] = winreg.QueryValueEx(asubkey, "DisplayIcon")[0]
                    except EnvironmentError:
                        software_['path'] = None

                    try:
                        software_['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
                    except EnvironmentError:
                        software_['version'] = None

                    try:
                        software_['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
                    except EnvironmentError:
                        software_['publisher'] = None

                    try:
                        software_['uninstall_exe'] = winreg.QueryValueEx(asubkey, "UninstallString")[0]
                    except EnvironmentError:
                        software_['uninstall_exe'] = None

                    software_list_.append(software_)
                except EnvironmentError:
                    continue

            return software_list_

        self.software_list = get_installed_softwares(winreg.HKEY_LOCAL_MACHINE,
                                                     winreg.KEY_WOW64_32KEY) + get_installed_softwares(
            winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + get_installed_softwares(winreg.HKEY_CURRENT_USER, 0)
        self.num_of_all = len(self.software_list)

        count = 0
        steam_path = self.get_path('Steam').replace('uninstall', 'steam')
        start_str = '"' + steam_path + '" steam://uninstall/'
        for i in self.software_list:  # "C:\Program Files (x86)\Steam\steam.exe" steam://uninstall/431960
            if type(i['uninstall_exe']) == str and i['uninstall_exe'].startswith(start_str) \
                    and re.match('\d+', i['uninstall_exe'].split(start_str)[1]):
                count += 1
        self.num_of_steam_app = count
        self.software_names = []
        for i in self.software_list:
            self.software_names.append(i['name'])

    def get_path(self, name):
        """返回软件的图标，大概率是软件的程序路径"""
        for i in self.software_list:
            if i['name'] == name:
                return i['path']

    def get_version(self, name):
        """返回软件的版本"""
        for i in self.software_list:
            if i['name'] == name:
                return i['version']

    def get_uninstall_path(self, name):
        """返回软件的卸载程序路径"""
        for i in self.software_list:
            if i['name'] == name:
                return i['uninstall_exe']
