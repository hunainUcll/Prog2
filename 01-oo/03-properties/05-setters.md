# Setters

As of yet, we have only defined getter methods, i.e., methods that tell Python what to do when the user *reads* from a property.
We will now take a look at *setter methods*, which are called whenever a user *writes* to a property.

Let's go back to our old version of the `Person` class:

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age
```

In this version, changes are disallowed.
Let's say we want to allow the user to make arbitrary changes to `age`, as long as the `age` is set to a positive number.

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        ???
```

We added another `age` method, but this one has `@age.setter` in front of it.
This tells Python that it's the `age`'s setter method.
The `value` parameter (you can choose whichever name you like, but as always, keep it descriptive) is the value the user is trying to assign to `age`.

```python
person = Person(18)
person.age = 19
```

This code would call the `age` setter with `value` set to `19`.

A simple implementation for the setter would be

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
```

Okay, this works, but it doesn't do anything special.
In fact, this implementation works exactly the same as if you simply made `age` a regular public attribute.
No need for properties.

However, we want to add some intelligence to it: we want to allow only positive ages.
Let's add an `if` to the setter.

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('age must be positive')
        self.__age = value
```

As you can see, the setter will loudly complain when `value < 0`:

```text
>>> person = Person(20)
>>> person.age
20

>>> person.age = 21
>>> person.age
21

>>> person.age = -1
ValueError: age must be positive
>>> person.age
21
```

## Fixing the Constructor

The above code contains a glaring flaw:

```python
>>> person = Person(-20)
>>> person.age
-20
```

The constructor doesn't check the age, so it _is_ possible to have `Person` objects with invalid ages.
It's like a hole in `Person` that we need to fix.

```python
class Person:
    def __init__(self, age):
        if age < 0:
            raise ValueError('age must be positive')
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('age must be positive')
        self.__age = value
```

This works, but you should immediately notice the duplication of logic: both the constructor and the `age` setter contain the same logic.
Such repetition needs to be avoided, so we rewrite it as

```python
class Person:
    def __init__(self, age):
        self.age = age       # Calls age's setter

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('age must be positive')
        self.__age = value
```

This pattern is quite common in code: you will have one gatekeeper (the one who knows the rules and has direct access) and everyone else should delegate to this gatekeeper.
Here, the `age` setter is the gatekeeper to `__age`.
The constructor wants to set `__age` but needs to have the discipline to go through the `age` setter.
If other methods were to be added that need to modify the age, they should all rely on the `age` setter.
