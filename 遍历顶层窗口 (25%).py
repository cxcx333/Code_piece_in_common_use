from pprint import pprint

import win32gui

hwnd_title, empty = {}, []


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_title.items():
    if not t or t == 'NVIDIA GeForce Overlay':
        empty.append(h)

for i in empty:
    del hwnd_title[i]

pprint(hwnd_title)
