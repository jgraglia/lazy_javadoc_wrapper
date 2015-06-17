from subprocess import call
import sys
import os
print "Hacking javadoc param : disabling doclint verifications"
currentfolder = os.path.dirname(sys.argv[0])
base = [currentfolder+"\javadocX.exe", "-Xdoclint:none"]
cmdWithOrigArgs = base + sys.argv[1:]
print "Cmd as array:"
print(cmdWithOrigArgs)
print "Cmd: " +" ".join(cmdWithOrigArgs)

call(cmdWithOrigArgs, shell=True)