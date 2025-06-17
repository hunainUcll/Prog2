# 🧠 Python `re` Regex Cheat Sheet

This cheat sheet summarizes key `re` functions and regex patterns useful for string validation and matching. Perfect for exams!

---

## ✅ `re` Function Summary

### 1. `re.fullmatch(pattern, string)`
- Matches the **entire string** against the pattern.

### 2. `re.search(pattern, string)`
- Matches **any part** of the string.

### 3. `re.match(pattern, string)`
- Matches from the **beginning** of the string.

---

## 🔣 Regex Symbol Reference

| Pattern         | Meaning                                                                 |
|----------------|-------------------------------------------------------------------------|
| `.`            | Any single character (except newline)                                   |
| `*`            | Zero or more times (greedy)                                             |
| `+`            | One or more times                                                       |
| `?`            | Zero or one time                                                        |
| `{N}`          | Exactly N times                                                         |
| `{N,}`         | At least N times                                                        |
| `{N,M}`        | Between N and M times                                                   |
| `[...]`        | Match any character inside                                              |
| `[^...]`       | Match any character **not** inside                                      |
| `[a-z]`        | Lowercase letters                                                       |
| `[A-Z]`        | Uppercase letters                                                       |
| `[0-9]` or `\d`| Digits                                                                 |
| `\D`          | Non-digit characters                                                    |
| `\w`          | Word characters (letters, digits, underscore)                           |
| `\W`          | Non-word characters                                                     |
| `\s`          | Whitespace characters                                                   |
| `\S`          | Non-whitespace characters                                               |
| `\.`          | A literal dot                                                           |
| `^`            | Start of string                                                         |
| `$`            | End of string                                                           |
| `|`            | Alternation: either left or right side                                  |
| `(abc)`        | Capturing group                                                         |
| `\1`, `\2`   | Backreferences to previous groups                                        |
| `(?=...)`      | Lookahead                                                               |
| `(?!...)`      | Negative lookahead                                                      |

---

## 🎯 Common Use Cases

| Goal                             | Regex Example                         | Description                                  |
|----------------------------------|----------------------------------------|----------------------------------------------|
| Exactly 3 times `abc`            | `(abc){3}`                             | Matches `abcabcabc`                          |
| 3 to 10 times `abc`             | `(abc){3,10}`                          | From 3 to 10 repetitions                     |
| 10 or more times `abc`          | `(abc){10,}`                           | At least 10 times                            |
| Zero or more `abc`              | `(abc)*`                               | Optional or repeated                         |
| Match `abc` or `xyz`            | `(abc|xyz)`                            | Either `abc` or `xyz`                        |
| Only vowels                     | `([aeiouAEIOU])*`                      | Any number of vowels only                    |
| Only letters                    | `[a-zA-Z]*`                            | Only uppercase or lowercase letters          |
| At least 3 digits               | `(.*\d.*){3,}`                        | At least 3 digits in total                   |
| Starts with `a`                 | `^a`                                   | Begins with `a`                              |
| Valid number                    | `\d+(\.\d+)?`                       | Digits, optional decimal part                |
| Student ID (s1234567)           | `[sSrR][0-9]{7,}`                      | Starts with s/r and 7+ digits                |
| Repeated 3x pattern             | `(.+)\1\1`                           | Same pattern repeated 3 times                |
| ABABA pattern                   | `(.+)(.+)\1\2\1`                    | ABABA structure                              |
| No letter `a`                   | `[^a]*`                                | Any char except `a`                          |
| Valid UCLL email                | `.+@(ucll\.be|student\.ucll\.be)`  | Must end with that domain                    |
| No 3 same characters in a row   | `(?!.*(.)\1\1)`                      | Disallow triple repeated char                |



markdown_content = """
## ✅ Regex Function Cheatsheet Additions

### Capturing and Substituting Solutions
```python
import re

def parse_time(string):
    match = re.fullmatch(r'(\\d{2}):(\\d{2}):(\\d{2})(\\.\\d{3})?', string)
    if match:
        h, m, s, ms = match.groups('.000')
        return int(h), int(m), int(s), int(ms[1:])
    return None


import re

def parse_link(string):
    match = re.fullmatch(r'<a href="([^"]+)">([^<]+)</a>', string)
    if match:
        return match.group(2), match.group(1)
    return None


import re

def collect_links(string):
    return re.findall(r'<a href="([^"]+)">.*?</a>', string)


import re

def scrape_email_addresses(string):
    return re.findall(r'\\b[a-z0-9.]+@[a-z0-9]+(?:\\.[a-z0-9]+)+\\b', string)

import re

def remove_trailing_whitespace(string):
    return re.sub(r' +$', '', string, flags=re.MULTILINE)

import re

def remove_repeated_words(string):
    def replace(match):
        return match.group(1)
    return re.sub(r'\\b([a-zA-Z]+)( \\1)+\\b', replace, string)

import re

def correct_dates(string):
    def replace(match):
        m, d, y = match.groups()
        return f'{d}/{m}/{y}'
    return re.sub(r'(\\d+)/(\\d+)/(\\d+)', replace, string)



import re

def hide_email_addresses(string):
    def replace(match):
        return '*' * len(match.group(0))
    return re.sub(r'\\b[a-z0-9.]+@[a-z0-9]+(?:\\.[a-z0-9]+)+\\b', replace, string)


Save it as a markdown file
with open("/mnt/data/regex_function_cheatsheet_additions.md", "w") as f:
f.write(markdown_content)

"/mnt/data/regex_function_cheatsheet_additions.md"

---

Good luck! 🚀 You got this!
