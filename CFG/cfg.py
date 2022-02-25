import sys
#Usage: python cfg.py <input_file_name>
input_file_name = sys.argv[1]

file = open(input_file_name)
lines = file.readlines()
cfg = []

#Set up cfg array
for line in lines:
    cfg.append(line.split())

terminals = []
non_terminals = []

#Forces cfg array to conform to the form [Non-terminal, terminal, terminal....] for each line. The "->" is implicit between
#the first and second elements of each line.
#A list of terminals and a list of non-terminals are also created
i = 0
while i < len(cfg):
    j = 0
    while j < len(cfg[i]):
        print(i,j)
        if cfg[i][j] == "->":
            print("POP")
            cfg[i].pop(j)
            j -= 1
            print(j)
        elif j == 0 and cfg[i][j] == "|":
            cfg[i][j] = cfg[i-1][0]
        elif cfg[i][j] == "|":
            tmp = []
            tmp.append(cfg[i][0])
            tmp = tmp + cfg[i][j+1:]
            cfg.insert(i+1, tmp)
            while j < len(cfg[i]):
                cfg[i].pop(j)
        elif j == 0:
            if not cfg[i][j] in non_terminals:
                non_terminals.append(cfg[i][j])
        elif cfg[i][j].islower():
            if not cfg[i][j] in terminals:
                terminals.append(cfg[i][j])
        j+=1
    i += 1

#printing the output.

print("Grammar Non-Terminals:")
s = ""
for t in non_terminals:
    s += t + " "
print(s)

print("Grammar Terminals:")
d = ""
for t in terminals:
    d += t + " "
print(d)

print("Grammar Symbols: ")
print(s, d)

print("Grammar Rules")

for c in cfg:
    s = ""
    for i in range(len(c)):
        s += c[i] + " "
        if(i == 0):
            s += "-> "
    print(s)