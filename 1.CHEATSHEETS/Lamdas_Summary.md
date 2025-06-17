Absolutely, Hunain! Here's a **complete summary of `lambda` functions** in Python — from the basics to advanced usage like sorting, multiple keys, and comparisons — all in one place 👇

---

# ✅ Python `lambda` Summary

---

## 📌 What is a `lambda`?

A `lambda` is a **small, anonymous function** used for **short, simple tasks**.

### 🧱 Syntax:

```python
lambda arguments: expression
```

### 💡 Example:

```python
square = lambda x: x ** 2
print(square(5))  # ➞ 25
```

Same as:

```python
def square(x):
    return x ** 2
```

---

## 🧰 Common Use Cases for `lambda`

---

### 🔸 Use with `sorted()`:

#### ➤ Sort strings by length:

```python
words = ["kiwi", "apple", "banana"]
sorted(words, key=lambda word: len(word))
# ➞ ['kiwi', 'apple', 'banana']
```

---

### 🔸 Sort custom objects (e.g., `Person`):

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("Bob", 25), Person("Alice", 30)]
sorted(people, key=lambda p: p.age)
```

---

## 📦 `key` parameter (with `sorted`, `min`, `max`)

Functions like `sorted()`, `min()`, and `max()` allow a `key=` argument to define **how to compare items**.

### Example: Find the shortest word

```python
min(["apple", "kiwi", "banana"], key=lambda x: len(x))
# ➞ 'kiwi'
```

---

## 🧠 Sorting by Multiple Values

You can return a tuple in the `lambda` to sort by multiple criteria.

```python
# Sort by name, then by age
sorted(people, key=lambda p: (p.name, p.age))
```

* Python compares tuples **element by element**, left to right.

---

## 🔁 Common Patterns with `lambda`

| Task                      | Lambda Example                            |
| ------------------------- | ----------------------------------------- |
| Square a number           | `lambda x: x ** 2`                        |
| Sort list by length       | `sorted(words, key=lambda w: len(w))`     |
| Sort objects by attribute | `sorted(people, key=lambda p: p.age)`     |
| Sort by multiple fields   | `sorted(items, key=lambda x: (x.a, x.b))` |
| Get closest point         | `min(points, key=lambda p: distance(p))`  |
| Filter even numbers       | `filter(lambda x: x % 2 == 0, nums)`      |
| Map square to numbers     | `map(lambda x: x ** 2, nums)`             |

---

## ⚠️ When *not* to use `lambda`

* When the function logic is too complex — prefer using `def` for clarity.
* When debugging — named functions are easier to trace.

---

## 🧪 Mini Practice Examples

```python
# 1. Sort by string length
sorted(["abc", "a", "abcd"], key=lambda x: len(x))

# 2. Max by distance from (0, 0)
points = [(1, 2), (5, 5), (-2, -1)]
max(points, key=lambda p: (p[0]**2 + p[1]**2)**0.5)

# 3. Sort people by name, then decreasing age
sorted(people, key=lambda p: (p.name, -p.age))
```

---

## ✅ Quick Summary

* `lambda`: creates small anonymous functions.
* `key=`: used to define custom sorting/comparing logic.
* `lambda` is often used with `sorted()`, `min()`, `max()`, `filter()`, `map()`.
* For multi-level sorting: return tuples from the lambda.
* `lambda`s are one-liners — use `def` for anything longer.

---

Let me know if you want this as a PDF or visual chart!
