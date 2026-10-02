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
# تم تحديد pip==23.3.1 لتجنب خطأ BuildDependencyInstallError
requirements = python3,kivy,requests,pip==23.3.1

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip hosting a local webserver
android.skip_update = False

# (list) List of Android architectures to build for
# تم الاقتصار على معمارية واحدة لمنع التعارض أثناء البناء
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.androidx = true

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable, 1 = enable)
warn_on_root = 1
