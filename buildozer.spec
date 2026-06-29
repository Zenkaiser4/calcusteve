[app]

# (str) Title of your application
title = Calculadora

# (str) Package name
package.name = calculadora

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,kivymd,pillow

# (str) Presplash of the application
presplash.filename = %(source.dir)s/calcu.png

# (str) Icon of the application
icon.filename = %(source.dir)s/calcu.png

# (list) Supported orientations
orientation = portrait

#
# OSX Specific
#

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 2.3.0

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API. Subimos a la 34 que es el estándar actual compatible.
android.api = 34

# (int) Minimum API your APK / AAB will support.
android.minapi = 24

# (str) Android NDK version to use. Cambiado a la versión 27b (Evita que busque el sdkmanager antiguo)
android.ndk = 27b

# (int) Android NDK API to use. Debe coincidir habitualmente con minapi o ser superior.
android.ndk_api = 24

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (bool) Enable AndroidX support. ¡OBLIGATORIO PARA KIVYMD!
android.enable_androidx = True

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True

#
# iOS specific
#

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0

# (bool) Whether or not to sign the code
ios.codesign.allowed = false


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
