import time

def build_hack_tree(program):

    current_dmg = 0
    power = 1
    command_potential = []
    hack_efficiencies = []

    for command in program:
        if command == "C":
            command_potential.append(power)
            power = power * 2
        else:
            current_dmg += power
            hack_efficiencies.append(command_potential)
            command_potential = []

    return hack_efficiencies, current_dmg

def calculate_number_hacks(d, current_dmg, hack_efficiencies):

    nodes_after = 0
    num_hacks = 0

    for node in reversed(hack_efficiencies):
        for hack_efficiency in reversed(node):
            
            current_dmg -= hack_efficiency
            num_hacks += 1
            
            if current_dmg <= d:
                return num_hacks

            for i in range(0, nodes_after):
                current_dmg -= hack_efficiency
                num_hacks += 1
                if current_dmg <= d:
                    return num_hacks

        nodes_after += 1

    return -1

def getstrings(): return stdin.readline().strip().split()
def getints(): return map(int,stdin.readline().strip().split())
def getfloats(): return map(float,stdin.readline().strip().split())

def thing(D,P):
  it=0
  while 1:
    d=0;c=1
    for x in P:
      if x=='C': c*=2
      else: d+=c
    if d<=D: return it
    i=P.rfind("CS")
    if i==-1: return "IMPOSSIBLE"
    P=P[:i]+"SC"+P[i+2:]
    it+=1


ds = [5,12,53,1,24,43,53,21,32,432,435,2334,532]
inps = ["CSSCSCCSCSCSSCSCSCSCCCCSSSCSCSSCSCSSCSCSSCSCSSCSCSSCSCSCSSCSCSCSCSCSSCSCSCSCCSCCSCSCSCCCSCCCSCCSSSSCSCSCS", "CSCSCSCCCSCSCSSCSCSCSCCCSCSCSSCSCSCSCCCSCSCSSCSCSCSCSSCSCSCSCSSCSCSCSCCSCSCCSCSCCSSSSCCCSSCSSC", "CCSCSCCSCCCCSSSSCSCCSSSCCSSCSCCCSCSCSCCSSSSCCCSCSCSCSCSSCSCCSSCSCSSSSSCCSCSCSCSCCCC","CCCSSSCSCSSSCCSSCSCCSSSCCSSCSCCCSCSCSCCSSSSCCCSCSCSCSCSSCSCCSSCSCSSSCSCCSSSCCSSCSCCCSCSCSCCSSSSCCCSCSCSCSCSSCSCCSSCSCSSSCSCCSSSCCSSCSCCCSCSCSCCSSSSCCCSCSCSCSCSSCSCCSSCSCSCSCSCSCSCSCCSSCS", "SSCSCSCSCCCSCSCCCSCSCSCSSCSCSCSCSC","CSCSCSSSCSCCSCSCSSCSCSCSCCSCSCSSCSCSCSCCCCSCSCCCSSSSSCSCSCSCSSC","SSSCCCSCSCSCSCSCSSCSCSCSCCSCSCSCSSCSCSCSCCSCSSCSCSCSCCSCSCSSCSCSCSCCCCCCSCSCSCCCSSSSCSCSSC","CCSCSCSSSSCSCCCSCSCSSCSCSSCSCSCSCCSCSCSSCSCSCSCCSCSCSSCSCSCSCCCCCSSSSSSCSCSCSCSCSSSS","SCSSSCCCCSCSCSCCCSSSSSSSCCCCCSCSCCCSSCSSCCCCCCSSSCSCS","SSCSCCSSSCCSSCSCCCSCSCSCCSSSSCCCSCSCSCSCSSCSCCSSCSCS","SSCSCCSSSCCSSCSCCCSCSCSCCSSSSCCCSCSCSCSCSSCSCCSSCSCS","SSCSCCSSSCCSSCSCCCSCSCSCCSSSSCCCSCSCSCSCSSCSCCSSSCCSSCSCCCSCSCSCCSSSSCCCSCSCSCSCSSCSCCSSCSCSSSCSCCSSSCCSSCSCCCSCSCSCCSSSSCCCSCSCSCSCSSCSCCSSCSCSSSCSCCSSCSCS","SSCSCCSSSCCSSCSSCSCCSSSCCSSCSCCCSCSCSCCSSSSCCCSCSCSCSCSSCSCCSSCSCSSCCCSCSCSCCSSSSCCCSCSCSCSCSSCSCCSSCSCS"]


start = time.time()

ind = 0
for inp in inps:
    d = ds[ind]

    hack_efficiencies, current_dmg = build_hack_tree(inp)

    if current_dmg < d:
        print("0 nötig")

    num_hacks = calculate_number_hacks(d, current_dmg, hack_efficiencies)

    if num_hacks == -1:
        print("IMPOSSIBLE")
    else:
        print("POSSIBLE: " + str(num_hacks))

    ind += 1

end = time.time()
print(end - start)




print("===============================")
start = time.time()
ind = 0
for inp in inps:
    d = ds[ind]

    erg = thing(d,inp)
    print(erg)

    ind += 1

end = time.time()
print(end - start)
