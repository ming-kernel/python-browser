# Optimization Phase

def optimize(tree): # Expression trees only
    etype = tree[0]
    if etype == "binop":
        # Fix this code so that it handles a + ( 5 * 0 )
        # recursively! QUIZ!
        a = tree[1]
        op = tree[2]
        b = tree[3]
        if op == "*" and b == ("number","1"):
            return a
        elif op == "*" and b == ("number","0"):
            return ("number","0")
        elif op == "+" and b == ("number","0"):
            return a
        elif b[0] == "binop":
            r_child = optimize(b)
            return optimize(("binop", a, op, r_child))

        return tree
    

print optimize(("binop",("number","5"),"*",("number","1"))) == ("number","5")
print optimize(("binop",("number","5"),"*",("number","0"))) == ("number","0")
print optimize(("binop",("number","5"),"+",("number","0"))) == ("number","5")
print optimize(("binop",("number","5"),"+",("binop",("number","5"),"*",("number","0")))) == ("number","5")
print optimize(("binop",("number","5"),"+",("binop",("number","5"),"*",("number","0"))))
