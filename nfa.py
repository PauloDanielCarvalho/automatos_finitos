

class NFA:
    def __init__(self,alphabet,initial_state,accepting_states,transitions,input_,states):
        self.transitions = transitions
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.input_ = input_
        self.states=states
        self.states_double=[]
        self.state_initial_transation=[]

    def get_all_transiton_by_state(self,state):
        self.list_return=[]
        for i in self.transitions:
            if i[0]==state:
                self.list_return.append(i)
        return self.list_return
    
    def get_transition_equal(self,list_transations):
        for i in range(len(list_transations)):
            
            if list_transations[i][0]== list_transations[i][-1]:
                self.states_double.append(list_transations[i])
                del self.list_return[i]
                return True
        return False

    def verify_list(self,i):
        for d in self.list_return:
            if i in d:
                return True   
        return False      

    def get_state_double(self):
        for states in self.states:
            if self.get_transition_equal(self.get_all_transiton_by_state(states)):
                
                for i in self.states_double[-1]:
                    if not self.verify_list(i):
                        del self.states_double[-1]
    
    def veryfy_states_double(self,value):
        for i in self.states_double:
            if self.initial_state == i[0] and value in i:
                return i
        return False


    def verify_transition(self,value):
        for i in self.transitions:
            state=self.veryfy_states_double(value)
            if state:
                if self.initial_state == i[0] and value in i and not self.initial_state in self.state_initial_transation and i[0] != i[-1]:
                    self.state_initial_transation.append(state[0])
                    self.state_initial_transation.append(value)
                    self.state_initial_transation.append(i[-1])
                    self.initial_state=i[-1]
                    
                    return True
            elif value in self.state_initial_transation:
                return True

            if self.initial_state == i[0] and value in i and not i[0]==i[-1]:
                self.initial_state=i[-1]
                self.state_initial_transation=[]
                return True
            if self.state_initial_transation != []:
                if self.state_initial_transation[0] == i[0] and value in i and i[0] != i[-1]:
                    self.initial_state=i[-1]
                    self.state_initial_transation=[]
                    return True
        return False

    def start(self):
        self.get_state_double()
        for value in self.input_:
            
            if not self.verify_transition(value):
                return False
        try:
            if self.initial_state in self.accepting_states or self.state_initial_transation[0] in self.accepting_states :
                return True
            else:
                return False
        except:
            return False
    
    
        
    
        