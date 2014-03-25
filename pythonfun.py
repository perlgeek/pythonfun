# cleanup[2] _abcoll
# cleanup[2] genericpath
# cleanup[2] stat
# cleanup[2] _ssl
# cleanup[2] pyreadline.modes.vi
# cleanup[2] warnings
# cleanup[2] glob
# cleanup[2] pyreadline.error
# cleanup[2] types
# cleanup[2] time
# cleanup[2] pyreadline.release
# cleanup[2] pyreadline.modes
# cleanup sys
# cleanup __builtin__
# cleanup ints: 943 unfreed ints
# cleanup floats: 37 unfreed floats

C:\Users\weems>python math.[i
python: can't open file 'math.[i': [Errno 2] No such file or directory

C:\Users\weems>python (math.pi)
python: can't open file '(math.pi)': [Errno 2] No such file or directory

C:\Users\weems>python
Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win
32
Type "help", "copyright", "credits" or "license" for more information.
>>> math.pi
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
>>> import mmath
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named mmath
>>> import math
>>> math.pi
3.141592653589793
>>> dir(math)
['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan',
 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'er
fc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gam
ma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'mod
f', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'math']
>>> name = "Bob"
>>> import math
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'math', 'name']
>>> math
<module 'math' (built-in)>
>>> dir(math)
['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan',
 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'er
fc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gam
ma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'mod
f', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> print __name__
__main__
>>> print math.__name__
math
>>> print math.__doc__
This module is always available.  It provides access to the
mathematical functions defined by the C standard.
>>> math.pi
3.141592653589793
>>> "Hello World!"[0]
'H'
>>> "Hello World!"[1]
'e'
>>> "Hello World!"[2]
'l'
>>> "Hello World!"[3]
'l'
>>> "Hello World!"[4]
'o'
>>> "Hello World!"[5]
' '
>>> "Hello World!"[6]
'W'
>>> "Hello World!"[7]
'o'
>>> "Hello World!"[8]
'r'
>>> "Hello World!"[9]
'l'
>>> "Hello World!"[10]
'd'
>>> "Hello World!"[11]
'!'
>>> "Hello World!"[12]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> "Hello World!"[-2]
'd'
>>> "Hello World!"[-9]
'l'
>>> "Hello World!"[-13]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> "Hello World!"[-1]
'!'
>>> "Hello World!"[3:9]
'lo Wor'
>>> "Hello World!"[:5]
'Hello'
>>> "Hello World!"[-6:-1]
'World'
>>> "Hello World!"[-9:]
'lo World!'
>>> "Hello World!"[:-8]
'Hell'
>>> "Hello World!"[:]
'Hello World!'
>>> spam ['bacon' , 'eggs', 42]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> spam =  ['bacon' , 'eggs', 42]
>>> spam
['bacon', 'eggs', 42]
>>> spam[0]
'bacon'
>>> spam[1]
'eggs'
>>> spam[2]
42
>>> spam[-1]
42
>>> spam[-2]
'eggs'
>>> spam[-3]
'bacon'
>>> len(spam)
3
>>> spam = ["bacon", "eggs", 42 ]
>>> spam
['bacon', 'eggs', 42]
>>> spam[1]
'eggs'
>>> spam[2]
42
>>> spam[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> spam[0]
'bacon'
>>> spam[1] = "ketchup"
>>> spam
['bacon', 'ketchup', 42]
>>> spam[1:]
['ketchup', 42]
>>> spam[:-1]
['bacon', 'ketchup']
>>> spam.append(10)
>>> spam
['bacon', 'ketchup', 42, 10]
>>> spam[4] = 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> spam.insert(1, 'and')
>>> spam
['bacon', 'and', 'ketchup', 42, 10]
>>> spam
['bacon', 'and', 'ketchup', 42, 10]
>>> del spam[1]
>>> spam
['bacon', 'ketchup', 42, 10]
>>> spam[0]
'bacon'
>>> spam[1]
'ketchup'
>>> spam[2]
42
>>> spam[3]
10
>>> a = [2,3,4,5]
>>> b = a
>>> del a[3]
>>> print a
[2, 3, 4]
>>> print b
[2, 3, 4]
>>> a = [2,3,4,5]
>>> b=a[:]
>>> del a[3]
>>> print a
[2, 3, 4]
>>> print b
[2, 3, 4, 5]
>>> unchanging = "rocks", 0, "the universe"
>>> foo, bar = "rocks", 0, "the universe"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack
>>> foo, bar = "rocks", (0, "the universe")
>>> var = "me", "you", "us", "them"
>>> var = ("me", "you", "us", "them")
>>> print var
('me', 'you', 'us', 'them')
>>> var = ("me", "you", ("us", "them"))
>>> print(var)
('me', 'you', ('us', 'them'))
>>> definitions = {"guava: "a tropical fruit", "python": "a programming language
", "the answer": 42}
  File "<stdin>", line 1
    definitions = {"guava: "a tropical fruit", "python": "a programming language
", "the answer": 42}
                            ^
SyntaxError: invalid syntax
>>> definitions = {"guava": "a tropical fruit", "python": "a programming languag
>>> definitions
{'python': 'a programming language', 'the answer': 42, 'guava': 'a tropical frui
t'}
>>> definitions["the answer"]
42
>>> definitions["guava"]
'a tropical fruit'
>>> len(definitions)
3
>>> definitions["new key"]= "new value"
>>> del definitions["new key"]
>>> definitions
{'python': 'a programming language', 'the answer': 42, 'guava': 'a tropical frui
t'}
>>> mind = set([42, 'a string', (23, 4)])
>>> mind
set([(23, 4), 42, 'a string'])
>>> mind = set([42, 'a string', 40, 0])
>>> mind
set([40, 0, 42, 'a string'])
>>> mind.add('hello')
>>> mind
set([40, 0, 42, 'a string', 'hello'])
>>> mind.add('duplicate value")
  File "<stdin>", line 1
    mind.add('duplicate value")
                              ^
SyntaxError: EOL while scanning string literal
>>> mind.add('duplicate value")
  File "<stdin>", line 1
    mind.add('duplicate value")
                              ^
SyntaxError: EOL while scanning string literal
>>> mind
set([40, 0, 42, 'a string', 'hello'])
>>> mind.add('duplicate value')
>>> mind.add('duplicate value')
>>> mind
set([0, 'a string', 40, 42, 'hello', 'duplicate value'])
>>> frozen = frozenset(['life', 'universe', 'everything'])
>>> frozen
frozenset(['universe', 'life', 'everything'])
>>> frozen = frozenset({'life', 'universe', 'everything'})
>>> frozen
frozenset(['everything', 'life', 'universe'])
>>> frozen = frozenset(['life', 'universe', 'everything'])
>>> frozen
frozenset(['universe', 'life', 'everything'])
>>> name = [5, 10, "twenty"]
>>> del name = [10]
  File "<stdin>", line 1
    del name = [10]
             ^
SyntaxError: invalid syntax
>>> del name [10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> del name 10
  File "<stdin>", line 1
    del name 10
              ^
SyntaxError: invalid syntax
>>> del name[1]
>>> name
[5, 'twenty']
>>> name = 5, 10, "twenty"
>>> name = set([5, 10, "twenty"])
>>> name
set(['twenty', 10, 5])
>>> nametwo = set(["twenty", 10, 5])
>>> print nametwo, name
set(['twenty', 10, 5]) set(['twenty', 10, 5])
>>> days = "Monday", "Tuesday", frozenset(["Wednesday"])
>>> print days
('Monday', 'Tuesday', frozenset(['Wednesday']))
>>> print days, name, nametwo, mind, frozen
('Monday', 'Tuesday', frozenset(['Wednesday'])) set(['twenty', 10, 5]) set(['twe
>>> f = open('code','r+')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: [Errno 2] No such file or directory: 'code'
>>>
