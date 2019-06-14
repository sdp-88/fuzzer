file_list = [ 
    "test1.pdf",
    "test2.pdf"
    ]
apps = [
    "C:\Program Files (x86)\Adobe\Acrobat 9.0\Acrobat\Acrobat.exe"
    ]

fuzz_output = "fuzz.pdf"

FuzzFactor = 250
num_tests = 10000

#end of configuration

import math
import random
import string
import subprocess
import time

for i in range(num_tests):
    file_choice = random.choice(file_list)
    app = random.choice(apps)

    buf = bytearray(open(file_choice, "rb").read())

    numwrites = random.randrange(math.ceil((float(len(buf)) / FuzzFactor))) + 1

for j in range(numwrites):
    rbyte = random.randrange(256)
    rn = random.randrange(len(buf))
    buf[rn] = rbyte
    

    open(fuzz_output,"wb").write(buf)

    process = subprocess.Popen([app, fuzz_output])

    time.sleep(1)
    crashed = process.poll()
    if not crashed:
        process.terminate()
