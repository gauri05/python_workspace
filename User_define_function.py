print("User_define function Demo")
def u_def():
    print("Inside U_def")
def p_def(val):
    print("Inside P_def")
    print("Accepted value is",val)
def r_def(val):
    print("Inside r_def")
    print("Accepted value is",val)
    return val+1
def accept_multi_def(val1,val2):
    print("Inside multi_def")
    ans =val1 +val2
    sub =val1 -val2
    return ans,sub
def a_c_def():
    print("Inside A_c_def")
    u_def()
def O_def():
    print("Inside outer def")
    def I_def():
        print("Inside Inner def")
    I_def()