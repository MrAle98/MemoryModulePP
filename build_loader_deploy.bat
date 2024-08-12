python convertToBuf.py %1
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" x86_amd64
msbuild MemoryModulePP.sln -t:test /property:Configuration=Release