from itertools import product
import re


# Evaluate a propositional logic expression

def evaluate(expr, model):

    expr = expr.replace("<->", " == ")
    expr = expr.replace("->", " <= ")
    expr = expr.replace("&", " and ")
    expr = expr.replace("|", " or ")

    # Replace NOT operator with proper parentheses
    expr = re.sub(r'~\s*([A-Z][A-Za-z0-9_]*)',
                  r'(not \1)', expr)

    for symbol, value in model.items():
        expr = re.sub(
            r'\b' + re.escape(symbol) + r'\b',
            str(value),
            expr
        )

    return eval(expr)



# Find all propositional symbols
def find_symbols(expressions):

    symbols = set()

    for expr in expressions:
        words = re.findall(r'\b[A-Z][A-Za-z0-9_]*\b', expr)

        for word in words:
            symbols.add(word)

    return sorted(symbols)


# Check whether Knowledge Base entails Query
def truth_table_entails(kb, query):

    symbols = find_symbols(kb + [query])

    print("\nPropositional Symbols:", symbols)

    print("\nTRUTH TABLE")
    print("-" * 60)

    for symbol in symbols:
        print(f"{symbol:8}", end="")

    print(f"{'KB':8}{'Query':8}")
    print("-" * 60)

    entails = True

    # Generate all possible truth assignments
    for values in product([False, True], repeat=len(symbols)):

        model = dict(zip(symbols, values))

        # Evaluate Knowledge Base
        kb_result = all(evaluate(expr, model) for expr in kb)

        # Evaluate Query
        query_result = evaluate(query, model)

        # Display truth assignment
        for symbol in symbols:
            print(f"{str(model[symbol]):8}", end="")

        print(f"{str(kb_result):8}{str(query_result):8}")

        # Check entailment
        if kb_result and not query_result:
            entails = False

    print("-" * 60)

    if entails:
        print("\nRESULT: KB entails the Query.")
        print("Therefore, KB |= Query is TRUE.")
    else:
        print("\nRESULT: KB does not entail the Query.")
        print("Therefore, KB |= Query is FALSE.")


# Main program
print("==========================================")
print(" TRUTH TABLE ENUMERATION ALGORITHM")
print("==========================================")

n = int(input("\nEnter number of sentences in KB: "))

kb = []

for i in range(n):
    sentence = input(f"Enter KB sentence {i + 1}: ")
    kb.append(sentence)

query = input("\nEnter the Query: ")

truth_table_entails(kb, query)