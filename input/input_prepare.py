k = '''0 0 0 1 0 0 0 1 0 0 0 1 20.0 15.0 15.0
7 7 4 0 1 3 1 3 2 3 -1 0 15.0 10.0 10.0
0 0 0 1 0 0 0 1 0 0 0 1 3.0 3.0 3.0
-7 -7 0 1 0 0 0 1 0 0 0 1 3.0 5.0 3.0'''

lines = k.split("\n")

for line in lines:
    terms = line.split()
    if len(terms) != 15:
        print "ALL Hell breaks loose"
        continue

    for row in range(5):
        for column in range(3):
            print terms[row * 3 + column],
        print
    print