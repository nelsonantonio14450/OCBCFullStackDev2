from dog import Dog, Terrir

buddy = Dog("asdasd", 9)

print(buddy.name, buddy.age, buddy.species)

raka = ["Raka Ardhi", 28, "CurDev", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

print(mccoy[1])
buddy.test()
print(type(buddy) is Dog)

terr = Terrir("watch dogs", buddy.age, "nopes", "asdasd")
print(terr.name, terr.age, terr.species, terr.breed, terr.sound)
print(type(terr) is Dog)
print(isinstance(terr, Dog))
