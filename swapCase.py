string = "Sinsa was the most memorable district in Seoul for me."
# trying to make our swap functions

            
        

# dumbSwap(string)

def pythonicSwap(s):
    new_list_str = [i.upper() if i.islower() else i.lower() for i in s.split(" ")]
    new_list_str = " ".join(new_list_str)
    return new_list_str
# dumbSwap(string)
print(pythonicSwap(string))
    
    