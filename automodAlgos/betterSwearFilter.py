# This simple algorithm can filter out swear words and even detect bypassing.
# Input format: string, array, dictionary
# AliasTables example:
"""
aliasTables = {
           "a": ["a", "@"],
           "b": ["b"],
           "c": ["c"],
           "d": ["d"],
           "e": ["e"],
           "f": ["f"],
           "g": ["g"],
           "h": ["h"],
           "i": ["i"],
           "j": ["j"],
           "k": ["k"],
           "l": ["l"],
           "m": ["m"],
           "n": ["n"],
           "o": ["o"],
           "p": ["p"],
           "q": ["q"],
           "r": ["r"],
           "s": ["s"],
           "t": ["t"],
           "u": ["u"],
           "v": ["v"],
           "w": ["w"],
           "x": ["x"],
           "y": ["y"],
           "z": ["z"]
}
"""
# Adding more "aliases" is simple, you just add it to the array of the letter like so: ["i", "1"]
# Be careful with the aliases, for example adding L to the i array could cause issues.
# Algorithm could probably be improved a bit speed wise, this will probably be done in the future. (for now as efficient as I can write it)
# This is perfect for automod algorithms that don't want to only involve a simple in search.

def checkForCusses(msg, cusses, aliasTables):
    msg = msg.lower()
    for cuss in cusses:
        cussToListToRemoveFrom = list(cuss)
        curseFound = False
        lastCachedChar = ""
        for x in msg: 
            if x in aliasTables.get(cussToListToRemoveFrom[0], cussToListToRemoveFrom[0]): 
                lastCachedChar = aliasTables.get(cussToListToRemoveFrom[0], cussToListToRemoveFrom[0])
                del cussToListToRemoveFrom[0]
                curseFound = True
            elif  x in lastCachedChar:
                pass
            elif curseFound and not x in aliasTables.get(cussToListToRemoveFrom[0], cussToListToRemoveFrom[0]) and not x in lastCachedChar:
                cussToListToRemoveFrom = list(cuss)
                curseFound = False
            if len(cussToListToRemoveFrom) == 0:
                return True
    return False
