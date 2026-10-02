[app]

# (str) Title of your application
title = My PS4 PKG Splitter

# (str) Package name
package.name = ps4_pkg_splitter

# (str) Package domain (needed for android packaging)
package.domain = org.ps4app

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,requests

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android Build Tools version
android.build_tools_version = 33.0.2

# (bool) Accept Android SDK licenses automatically
android.accept_sdk_license = True

# (list) List of Android architectures to build for (arm64-v8a هو المعمارية الأسرع للهواتف الحديثة)
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.androidx = true

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable, 1 = enable)
# تم ضبط القيمة إلى 0 لمنع توقف عملية البناء داخل Docker عند التشغيل بصلاحيات الجذر
warn_on_root = 0
