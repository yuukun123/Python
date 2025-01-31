def findShortestStringInList(strings):
    if not strings: #check if strings is empty
        return None
    shortest_str = min(strings, key=len)
    return shortest_str

strings = ["hello", "word", "hi", "hello"]
print(findShortestStringInList(strings))