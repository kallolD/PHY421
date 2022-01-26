# Python3

## Features
- Interpreted language
- High level language. Easy to get into and start coding
- Object oriented language
- Vast array of free and open source resources. You can find a python code for just about anything.
- Helpful community. Numerous forums to ask questions. Beginner friendly as well. 
___and most importantly,___
- Extemely popular in scientific sector. Most new scientific codes/programs are written in python, and these are generally open source and available on github or gitlab. Even leagacy FORTRAN and C codes are being translated to python.


## Writing a python code
Python codes are text files with the extension __.py__. Create a new text file and name it as __*something*.py__. In order to edit this file, open up a text editor. If you are on a Ubuntu, you can use the inbuilt text editor *gedit*. On windows, you can use notepad. In addtion, there are a lot of other text editors that offer features like text completion, syntax highlighting and extensibilty. Some popular ones are _sublime text_, _vim_, _emacs_ and _atom_.

You can also use IDEs (Integrated development environments). These offer a lot more than simple editors. They are, however, _heavier_ on the available resources compared to simple text editors.

## Running python code
You can execute a python code by going to the terminal and executing
```sh
$ python3 code.py
```

## Comments in code
You can comment out a line in the code (make it so that the computer does not try to execute that line) by adding a hash (#) symbol.
```python
x = ['Alice', 'Bob', 'Charlie']
# This is an example of a comment
print(x)
```
In the above snippet, the 2nd line will be overlooked while execution. To comment out large sections of code, encase the segment within triple quotes.
```python
x = ['Alice', 'Bob', 'Charlie']
'''
for i in range(len(x)):
    print(x[i])
'''
print(x)
```







