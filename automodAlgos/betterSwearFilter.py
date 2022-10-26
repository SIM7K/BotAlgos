aliasTables =  {
            "a": ["a", "@"],
            "b": ["b"],
            "c": ["c"],
            "d": ["d"],
            "e": ["e"],
            "f": ["f"],
            "g": ["g"],
            "h": ["h"],
            "i": ["i", "1"],
            "j": ["j"],
            "k": ["k"],
            "l": ["l"],
            "m": ["m"],
            "n": ["n"],
            "o": ["o"],
            "p": ["p"],
            "q": ["q"],
            "r": ["r"],
            "s": ["s", "$"],
            "t": ["t", "7"],
            "u": ["u"],
            "v": ["v"],
            "w": ["w"],
            "x": ["x"],
            "y": ["y"],
            "z": ["z"]
        }

def convertForSeekAliasTables(aliasTables):
    cvtResult = {}
    for key in aliasTables:
        for element in aliasTables[key]:
            cvtResult[element] = key
    return cvtResult

newAliasTables = convertForSeekAliasTables(aliasTables)

swears = ["shit"]
swears_nospaceatfront = ["fuck"]

seps = ["_", ".", " "]

#initialised

#run this to transform string into baseline

stri = "testshiiiit coalfuck"
newstri = []
cached_char = []
ind = 0
spaces = []
for char in stri:
    if char in seps and not char in cached_char:
        spaces.append(ind)
        cached_char = seps
    elif char not in cached_char:
        newstri.append(newAliasTables.get(char, char))
        ind += 1
        cached_char = newAliasTables.get(char, char)

joined_newstri = "".join(newstri)

print(joined_newstri)

#run this to check for swears

def seek_with_spaces():
    for swear in swears_nospaceatfront:
        if swear in joined_newstri:
            indexes = [index for index in range(len(joined_newstri)) if joined_newstri.startswith(swear, index)]
            for index in indexes:
                if index in spaces:
                    return True
    return False

def seek_without_spaces():
    for swear in swears:
        if swear in joined_newstri:
            return True
    return False

#figure this out yourself i am too tired to explain it
