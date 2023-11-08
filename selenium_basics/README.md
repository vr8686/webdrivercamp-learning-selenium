# Assignment Selenium

This directory contains completed assignments "Selenium" and "Python - Classes". 
All exercises performed in PyCharm editor.

## Contents

- All the finished exercises of assigment "Selenium" are in the file [search.py](./search.py)

**Python - Classes finished assignments**

- Exercise 5. Check the object: file [5_check_obj.py](./5_check_obj.py)
- Exercise 6. What is available?: file [6_available_attr.py](./6_available_attr.py)
- Exercise 700. Is it exact same object?: file [700_check_exact_obj.py](./700_check_exact_obj.py)
- Exercise 800. Was it inherited?: file [800_check_if_inherited.py](./800_check_if_inherited.py)

## Tasks for "Selenium" assigment

1. **Open Browser:**
  * Navigate to URL ( www.ebay.com )
  * Print URL
  * Close browser
2. **Add wait:**
  * Navigate to URL ( www.ebay.com )
  * WebDriverWait -  Waiting for the page to load 
  * Print URL
  * Close browser
3. **Search items:**
  * Navigate to URL ( www.ebay.com )
  * WebDriverWait -  Waiting for the page to load 
  * Print URL
  * Type “women watch” into search field
  * Press search
  * Close browser
4. **Verify the search results:**
  * Navigate to URL ( www.ebay.com )
  * WebDriverWait -  Waiting for the page to load 
  * Print URL
  * Type “women watch” into search field
  * Press search
  * Verify the header contains “results for women watch“
  * Close browser

## Comments

Printed extra messages to make the output more informative.
```python
...
print('Waiting for the page to load...')
...
print(f"The page has been loaded. Current url is: {driver.current_url}")
...
print(f"Searching for \"{search_input}\"...")
...
print(f"Found in header: {header_text}")
...
print('Verified. The header contains “results for women watch“')
...
```

## Tasks for "Python - Classes" assigment

5. **Check the object**

Write a function that checks if the object is an instance of a class (`class_`), or if the object is an instance of a class that (`class_`) inherited from.
 * Return `True` or `False` (if not an instance)
```python
 $ cat 5_check_obj.py
def check_obj(obj, class_):
    # YOUR CODE HERE

if __name__ == "__main__":
    from components.filter import LeftFilter
    from components import base
    
    class Base:
        pass

    another_base = Base()
    some_list = [1, 2]
    left_filter = LeftFilter("")
    
    for x in [another_base, some_list, left_filter]:
        if check_obj(x, int):
            print(f"{x} is from class {int.__name__}")
        if check_obj(x, list):
            print(f"{x} is from class {list.__name__}")
        if check_obj(x, Base):
            print(f"{x} is from class {Base.__name__}")
        if check_obj(x, LeftFilter):
            print(f"{x} is from class {LeftFilter.__name__}")
        if check_obj(x, object):
            print(f"{x} is from class {object.__name__}")
        if check_obj(x, base.Base):
            print(f"{x} is from class {base.Base.__name__}")
        print(f"{'':.^20}")
```
6. **What is available?**

Print the list of available attributes and methods of an object
```python
 $ cat 6_available_attr.py
from selenium import webdriver
from components.filter import LeftFilter

driver = webdriver.Chrome
left_filter = LeftFilter(driver)

# YOUR CODE HERE
 $
```
700. **Is it exact same object?**

Write a function that checks if the object is **exactly** an instance of the specified class

* Return `True` or `False`
```python
 $ cat 700_check_exact_obj.py
def check_exact_obj(obj, class_):
  # YOUR CODE HERE

if __name__=="__main__":
    class Base:
        pass

    b = Base()
    i = [1, 2]
    for x in [b, i]:

        if check_exact_obj(x, int):
            print(f"{x} is an instance of class {int.__name__}")
        if check_exact_obj(x, list):
            print(f"{x} is an instance of class {list.__name__}")
        if check_exact_obj(x, Base):
            print(f"{x} is an instance of class {Base.__name__}")
        if check_exact_obj(x, object):
            print(f"{x} is an instance of class {object.__name__}")
 $
```

800. **Was it inherited?**

Write a function that checks if the object is an instance of a class that inherited (directly or indirectly) from the specified class
* Return True or False
```python
 $ cat 800_check_if_inherited.py
def check_inheritance(obj, class_):
    # YOUR CODE HERE

if __name__=="__main__":
    class Base:
        pass

    a = Base()
    b = [1, 2]
    c = False
    for x in [a, b, c]:

        if check_inheritance(x, int):
            print(f"{x} was inherited from {int.__name__}")
        if check_inheritance(x, list):
            print(f"{x} was inherited from {list.__name__}")
        if check_inheritance(x, Base):
            print(f"{x} was inherited from {Base.__name__}")
        if check_inheritance(x, object):
            print(f"{x} was inherited from {object.__name__}")
 $
```
