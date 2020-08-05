import win32clipboard


def get_clipboard_text():
    win32clipboard.OpenClipboard()
    try:
        clipboard_text = win32clipboard.GetClipboardData()  # TypeError will be raised if it is a file or files or nothing in clipboard.
    except TypeError:
        clipboard_text = ''
    finally:
        win32clipboard.CloseClipboard()
    return clipboard_text
