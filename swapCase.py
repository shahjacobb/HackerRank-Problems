string = "Sinsa was the most memorable district in Seoul for me."
# trying to make our swap functions


def swap(s):
    new_str = []
    new_str = [s[i].upper() if s[i].islower() else s[i].lower() for i,v in enumerate(s)]
    new_str= "".join(new_str)
    
    return new_str


print(swap(string))
    