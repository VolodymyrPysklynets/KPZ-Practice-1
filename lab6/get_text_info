def get_text_info(filepath):
    from collections import Counter
    import os.path

    if not os.path.exists(filepath):
        return "!Error!"

    text = open(filepath).read()

    arrayList = []
    word = ""

    text = text.lower()

    for index, i in enumerate(text):
        if not i.isalpha():
            if len(word) != 0:
                arrayList.append(word)
                word = ""
        else:
            word += i
            if index == len(text)-1:
                arrayList.append(word)
                word = ""

    return Counter(arrayList)


print(get_text_info("article.txt"))
