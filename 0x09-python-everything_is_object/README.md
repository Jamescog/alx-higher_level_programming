# Everything is object

This project contains some tasks for learning about object behaviours in **Python**.

## Tasks To Complete

+ [x] 0\. Who am I? <br/>_**[0-answer.txt](0-answer.txt)**_ contains the function I would use to print the type of an object.
+ [x] 1\. Where are you? <br/>_**[1-answer.txt](1-answer.txt)**_ contains the function I would use to get the variable identifier (which is the memory address in the CPython implementation).
+ [x] 2\. Right count <br/>_**[2-answer.txt](2-answer.txt)**_ contains the answer to if `a` and `b` point to the same object in the following code (`Yes` / `No`).
  ```python
  >>> a = 89
  >>> b = 100
  ```
+ [x] 3\. Right count = <br/>_**[3-answer.txt](3-answer.txt)**_ contains the answer to if `a` and `b` point to the same object in the following code (`Yes` / `No`).
  ```python
  >>> a = 89
  >>> b = 89
  ```
+ [x] 4\. Right count = <br/>_**[4-answer.txt](4-answer.txt)**_ contains the answer to if `a` and `b` point to the same object in the following code (`Yes` / `No`).
  ```python
  >>> a = 89
  >>> b = a
  ```
+ [x] 5\. Right count =+ <br/>_**[5-answer.txt](5-answer.txt)**_ contains the answer to if `a` and `b` point to the same object in the following code (`Yes` / `No`).
  ```python
  >>> a = 89
  >>> b = a + 1
  ```
+ [x] 6\. Is equal <br/>_**[6-answer.txt](6-answer.txt)**_ contains the output of the following code.
  ```python
  >>> s1 = "Best School"
  >>> s2 = s1
  >>> print(s1 == s2)
  ```
+ [x] 7\. Is the same <br/>_**[7-answer.txt](7-answer.txt)**_ contains the output of the following code.
  ```python
  >>> s1 = "Best"
  >>> s2 = s1
  >>> print(s1 is s2)
  ```
+ [x] 8\. Is really equal <br/>_**[8-answer.txt](8-answer.txt)**_ contains the output of the following code.
  ```python
  >>> s1 = "Best School"
  >>> s2 = "Best School"
  >>> print(s1 == s2)
  ```
+ [x] 9\. Is really the same <br/>_**[9-answer.txt](9-answer.txt)**_ contains the output of the following code.
  ```python
  >>> s1 = "Best School"
  >>> s2 = "Best School"
  >>> print(s1 is s2)
  ```
+ [x] 10\. And with a list, is it equal <br/>_**[10-answer.txt](10-answer.txt)**_ contains the output of the following code.
  ```python
  >>> l1 = [1, 2, 3]
  >>> l2 = [1, 2, 3]
  >>> print(l1 == l2)
  ```
+ [x] 11\. And with a list, is it the same <br/>_**[11-answer.txt](11-answer.txt)**_ contains the output of the following code.
  ```python
  >>> l1 = [1, 2, 3]
  >>> l2 = [1, 2, 3]
  >>> print(l1 is l2)
  ```
+ [x] 12\. And with a list, is it really equal <br/>_**[12-answer.txt](12-answer.txt)**_ contains the output of the following code.
  ```python
  >>> l1 = [1, 2, 3]
  >>> l2 = l1
  >>> print(l1 == l2)
  ```
+ [x] 13\. And with a list, is it really the same <br/>_**[13-answer.txt](13-answer.txt)**_ contains the output of the following code.
  ```python
  >>> l1 = [1, 2, 3]
  >>> l2 = l1
  >>> print(l1 is l2)
  ```
+ [x] 14\. List append <br/>_**[14-answer.txt](14-answer.txt)**_ contains the output of the following code.
  ```python
  l1 = [1, 2, 3]
  l2 = l1
  l1.append(4)
  print(l2)
  ```
+ [x] 15\. List add <br/>_**[15-answer.txt](15-answer.txt)**_ contains the output of the following code.
  ```python
  l1 = [1, 2, 3]
  l2 = l1
  l1 = l1 + [4]
  print(l2)
  ```
+ [x] 16\. Integer incrementation <br/>_**[16-answer.txt](16-answer.txt)**_ contains the output of the following code.
  ```python
  def increment(n):
      n += 1

  a = 1
  increment(a)
  print(a)
  ```
+ [x] 17\. List incrementation <br/>_**[17-answer.txt](17-answer.txt)**_ contains the output of the following code.
  ```python
  def increment(n):
      n.append(4)

  l = [1, 2, 3]
  increment(l)
  print(l)
  ```
+ [x] 18\. List assignation <br/>_**[18-answer.txt](18-answer.txt)**_ contains the output of the following code.
  ```python
  def assign_value(n, v):
      n = v

  l1 = [1, 2, 3]
  l2 = [4, 5, 6]
  assign_value(l1, l2)
  print(l1)
  ```
+ [x] 19\. Copy a list object <br/>_**[19-copy_list.py](19-copy_list.py)**_ contains a function that returns a copy of a list.
+ [x] 20\. Tuple or not? <br/>_**[20-answer.txt](20-answer.txt)**_ contains the answer to if `a` is a tuple or not (`Yes` / `No`).
  ```python
  a = ()
  ```
+ [x] 21\. Tuple or not? <br/>_**[21-answer.txt](21-answer.txt)**_ contains the answer to if `a` is a tuple or not (`Yes` / `No`).
  ```python
  a = (1, 2)
  ```
+ [x] 22\. Tuple or not? <br/>_**[22-answer.txt](22-answer.txt)**_ contains the answer to if `a` is a tuple or not (`Yes` / `No`).
  ```python
  a = (1)
  ```
+ [x] 23\. Tuple or not? <br/>_**[23-answer.txt](23-answer.txt)**_ contains the answer to if `a` is a tuple or not (`Yes` / `No`).
  ```python
  a = (1, )
  ```
+ [x] 24\. Who I am? <br/>_**[24-answer.txt](24-answer.txt)**_ contains the output of the following code.
  ```python
  a = (1)
  b = (1)
  a is b
  ```
+ [x] 25\. Tuple or not <br/>_**[25-answer.txt](25-answer.txt)**_ contains the output of the following code.
  ```python
  a = (1, 2)
  b = (1, 2)
  a is b
  ```
+ [x] 26\. Empty is not empty <br/>_**[26-answer.txt](26-answer.txt)**_ contains the output of the following code.
  ```python
  a = ()
  b = ()
  a is b
  ```
+ [x] 27\. Still the same? <br/>_**[27-answer.txt](27-answer.txt)**_ contains the answer to if the last line of the following script will print `139926795932424` (`Yes` / `No`).
  ```python
  >>> id(a)
  139926795932424
  >>> a
  [1, 2, 3, 4]
  >>> a = a + [5]
  >>> id(a)
  ```
+ [x] 28\. Same or not? <br/>_**[28-answer.txt](28-answer.txt)**_ contains the answer to if the last line of the following script will print `139926795932424` (`Yes` / `No`).
  ```python
  >>> a
  [1, 2, 3]
  >>> id (a)
  139926795932424
  >>> a += [4]
  >>> id(a)
  ```
+ [x] 29\. #pythonic <br/>_**[100-magic_string.py](100-magic_string.py)**_ contains a function that returns a string “BestSchool” n times the number of the iteration.
+ [x] 30\. Low memory cost <br/>_**[101-locked_class.py](101-locked_class.py)**_ contains a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`.
+ [x] 31\. int 1/3 <br/>Considering the script below and assuming we are using a CPython implementation of Python3 with default options/configuration:
  ```python
  a = 1
  b = 1
  ```
  + _**[103-line1.txt](103-line1.txt)**_ Contains the answer to how many int objects are created by the execution of the first line of the script.
  + _**[103-line2.txt](103-line2.txt)**_ Contains the answer to how many int objects are created by the execution of the second line of the script.
+ [x] 32\. int 2/3 <br/>Considering the script below and assuming we are using a CPython implementation of Python3 with default options/configuration:
  ```python
  a = 1024
  b = 1024
  del a
  del b
  c = 1024
  ```
  + _**[104-line1.txt](104-line1.txt)**_ Contains the answer to how many int objects are created by the execution of the first line of the script.
  + _**[104-line2.txt](104-line2.txt)**_ Contains the answer to how many int objects are created by the execution of the second line of the script.
  + _**[104-line3.txt](104-line3.txt)**_ Contains the answer to if the int object pointed by `a` is deleted after the execution of line 3 in the script (`Yes` / `No`).
  + _**[104-line4.txt](104-line4.txt)**_ Contains the answer to if the int object pointed by `b` is deleted after the execution of line 4 in the script (`Yes` / `No`).
  + _**[104-line5.txt](104-line5.txt)**_ Contains the answer to how many int objects are created by the execution of the last line of the script.
+ [x] 33\. int 3/3 <br/>Considering the script below and assuming we are using a CPython implementation of Python3 with default options/configuration:
  ```python
  print("I")
  print("Love")
  print("Python")
  ```
  + _**[105-line1.txt](105-line1.txt)**_ Contains the answer to how many int objects have been created and are still in memory before the execution of line in the script (`print("Love")`).
  + _**[105-blog_post.md](105-blog_post.md)**_ Contains the blog post of an explanation of the answer.
+ [x] 34\. Clear strings <br/>Considering the script below and assuming we are using a CPython implementation of Python3 with default options/configuration:
  ```python
  a = "SCHL"
  b = "SCHL"
  del a
  del b
  c = "SCHL"
  ```
  + _**[106-line1.txt](106-line1.txt)**_ Contains the answer to how many string objects are created by the execution of the first line of the script.
  + _**[106-line2.txt](106-line2.txt)**_ Contains the answer to how many string objects are created by the execution of the second line of the script.
  + _**[106-line3.txt](106-line3.txt)**_ Contains the answer to if the string object pointed by `a` is deleted after the execution of line 3 in the script (`Yes` / `No`).
  + _**[106-line4.txt](106-line4.txt)**_ Contains the answer to if the string object pointed by `b` is deleted after the execution of line 4 in the script (`Yes` / `No`).
  + _**[106-line5.txt](106-line5.txt)**_ Contains the answer to how many string objects are created by the execution of the last line of the script.
