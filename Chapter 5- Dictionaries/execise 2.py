glossary = {
    ("string"): ("A string is any serise  characters."),
    ("comment"):("comment can be used to make the code more readable."),
    ("list"): ("Lists are used to store multiple items in a single variable."),
    ("loop"): ("Work through a collection of items, one at a time."),
    ("dictionary"): ("Dictionaries are optimized to retrieve values when the key is known."),
    }

word = ("string")
print("\n" + word.title() + ": " + glossary[word])

word = ("comment")
print("\n" + word.title() + ": " + glossary[word])

word = ("list")
print("\n" + word.title() + ": " + glossary[word])

word = ("loop")
print("\n" + word.title() + ": " + glossary[word])

word = ("dictionary")
print("\n" + word.title() + ": " + glossary[word])