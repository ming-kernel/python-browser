# Writing Shift

# We are currently looking at chart[i] and we see x => ab . cd from j. The input is tokens.

# Your procedure, shift, should either return None, at which point there is
# nothing to do or will return a single new parsing state that presumably
# involved shifting over the c if c matches the ith token.

def shift (tokens, i, x, ab, cd, j):
    # Insert code here
    if cd == [] or len(tokens) < i - 1:
        return None
    elif cd[0] == tokens[i]:
        return (x, ab + [cd[0]], cd[1:], j)
    else:
        return None



print shift(["exp","+","exp"],2,"exp",["exp","+"],["exp"],0) == ('exp', ['exp', '+', 'exp'], [], 0)
print shift(["exp","+","exp"],0,"exp",[],["exp","+","exp"],0) == ('exp', ['exp'], ['+', 'exp'], 0)
print shift(["exp","+","exp"],3,"exp",["exp","+","exp"],[],0) == None
print shift(["exp","+","ANDY LOVES COOKIES"],2,"exp",["exp","+"],["exp"],0) == None
print shift(["exp","+","exp"],2,"exp",["exp","+"],["exp"],0)




print '=' * 30

# Writing Reductions
# We are looking at chart[i] and we see x => ab . cd from j.

# Hint: Reductions are tricky, so as a hint, remember that you only want to do
# reductions if cd == []

# Hint: You'll have to look back previously in the chart. 

def reductions(chart, i, x, ab, cd, j):
    # Insert code here!
    if cd != []:
        return None
    else:
        result = []
        pre_states = chart[j]
        for state in pre_states:           
            the_cd = state[2]
            if the_cd != [] and the_cd[0] == x:
                result.append((state[0], state[1] + [the_cd[0]], the_cd[1:], state[3]))
        return result
    
    
chart = {0: [('exp', ['exp'], ['+', 'exp'], 0), 
             ('exp', [], ['num'], 0), 
             ('exp', [], ['(', 'exp', ')'], 0), 
             ('exp', [], ['exp', '-', 'exp'], 0), 
             ('exp', [], ['exp', '+', 'exp'], 0)], 
         1: [('exp', ['exp', '+'], ['exp'], 0)], 
         2: [('exp', ['exp', '+', 'exp'], [], 0)]
         }

print reductions(chart,2,'exp',['exp','+','exp'],[],0) == [('exp', ['exp'], ['-', 'exp'], 0), ('exp', ['exp'], ['+', 'exp'], 0)]
