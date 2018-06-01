config = open('./myConfig.txt', 'w')

d1 = {"a": 1}
d2 = {"b": 2, "c": 3}
d3 = {"d": 4, "f": 5}

dictList = [d1, d2, d3]

for values in dictList:
    config.write("".join(["%s=%d\n" % (key, value) for key, value in values.items()]))
