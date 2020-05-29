import re
import speech_recognition as sr
import sys
print(sys.executable)
print(sys.version)

for i in sys.modules.keys():
    if re.search("speech", i):
        print(i)

# for i in sys.path:
#     print(i)
#
# git clone <git repo url>
# git add <filename.py>
# git commit -m "type some info here"
# git push

# help(cplex)
