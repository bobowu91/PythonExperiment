import re
import speech_recognition as sr
import sys

print(sys.executable)
print(sys.version)

for i in sys.modules.keys():
    if re.search("speech", i):
        print(i)

for i in dir(sr):
    print(i)

for i in sys.path:
    print(i)

# help(cplex)

'''
pip install - -global-option = 'build_ext'
- -global-option = '-I/usr/local/include'
- -global-option = '-L/usr/local/lib' pyaudio

pip3 install - -global-option = 'build_ext'
- -global-option = '-I/usr/local/Cellar/portaudio/19.6.0/include'
- -global-option = '-L/usr/local/Cellar/portaudio/19.6.0/lib' pyaudio'''

# deal with long string
xxxxxxxxxhfbdbfjdksanfjnsdvckjas = ('ciunrfkjanrjkgfkdslamfasnjakfs'
                                    'nvjkafnvkjndfajvkanfv'
                                    )
print(xxxxxxxxxhfbdbfjdksanfjnsdvckjas)
print(type(xxxxxxxxxhfbdbfjdksanfjnsdvckjas))

# deal with long assignment
# always break the first part after the parenthesis to the next line
# always break the part after comma into the next line to save space
nfajknsdfjanfaddddddnkasnfjdknakjsnfjaksnfjkasndfkksjnf = re.search(
    "nvjkafnvkjndfa",
    xxxxxxxxxhfbdbfjdksanfjnsdvckjas)
print(nfajknsdfjanfaddddddnkasnfjdknakjsnfjaksnfjkasndfkksjnf,
      type(nfajknsdfjanfaddddddnkasnfjdknakjsnfjaksnfjkasndfkksjnf))

if nfajknsdfjanfaddddddnkasnfjdknakjsnfjaksnfjkasndfkksjnf:
    print('true')
else:
    print('false')
