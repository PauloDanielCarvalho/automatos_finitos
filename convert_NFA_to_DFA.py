


class NfaToDfa:
    def __init__(self,alphabet,initial_state,accepting_states,transitions,states):
        self.transitions = transitions
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.states=states
        self.list_adjacent=list()
        self.next_adjacent=initial_state+","

    def add_adjacent(self,value):
        list_=[]
        word=""
        for i in self.transitions:
            for state in self.next_adjacent.split(","):
                if state == i[0] and value in i and not i[-1] in list_:
                    word+=i[-1]
                    word+=","
                    list_.append(i[-1])
                
        self.list_adjacent[-1][self.next_adjacent].append(word)
    
    def verify_key(self,value):
        for dict in self.list_adjacent:
            if value in str(dict.keys()):
                
                return True
        return False

    def verify_same(self,value):
        for dict in self.list_adjacent:
            #print(list(dict.keys())[0].split(","))
            #print(value.split(","))
            
            if value == "":
                
                return True
            
            elif sorted(value.split(",")) == sorted(list(dict.keys())[0].split(",")):
                
                return True
        return False

    def add_next_adjacent(self):
        for i in self.list_adjacent:
           
            for a in list(i.values())[0]:
                
                if not self.verify_same(a):
                    
                    self.next_adjacent = a 
                    
                    return True
        return False
        
    def start(self):
        self.list_adjacent.append({self.next_adjacent:[]})
        
        stop = True
        while  stop:
            for i in self.alphabet:
                
                self.add_adjacent(i)
                
            stop=self.add_next_adjacent()
            if not self.verify_key(self.next_adjacent):
                self.list_adjacent.append({self.next_adjacent:[]})
            
       
        
        self.rename_name_state()
        #print(self.get_state("s3,s0,"))
        self.get_transitions()
        self.get_accepting()
        self.return_initial=self.get_state(self.initial_state+",")
        self.get_states()
        #print(self.return_initial)
        return self.return_states,self.return_initial,self.return_acceting,self.alphabet,self.get_transitions_list
    def rename_name_state(self):
        self.rename_states=[]
        for number in range(len(self.list_adjacent)):
            self.rename_states.append({f"q{number}":list(self.list_adjacent[number].keys())[0]})
        
    def get_states(self):
        self.return_states=[]
        for i in self.rename_states:
        
            self.return_states.append(list(i.keys())[0])
       
    def get_state(self,state):
        for i in self.rename_states:
            
            if sorted(state.split(",")) == sorted(list(i.values())[0].split(",")):
                    return list(i.keys())[0]
                
    def get_transitions(self):
        self.get_transitions_list=[]
        
        for i in self.list_adjacent:
            for a in range(len(list(i.values())[0])):
                
                if not list(i.values())[0][a]=="":
                    self.get_transitions_list.append([self.get_state(list(i.keys())[0]),self.alphabet[a],self.get_state(list(i.values())[0][a])])
       

    def get_accepting(self):
        self.return_acceting=[]
        for i in self.accepting_states:
            for a in self.rename_states:
                
                if i in list(a.values())[0].split(","):
                    self.return_acceting.append(list(a.keys())[0])
       


'''print("states= ",return_states)
print("initial= ",return_initial)
print("acceting= ",return_acceting)
print("alphabet= ", alphabet)
print("transations= ",get_transitions_list)'''