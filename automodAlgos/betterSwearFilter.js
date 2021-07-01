/*
This simple algorithm can filter out swear words and even detect bypassing.
Input format: string, array, dictionary
AliasTables example:
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
Adding more "aliases" is simple, you just add it to the array of the letter like so: ["i", "1"]
Be careful with the aliases, for example adding L to the i array could cause issues.
Algorithm could probably be improved a bit speed wise, this will probably be done in the future. (for now as efficient as I can write it)
This is perfect for automod algorithms that don't want to only involve a simple in search.

This is a js rewrite of the original python algo. My js is rusty as fu(k ;) so if you spot some kind of issue tell me immediately.
*/
function checkForCusses(msg, cusses, aliasTables){
    msg = msg.toLowerCase();
    cusses.forEach(cuss => {
        cussToListToRemoveFrom = cuss.split("");
        curseFound = false;
        var lastCachedChar;
        msg.split("").forEach(char=> {
            if(aliasTables[cussToListToRemoveFrom[0]].includes(char)){
                lastCachedChar = aliasTables[cussToListToRemoveFrom[0]];
                cussToListToRemoveFrom.shift();
                curseFound = true;
            }
            else if (lastCachedChar.includes(char)){}
            else if (curseFound==true && !aliasTables[cussToListToRemoveFrom[0]].includes(char) && !lastCachedChar.includes(char)) {
                curseFound = false;
                cussToListToRemoveFrom = cuss.split("");
            }
            if (cussToListToRemoveFrom.length == 0){
                throw true
            }
        });
    });
    throw false
}
