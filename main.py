"""
    Creating function to show *args and **kwargs usage in python
    *args receive a tuple as parameter
    **args receive a dictionary as parameter
    the names of args and kwargs can be changed.
"""
def show_poem(data, *verses, **author_information):
    text = "\n".join(verses)

    author_data = "\n".join([f"{key.title()}: {value}" for key, value in author_information.items()])

    message = f"{data}\n\n\{text}\n\n{author_data}"

    print(message)

if __name__ == '__main__':
    show_poem(
        "Saturday 31, August 2024",
        "Beautiful is better than ugly.",
         "Explicit is better than implicit.",
        "Simple is better than complex.",
        "Complex is better than complicated.",
        "Flat is better than nested.",
        "Sparse is better than dense.",
        "Readability counts",
        "Special cases aren't special enough to break the rules.",
        "Although practicality beats purity.",
        "Errors should never pass silently.",
        "Unless explicitly silenced.",
        "In the face of ambiguity, refuse the temptation to guess",
        "There should be one-- and preferably only one --obvious way to do it.",
        "Although that way may not be obvious at first unless you're Dutch.",
        "Now is better than never.",
        "Although never is often better than *right* now.",
        "If the implementation is hard to explain, it's a bad idea.",
        "If the implementation is easy to explain, it may be a good idea.",
        "Namespaces are one honking great idea -- let's do more of those!",
        author="Tim Peters",
        year=1999
    )


