from selenium.webdriver.chrome.options import Options

options = Options()
# 禁止图片和css加载
prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
options.add_experimental_option("prefs", prefs)
# 无头模式
options.add_argument('--headless')
