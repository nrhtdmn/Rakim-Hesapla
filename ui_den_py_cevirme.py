from PyQt5 import uic

with open("rakim_hesaplama_ui.py","w",encoding="utf-8") as fout:
    uic.compileUi("rakim_hesaplama.ui",fout)


