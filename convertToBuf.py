import sys
f = open("./test/buf.h","w",newline="\r\n")
f2 = open(sys.argv[1],"rb")
bytes = f2.read()
stringa = f"#pragma once\nunsigned char buf[{len(bytes)}] = {{"
for i in bytes:
    stringa += f"{int(i)},"
stringa = stringa[:-1]
stringa += "};"
f.write(stringa)
f.close()
