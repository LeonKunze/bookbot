def countChars(textStr):
    ourDic = {}
    for text in textStr.split():
        text = list(text.lower())
        for x in text:
            if x.isalpha() is False:
                continue
            elif ourDic.get(x) is None:
                ourDic[x] = 1
            else:
                ourDic[str(x)] += 1

    return ourDic


with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(len(file_contents.split()))
    countDic = countChars(file_contents)
    for name, occuncies in countDic.items():
        print(f"The {name} character was found {occuncies} times")
    print("--- End report ---")
    # print(len(file_contents.split()))
