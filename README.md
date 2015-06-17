# Why
Wrap original javadoc.exe process and append *-Xdoclint:none* option

Use py2exe (http://www.py2exe.org/) to generate a javadoc.exe file that automatically append -Xdoclint:none option.

Created in order to use a JDK8 with Matlab mcc process.

http://blog.joda.org/2014/02/turning-off-doclint-in-jdk-8-javadoc.html

# Build

Requires **python 2.7** ! (py2exe requirement)

```
python.exe setup.py py2exe
```
