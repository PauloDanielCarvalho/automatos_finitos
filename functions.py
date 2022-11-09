
def add_list(list_,name):
    list_add=[]
    for i in list_:
        if i.strip("\n") == name:
            break
        list_add.append(i.strip("\n"))     
    return list_add

def split_list(list_transitions):
    list_return=[]
    for i in list_transitions:
        list_=[]
        list_.append(i.split(":")[0])
        split_=i.split(":")[1].split(">")[0]
        for  a in split_.split(","):
            list_.append(a)
        list_.append(i.split(":")[1].split(">")[1])
        list_return.append(list_)
    return list_return
    
def file_read(name_file):
    with open(f"./{name_file}.txt","r") as file_txt:
        file = file_txt.readlines()
        for i in range(len(file)):
            if file[i] =="#states\n":
                states=add_list(file[i+1:],"#initial")

            elif file[i] == "#initial\n":
                initial=add_list(file[i+1:],"#accepting")

            elif file[i] == "#accepting\n":
                accepting=add_list(file[i+1:],"#alphabet")
            
            elif file[i] == "#alphabet\n":
                alphabet=add_list(file[i+1:],"#transitions")

            elif file[i] == "#transitions\n":
                transitions=add_list(file[i+1:],"")
        split_transitions=split_list(transitions)

        '''print(f"states = {states}")
        print(f"initial = {initial}")
        print(f"accepting = {accepting}")
        print(f"alphabet = {alphabet}")
        
        
        print(f"transitions = {split_transitions}")
        print(f"transitions = {transitions}")'''
   
    return states,initial,accepting,alphabet,split_transitions

