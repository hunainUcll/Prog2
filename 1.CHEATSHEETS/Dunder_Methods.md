Here is a complete Markdown file content explaining **Python dunder (magic) methods**, organized by category, with tables and code examples:

---

# 🔍 Python Dunder Methods (Magic Methods) Explained

Dunder methods (short for “**double underscore**”) let you define how your custom objects behave with built-in Python syntax and operations like printing, addition, comparison, iteration, etc.

---

## 🔧 Object Construction & Initialization

| Method      | Purpose                                              |
|-------------|------------------------------------------------------|
| `__new__`   | Creates a new instance (used rarely)                 |
| `__init__`  | Initializes the object after creation                |
| `__del__`   | Called when object is deleted                        |

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} is being deleted.")
````

---

## 📦 Object Representation

| Method     | Purpose                                   |
| ---------- | ----------------------------------------- |
| `__str__`  | Human-readable string (used by `print()`) |
| `__repr__` | Developer string (used in debugging)      |

```python
class Dog:
    def __repr__(self):
        return "Dog()"

    def __str__(self):
        return "A friendly dog"
```

---

## ⚖️ Comparison Operators

| Method   | Operator |
| -------- | -------- |
| `__eq__` | `==`     |
| `__ne__` | `!=`     |
| `__lt__` | `<`      |
| `__le__` | `<=`     |
| `__gt__` | `>`      |
| `__ge__` | `>=`     |

```python
class Box:
    def __init__(self, volume):
        self.volume = volume

    def __lt__(self, other):
        return self.volume < other.volume
```

---

## ➕ Arithmetic Operators

| Method         | Operator |
| -------------- | -------- |
| `__add__`      | `+`      |
| `__sub__`      | `-`      |
| `__mul__`      | `*`      |
| `__truediv__`  | `/`      |
| `__floordiv__` | `//`     |
| `__mod__`      | `%`      |
| `__pow__`      | `**`     |

Also:

* `__radd__`, `__rsub__`, etc. → right-hand side fallback
* `__iadd__`, `__isub__`, etc. → in-place (e.g. `+=`)

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)
```

---

## 🧱 Unary Operators

| Method       | Operator |
| ------------ | -------- |
| `__neg__`    | `-x`     |
| `__pos__`    | `+x`     |
| `__abs__`    | `abs(x)` |
| `__invert__` | `~x`     |

---

## 📚 Collection Emulation

| Method         | Purpose            |
| -------------- | ------------------ |
| `__len__`      | `len(obj)`         |
| `__getitem__`  | `obj[key]`         |
| `__setitem__`  | `obj[key] = value` |
| `__delitem__`  | `del obj[key]`     |
| `__contains__` | `item in obj`      |

```python
class MyList:
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __len__(self):
        return len(self.data)
```

---

## 🔁 Iteration & Context Management

| Method      | Purpose               |
| ----------- | --------------------- |
| `__iter__`  | Returns iterator      |
| `__next__`  | Returns next element  |
| `__enter__` | Context manager start |
| `__exit__`  | Context manager end   |

```python
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        return self.count
```

```python
class FileOpener:
    def __enter__(self):
        self.file = open("test.txt", "r")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
```

---

## 🧪 Callable, Boolean, and Hashing

| Method     | Purpose                    |
| ---------- | -------------------------- |
| `__call__` | Make instance callable     |
| `__bool__` | Boolean context (`if obj`) |
| `__hash__` | Hashable for sets/dicts    |

```python
class Greeter:
    def __call__(self, name):
        return f"Hello, {name}!"
```

---

## 🎯 Attribute Access

| Method             | Purpose                           |
| ------------------ | --------------------------------- |
| `__getattr__`      | Accessing missing attributes      |
| `__getattribute__` | Intercepts *all* attribute access |
| `__setattr__`      | Called on attribute assignment    |
| `__delattr__`      | Called on attribute deletion      |

```python
class Person:
    def __getattr__(self, name):
        return f"{name} is unknown"
```

---

