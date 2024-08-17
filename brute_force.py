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


##Todo: Compare these algorithms with the time module