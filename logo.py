from colorama import Fore

def dense_ascii_suparp():
    art = '''
SSSSS   UU  UU  PPPPP   AAAAAA  RRRRR   PPPPP
SSSSS   UU  UU  PPPPP   AA  AA  RRRRR   PPPPP
SS      UU  UU  P   P   AA  AA  R   R   P   P
 SSSSS  UU  UU  PPPPP   AAAAAA  RRRRR   PPPPP
    SS  UU  UU  PP      AA  AA  RR  RR  PP 
SSSSSS   UUU    PP      AA  AA  RR  RR  PR  
    '''
    print(Fore.BLUE + art + Fore.RESET)