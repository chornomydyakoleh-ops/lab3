import doctest


def reverse_words(text: str) -> str:
    """
    >>> reverse_words("abcd")
    'dcba'
    >>> reverse_words("abcd efgh")
    'dcba hgfe'
    >>> reverse_words("")
    ''
    >>> reverse_words("a1bcd efg!h")
    'd1cba hgf!e'
    >>> reverse_words(12345)
    Traceback (most recent call last):
        ...
    TypeError: Argument must be a string
    """
    if not isinstance(text, str):
        raise TypeError("Argument must be a string")

    result = []
    for word in text.split(" "):
        letters = [char for char in word if char.isalpha()]
        new_word = [letters.pop() if char.isalpha() else char for char in word]
        result.append("".join(new_word))

    return " ".join(result)


if __name__ == "__main__":
    doctest.testmod(verbose=True)

    user_text = input("Текст для розвороту: ")
    print("Результат:", reverse_words(user_text))