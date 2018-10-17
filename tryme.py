# Sample taken from pyStrich GitHub repository
# https://github.com/mmulqueen/pyStrich
from pystrich.datamatrix import DataMatrixEncoder
encoder = DataMatrixEncoder('RetroMAN')
encoder.save('./datamatrix_test.png')
print(encoder.get_ascii())