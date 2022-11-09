
from functions import file_read
from nfa import NFA
from dfa import DFA
from convert_NFA_to_DFA import NfaToDfa

print("1-transforma nfa para dfa depois testar\n2-testar dfa\n3-testar nfa\n4-mostrar transformaco nfa para dfa")
input_=input("Digite o numero: ")
if input_=="1":
    states,initial_state,accepting_states,alphabet,transitions=file_read("automatonfa")
    return_states,return_initial,return_acceting,alphabet,get_transitions_list=NfaToDfa(alphabet,initial_state[0],accepting_states,transitions,states).start()
    print("nfa para dfa....ok")
    value_=input("palavra: ")
    
    dfa=DFA(alphabet,return_initial,return_acceting,get_transitions_list,value_).start()
    print(dfa)
value_="bba"
value_=list(value_)
if input_=="3":
    states,initial_state,accepting_states,alphabet,transitions=file_read("automatonfa")
    value_=input("palavra: ")
    nfa=NFA(alphabet,initial_state[0],accepting_states,transitions,value_,states).start()
    print(nfa)
if input_=="2":
    states,initial_state,accepting_states,alphabet,transitions=file_read("automatodfa")
    value_=input("palavra: ")
    dfa=DFA(alphabet,initial_state[0],accepting_states,transitions,value_).start()
    print(dfa)
    
if input_=="4":
    states,initial_state,accepting_states,alphabet,transitions=file_read("automatonfa")
    return_states,return_initial,return_acceting,alphabet,get_transitions_list=NfaToDfa(alphabet,initial_state[0],accepting_states,transitions,states).start()
    print("states= ",return_states)
    print("initial= ",return_initial)
    print("acceting= ",return_acceting)
    print("alphabet= ", alphabet)
    print("transations= ",get_transitions_list)






