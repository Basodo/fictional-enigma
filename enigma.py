#main file. vanuit hier worden alle losse functies aangeroepen

from lamps import translate
from caesar_encrypt import caesar_cipher
from keyboard import vercijfer
from filter import filter
from plugboard import plugtest
from rotors import rotor1


vercijfer()
filter()
#caesar_cipher(3)
plugtest()
rotor1()
translate()
