import math

def main():
    N = 10
    M = 100
    
    montmer(N, M)

def montmer(N, M):
    for i in range(N):
        print(f"Combos: {combinations(i+1)}\n\n")

def combinations(items):
    print(f"Got items: {items}")
    all_combs = math.factorial(items)
    for i in range(0, items+1):
        all_combs = math.factorial(items-i)
        print(f"Factorial of {items-i} is {all_combs}")
    return all_combs

if __name__ == "__main__":
    main()