# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from PyQt5 import uic

with open('formUI.py', 'w', encoding="utf-8") as fout:
    uic.compileUi('form.ui', fout)
