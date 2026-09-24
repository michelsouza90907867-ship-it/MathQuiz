[app]

title = Math Quiz
package.name = mathquiz
package.domain = org.michel
source.dir = .
source.include_exts = py,json
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Permite que o Android ajuste o tamanho da interface
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a

# Nome do arquivo APK
android.presplash_color = #0B1120

[buildozer]

log_level = 2
warn_on_root = 1
