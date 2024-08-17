import timeit;
def mcd_fuerza_bruta(a, b):

    menor = min(a, b) # 1 + 1
    for i in range(menor, 0, -1): ## 1 + n(1 + INSIDE + 1)
        if a % i == 0 and b % i == 0: ## 1 + 1 + 2 + 1 + 1 + 2
            return i ## 1
    return 1 ## 1

## Worst and Average Case
## 2 + 1 + n( 1 + 1 + 2 + 1 + 1 + 2) + 1 = 4 + 8n
## Better Case
## 1 + 1 + n(1 + 1 + 1) = 2 + 3n


def mcd_euclides(a, b):
        while b != 0:  ## 1 + 2 + n(INSIDE)
            a, b = b, a % b ## 1 + 1
        return a ## 1
    
## Worst and Average Case
## 2 + 1 + n(1 + 1 + 1) + 1 = 4 + 3n
## Better Case
## 2 + 1 + 1 = 4


def compare_euclides(a, b):
    start = timeit.default_timer()
    mcd_euclides(a, b)
    end = timeit.default_timer()
    elapsed_time = end - start
    return f"{elapsed_time:.6f} seconds"

def compare_fuerza_bruta(a, b):
    start = timeit.default_timer()
    mcd_fuerza_bruta(a, b)
    end = timeit.default_timer()
    elapsed_time = end - start
    return f"{elapsed_time:.6f} seconds"

def lower_time():
    if(compare_fuerza_bruta(10,10) < compare_euclides(10,10)): 
        return "Fuerza Bruta"
    else:
        return "Euclides"

print("Euclides:", compare_euclides(10000000,1000000000000))
print("Fuerza Bruta:", compare_fuerza_bruta(10000000,10000000))


##Todo: Compare these algorithms with the time module