def closest_match(query, collection):
    collection = collection.split(" ")
    match = ""
    matchPoints = -100
    matchExcess = 100
    for word in collection:
        points = 0
        index = 0
        while len(query) > index and len(word) > index and query[index] == word[index]:
            points += 1
            index += 1
        excess = len(word) - points
        if points >= matchPoints:
            if excess < matchExcess:
                match = word
                matchPoints = points
                matchExcess = excess
    return match
