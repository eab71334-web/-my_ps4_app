[app]

# (str) Title of your application
title = My PS4 App

# (str) Package name
package.name = my_ps4_app

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# تم تحديد إصدار pip مستقر وحذف حزمة android لتجنب التعارض
requirements = python3,kivy,requests,pip==23.3.1

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android Build Tools version
# هذا السطر يمنع التحديث التلقائي إلى إصدار Build-Tools 37 غير المستقر
android.build_tools_version = 33.0.2

# (bool) Accept Android SDK licenses automatically
android.accept_sdk_license = True

# (list) List of Android architectures to build for
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.androidx = true

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable, 1 = enable)
warn_on_root = 1
