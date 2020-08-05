import win32api
import win32con
import win32gui
import win32process
from time import sleep

sleep(2)
hWnd = win32gui.GetForegroundWindow()  # What is hwnd?:https://blog.csdn.net/bjbz_cxy/article/details/79866828
_, pid = win32process.GetWindowThreadProcessId(hWnd)
hProcess = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, 0, pid)
path = win32process.GetModuleFileNameEx(hProcess, 0)



print(path)