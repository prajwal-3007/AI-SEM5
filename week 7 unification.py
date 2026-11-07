class UnificationFailure(Exception):
    pass


# Parse an expression into a nested tuple structure
def parse_expression(s):
    s = s.replace(" ", "")

    def parse():
        nonlocal s

        if not s:
            raise ValueError("Invalid expression")

        # Read symbol
        name = ""

        while s and (s[0].isalnum() or s[0] in "?_"):
            name += s[0]
            s = s[1:]

        if not name:
            raise ValueError("Invalid symbol")

        # Check for function or predicate
        if s.startswith("("):
            s = s[1:]
            args = []

            while True:
                args.append(parse())

                if s.startswith(","):
                    s = s[1:]
                elif s.startswith(")"):
                    s = s[1:]
                    break
                else:
                    raise ValueError("Missing comma or closing bracket")

            return (name, *args)

        return name

    result = parse()

    if s:
        raise ValueError("Extra characters in expression")

    return result


# Check whether a symbol is a variable
def is_variable(x):
    return isinstance(x, str) and x.startswith("?")


# Apply substitutions
def substitute(expr, subst):
    if isinstance(expr, str):
        while expr in subst:
            expr = subst[expr]
        return expr

    if isinstance(expr, tuple):
        return (expr[0],) + tuple(
            substitute(arg, subst) for arg in expr[1:]
        )

    return expr


# Occurs check
def occurs_check(var, expr, subst):
    expr = substitute(expr, subst)

    if var == expr:
        return True

    if isinstance(expr, tuple):
        return any(
            occurs_check(var, arg, subst)
            for arg in expr[1:]
        )

    return False


# Unify variable with expression
def unify_variable(var, expr, subst):

    expr = substitute(expr, subst)

    if var == expr:
        return subst

    if occurs_check(var, expr, subst):
        raise UnificationFailure(
            "Occurs check failed!"
        )

    subst[var] = expr

    return subst


# Main unification algorithm
def unify(x, y, subst=None):

    if subst is None:
        subst = {}

    x = substitute(x, subst)
    y = substitute(y, subst)

    if x == y:
        return subst

    if is_variable(x):
        return unify_variable(x, y, subst)

    if is_variable(y):
        return unify_variable(y, x, subst)

    if isinstance(x, tuple) and isinstance(y, tuple):

        if x[0] != y[0]:
            raise UnificationFailure(
                "Predicate/function symbols do not match"
            )

        if len(x) != len(y):
            raise UnificationFailure(
                "Number of arguments does not match"
            )

        for a, b in zip(x[1:], y[1:]):
            subst = unify(a, b, subst)

        return subst

    raise UnificationFailure(
        "Expressions cannot be unified"
    )


# Convert tuple expression into readable format
def format_expression(expr):

    if isinstance(expr, str):
        return expr

    return expr[0] + "(" + ", ".join(
        format_expression(arg) for arg in expr[1:]
    ) + ")"


# Main program
print("======================================")
print(" FIRST ORDER LOGIC - UNIFICATION")
print("======================================")

try:

    exp1 = input("\nEnter first expression: ")
    exp2 = input("Enter second expression: ")

    # Parse input expressions
    expr1 = parse_expression(exp1)
    expr2 = parse_expression(exp2)

    print("\nExpression 1:", format_expression(expr1))
    print("Expression 2:", format_expression(expr2))

    # Perform unification
    result = unify(expr1, expr2)

    print("\nUnification Successful!")

    if result:
        print("\nMost General Unifier (MGU):")

        for var, value in result.items():
            print(var, "->", format_expression(value))
    else:
        print("\nNo substitution required.")

    print("\nUnified Expression:")
    print(format_expression(substitute(expr1, result)))

except (UnificationFailure, ValueError) as e:

    print("\nUnification Failed!")
    print("Reason:", e)
