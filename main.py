# function converts text file of street names and number
# ranges into a single line per number street combination

filename = "DMSStreetList.txt"
fileoutput = []

with open(filename, "r") as f:
    street = ''
    streetnumbers = []
    for line in f:
        allstreetnumbers = []
        line = line.strip()
        if line.find('-') == -1 and line.find(',') == -1:
            street = line
        else:
            splits = line.split(', ')
            for s in splits:
                ns = s.split('-')
                x = int(ns[0])
                y = int(ns[1])
                xy = range(x, y, 2)
                allstreetnumbers.extend(xy)
            streetnumbers = [street, set(allstreetnumbers)]
            fileoutput.append(streetnumbers)

with open("DMSStreetOutput.txt", "w") as o:
    for r in fileoutput:
        printablestreet = r[0]
        for s in r[1]:
            outputline = str(s) + ' ' + printablestreet + '\n'
            o.write(outputline)