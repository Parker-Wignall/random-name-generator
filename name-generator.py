import random
"""
<---Random Name Generator--->
By Parker Wignall

using most first names from the USA Social Security website https://www.ssa.gov/oact/babynames/decades/century.html
using last name taken from ThoughtCo. https://www.thoughtco.com/most-common-us-surnames-1422656


"""
m_fname_dictionary = {
    0:"James",
    1:"Michael",
    2:"John",
    3:"Robert",
    4:"David",
    5:"William",
    6:"Wallace",
    7:"Richard",
    8:"Joseph",
    9:"Thomas",
    10:"Christopher",
    11:"Charles",
    12:"Daniel",
    13:"Matthew",
    14:"Anthony",
    15:"Mark",
    16:"Steven",
    17:"Andrew",
    18:"Donald",
    19:"Joshua",
    20:"Paul",
    21:"Kevin",
    22:"Kenneth",
    23:"Brian",
    24:"Timothy",
    25:"Ronald",
    26:"Jason",
    27:"George",
    28:"Edward",
    29:"Jeffrey",
    30:"Jacob",
    31:"Ryan",
    32:"Nicholas",
    33:"Gary",
    34:"Eric",
    35:"Jonathan",
    36:"Stephen",
    37:"Larry",
    38:"Justin",
    39:"Benjamin",
    40:"Scott",
    41:"Brandon",
    42:"Samuel",
    43:"Alexander",
    44:"Gregory",
    45:"Patrick",
    46:"Jack",
    47:"Frank",
    48:"Raymond",
    49:"Dennis",
    50:"Aaron",
    51:"Tyler",
    52:"Jerry",
    53:"Jose",
    54:"Nathan",
    55:"Adam",
    56:"Henry",
    57:"Zachary",
    58:"Douglas",
    59:"Peter",
    60:"Noah",
    61:"Ethan",
    62:"Kyle",
    63:"Christian",
    64:"Jeremy",
    65:"Austin",
    66:"Keith",
    67:"Sean",
    68:"Terry",
    69:"Roger",
    70:"Dylan",
    71:"Walter",
    72:"Gerald",
    73:"Jordan",
    74:"Gabriel",
    75:"Carl",
    76:"Bryan",
    77:"Jesse",
    78:"Logan",
    79:"Lawrence",
    80:"Elijah",
    81:"Arthur",
    82:"Bruce",
    83:"Harold",
    84:"Billy",
    85:"Liam",
    86:"Alan",
    87:"Juan",
    88:"Joe",
    89:"Mason",
    90:"Lucas",
    91:"Randy",
    92:"Willie",
    93:"Wayne",
    94:"Vincent",
    95:"Caleb",
    96:"Albert",
    97:"Luke",
    98:"Isaac",
    99:"Bradley",
    100:"Cameron"
}
f_fname_dictionary = {
    0:"Mary",
    1:"Patricia",
    2:"Jennifer",
    3:"Linda",
    4:"Elizabeth",
    5:"Barbara",
    6:"Susan",
    7:"Jessica",
    8:"Karen",
    9:"Sarah",
    10:"Lisa",
    11:"Nancy",
    12:"Sandra",
    13:"Ashley",
    14:"Emily",
    15:"Kimberly",
    16:"Michelle",
    17:"Donna",
    18:"Margeret",
    19:"Carol",
    20:"Betty",
    21:"Amanda",
    22:"Melissa",
    23:"Deborah",
    24:"Stephanie",
    25:"Rebecca",
    26:"Sharon",
    27:"Cynthia",
    28:"Laura",
    29:"Amy",
    30:"Kathleen",
    31:"Angela",
    32:"Emma",
    33:"Shirley",
    34:"Dorothy",
    35:"Brenda",
    36:"Nicole",
    37:"Pamela",
    38:"Samantha",
    39:"Anna",
    40:"Olivia",
    41:"Katherine",
    42:"Christine",
    43:"Debra",
    44:"Rachel",
    45:"Maria",
    46:"Carolyn",
    47:"Janet",
    48:"Heather",
    49:"Diane",
    50:"Julie",
    51:"Catherine",
    52:"Victoria",
    53:"Joyce",
    54:"Lauren",
    55:"Kelly",
    56:"Christina",
    57:"Helen",
    58:"Joan",
    59:"Hannah",
    60:"Judith",
    61:"Andrea",
    62:"Evelyn",
    63:"Megan",
    64:"Cheryl",
    65:"Ruth",
    66:"Virginia",
    67:"Sophia",
    68:"Madison",
    69:"Jacqueline",
    70:"Abigail",
    71:"Isabella",
    72:"Teresa",
    73:"Sara",
    74:"Charlotte",
    75:"Janice",
    76:"Kathryn",
    77:"Martha",
    78:"Gloria",
    79:"Ann",
    80:"Judy",
    81:"Amber",
    82:"Danielle",
    83:"Denise",
    84:"Grace",
    85:"Julia",
    86:"Natalie",
    87:"Diana",
    88:"Marilyn",
    89:"Brittany",
    90:"Beverly",
    91:"Alice",
    92:"Theresa",
    93:"Jean",
    94:"Kayla",
    95:"Alexis",
    96:"Frances",
    97:"Ava",
    98:"Tiffany",
    99:"Lori",
    100:"Bailey"
}

lname_dictionary = {
    0:"Smith",
    1:"Johnson",
    2:"Williams",
    3:"Brown",
    4:"Jones",
    5:"Garcia",
    6:"Miller",
    7:"Davis",
    8:"Rodriguez",
    9:"Martinez",
    10:"Hernandez",
    11:"Lopez",
    12:"Gonzales",
    13:"Wilson",
    14:"Anderson",
    15:"Thomas",
    16:"Taylor",
    17:"Moore",
    18:"Jackson",
    19:"Martin",
    20:"Lee",
    21:"Perez",
    22:"Thompson",
    23:"White",
    24:"Harris",
    25:"Sanchez",
    26:"Clark",
    27:"Ramirez",
    28:"Lewis",
    29:"Robinson",
    30:"Walker",
    31:"Young",
    32:"Allen",
    33:"King",
    34:"Wright",
    35:"Scott",
    36:"Torres",
    37:"Nguyen",
    38:"Hill",
    39:"Flores",
    40:"Green",
    41:"Adams",
    42:"Nelson",
    43:"Baker",
    44:"Hall",
    45:"Rivera",
    46:"Campbell",
    47:"Mitchell",
    48:"Carter",
    49:"Roberts",
    50:"Gomez",
    51:"Phillips",
    52:"Evans",
    53:"Turner",
    54:"Diaz",
    55:"Parker",
    56:"Cruz",
    57:"Edwards",
    58:"Collins",
    59:"Reyes",
    60:"Stewart",
    61:"Morris",
    62:"Morales",
    63:"Murphy",
    64:"Cook",
    65:"Rogers",
    66:"Gutierrez",
    67:"Ortiz",
    68:"Morgan",
    69:"Cooper",
    70:"Peterson",
    71:"Bailey",
    72:"Reed",
    73:"Kelly",
    74:"Howard",
    75:"Ramos",
    76:"Kim",
    77:"Cox",
    78:"Ward",
    79:"Richardson",
    80:"Watson",
    81:"Brooks",
    82:"Chavez",
    83:"Wood",
    84:"James",
    85:"Bennet",
    86:"Gray",
    87:"Mendoza",
    88:"Ruiz",
    89:"Hughes",
    90:"Price",
    91:"Alverez",
    92:"Castillo",
    93:"Sanders",
    94:"Patel",
    95:"Myers",
    96:"Long",
    97:"Ross",
    98:"Foster",
    99:"Jimenez",
    
    
    
    
}



def m_fname():
    #Generate a random number from 0 up to and not including 11
    fname_num = random.randint(0, 100)
    #Once the number has been generated, go to fname-dict and grab the associated name based on the number generated
    fname_string = m_fname_dictionary[fname_num]
    #print("fname_num: " + str(fname_num))
    return fname_string

def f_fname():

    #Generate a random number from 0 up to and not including 11
    fname_num = random.randint(0, 100)
    #Once the number has been generated, go to fname-dict and grab the associated name based on the number generated
    fname_string = f_fname_dictionary[fname_num]
    #print("fname_num: " + str(fname_num))
    return fname_string

def lname():
    
    lname_num = random.randint(0, 99)
        
    lname_string = lname_dictionary[lname_num]
    return lname_string

def multiple_names(num_of_names):
    i = 0
    print("<---Masculine Names--->")

    while(i<=num_of_names):
        fname_string = m_fname()
        lname_string = lname()
        print(f"{i+1}- {fname_string}, {lname_string}")
        i+=1
    i = 0
    print()
    print()
    print("<---Feminine Names--->")

    while(i<=num_of_names):
        fname_string = f_fname()
        lname_string = lname()
        print(f"{i+1}- {fname_string}, {lname_string}")
        i+=1
        
    
        


def main():
    print("Name Generator")
    #Creates a choice variable to get player's choice, may add more options later...
    choice = input("Press 1 to generate a masculine name, 2 to generate a feminine name or, 3 to print 10 of each!")
    if choice == "1":
        fname_string = m_fname()
        print("First name: " + fname_string)


        
    elif choice == "2":
        fname_string = f_fname()
        print("First name: " + fname_string)
        
    elif choice == "3":
        print("Generating multiples...")

        multiple_names(9)
        
        
    #Next, do the last name
    if choice != "3":            
        lname_string = lname()
        print("Last name: " + lname_string)
            
        
    
    
main()
    