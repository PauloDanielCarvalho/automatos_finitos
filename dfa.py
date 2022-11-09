


class DFA:
    def __init__(self,alphabet,initial_state,accepting_states,transitions,input_):
        self.transitions=transitions
        self.alphabet=alphabet
        self.initial_state=initial_state
        self.accepting_states=accepting_states
        self.input_=input_

    def verify_transitions(self,value):
        for i in self.transitions:
            if self.initial_state == i[0] and value in i:
                self.initial_state = i[-1]
                return True
        return False

    def start(self):
        for i in self.input_:
            if  not self.verify_transitions(i):
                return False
        
        if self.initial_state in self.accepting_states:
            return True
        return False
    
   