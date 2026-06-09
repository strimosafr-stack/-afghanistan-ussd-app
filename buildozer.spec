[app]

# (string) Title of your application
title = Afghanistan USSD App

# (string) Package name
package.name = ussdapp

# (string) Package domain (needed for android packaging)
package.domain = org.afghanistan

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (string) Application versioning (method 1)
version = 1.0.1

# (list) Application requirements
# این خط بسیار حیاتی است؛ نسخه‌ها دقیقاً هماهنگ شده‌اند تا تداخل رخ ندهد
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,pyjnius,jnius

# (str) Custom source folders for requirements
# It can be a comma separated list of folders
# android.add_src =

# (list) Permissions
# اگر برنامه شما نیاز به تماس مستقیم دارد، این دسترسی‌ها لازم است
android.permissions = INTERNET, CALL_PHONE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
# نسخه 25b پایدارترین نسخه برای این ترکیب پایتون و کیوی است
android.ndk = 25b

# (int) Android NDK API to use
android.ndk_api = 21

# (bool) Use private storage for data (True or False)
android.private_storage = True

# (list) Android architectures to build for
# برای جلوگیری از خطای حافظه و سرعت بالا در گیت‌هاب، فقط معماری اصلی 64 بیتی را هدف می‌گیریم
android.archs = arm64-v8a

# (bool) Skip byte compile for .py files
android.skip_byte_compile = False

# (string) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Ant anticlockwise rotation of the screen
android.rotation = 1


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
