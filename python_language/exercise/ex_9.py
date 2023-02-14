# print languages = ["python", "java", "swift", "c", "c++"] in all different languages except swift and c++

languages = ["python", "java", "swift", "c", "c++"]

for opbhai in languages:
    if opbhai == "swift" or opbhai == "c++":
        continue
    else:
        print(opbhai)
