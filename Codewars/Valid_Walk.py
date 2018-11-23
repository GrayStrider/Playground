def isValidWalk(walk):
    return walk.count("n") == walk.count("s") and walk.count("w") == walk.count("e")


walk = ['n', 's', 'e', 'e']

print(isValidWalk(walk))
