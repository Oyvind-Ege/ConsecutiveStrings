def longest_consec(array, k):
    """ 
    Signature: List, Number -> String
    Purpose: 
    Accepts a list of strings, lstrings and a number, k. Returns a string: s
    s is a concatenation of the k biggest strings in lstrings.
    If two groups of k strings have the same length, s will be a concatenation of the first group.
    
    Boundaries:
    If lstrings is empty, return ''
    if k is 0, return ''
    if k > len(lstrings), return ''
    """
    if len(array) == 0 or k == 0 or k > len(array):
        return ''
    
    result = ''
    start = index_of_biggest(sum_sequence(sum_string_lengths(array), k))

    string_as_list = array[start:start+k]
    print(string_as_list)
    for string in string_as_list:
        result += string

    return result


def index_of_biggest(array):
    """
    * Signature: List -> Number
        @List(Numbers)
    * Purpose: Returns the index of the biggest number in a list of number
    """
    biggest = 0
    index = 0
    for i, num in enumerate(array):
        if num > biggest:
            index, biggest = i, num
    
    return index

def sum_string_lengths(array):
    """
    *Signature: List -> List
        @List(Strings)
    *Purpose: Accepts a list of strings. Outputs a list of numbers representing the length of those strings. 
    """
    return [len(string) for string in array]

def sum_sequence(array, k):
    """
    *Signature: List, Number -> List
        @List(Numbers)
        @Integer(k)
    *Purpose: This function accepts a list of numbers, L, and a number k.
    *It will produce a list of sums of k elements from L.

    k <= nL, nL >= 1, k >= 1
    Of groups k with size n, you will have n - (k-1) groups
    """

    group_number = (len(array)) - (k-1)

    groups = [array[index:index+k] for index in range(group_number)]

    return [sum(group) for group in groups]

#Twos
#["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2
#[4,        7,          5,      4,      4,      3       5       7      ] <--INPUT -> sum_sequence
#[      11         12       9       8       7       8       12         ] <--OUTPUT
#[                 12                                                  ]

#['first', 'pair'], 2
#[  5,      4    ]
#[      9        ]

#['1st', 'pair', 'second', 'pair'], 2
#[  3       4       6        4   ]
#[      7       10      10       ]
#[              10               ]

#Threes
#['first', 'second', 'third'], 3
#[  5          6        5   ]
#[             16           ]


#['first', 'second', 'third', '4th'], 3
#[  5          6        5       3  ]
#[          16          15         ]
#[          16                     ]



#['1st', 'second', 'third', 'fourth', '5th'], 3
#[  3       6       5           6       3  ]
#[          14          17          14     ]
#[                  17                     ]



#['1st', 'second', 'third', 'fourth', '5th', '6th'], k = 3, n = 6
#[  3       6       5           6       3      3  ] 6 - (3-1) = 6 - 2 = 4 groups
#[       14         17         14         12      ] --> 4 groups of 3
#[                     1                          ] INDEX OF BIGGEST

#['1st', 'second', 'third', 'fourth', '5th', '6th'], k = 4, n = 6
#[  3       6       5           6       3      3  ] 6 - (4-1) = 6 - 3 = 3 groups
#[              20           20         17        ] --> 3 groups of 4
#[                     0                          ] INDEX OF BIGGEST
# 

""" BASE[INDEXOFBIGGEST:k] """
# = 1:k = 1:3 = 'secondthirdfourth'
# = 0:k = 0:4 = '1stsecondthirdfourth5th' 

