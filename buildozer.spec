[app]
title = USSD Afghanistan
package.name = ussdapp
package.domain = org.akrami
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pyjnius
orientation = portrait
fullscreen = 0
android.permissions = android.permission.CALL_PHONE
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.private_storage = True
android.entrypoint = org.kivy.android.PythonActivity
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
