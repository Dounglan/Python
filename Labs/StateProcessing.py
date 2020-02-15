#Dounglan Cheung
#lab 20
#4.10.19
class State:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def display(self):
        print("{0:<20}Population:{1:,}".format(self.name, self.population))
        
    def getPopulation(self):
        return self.population

    def getName(self):
        return self.name
    
def makeAState(line):    
    item = line.split("\t")
    name = item[0].strip()
    pop = int(item[1].strip().replace(",",""))
    s = State(name, pop)
    return s

def usePopulation(aState):    
    return aState.getPopulation()
    
def useName(aState):
    return aState.getName()
    
def main():
#    state1 = State("New York", 19862512)
#    state1.display()
#    state2 = State("Connecticut", 3592512)
#    state2.display()
#Part I C
    stateList = []
    infile = open("states.txt","r")
    for line in infile:
        st = makeAState(line)
        st.display()
#Part D i
        stateList.append(st)
    print("*"*50)
#choice: comment out one for population sorted/name sorted
    stateList.sort(key=usePopulation)
    stateList.sort(key=useName)
#part D ii        
    for i in stateList:
        i.display()
    infile.close()
main()