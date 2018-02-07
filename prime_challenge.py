lesser_primes = [2]
counter = 1
x = 1
while counter != 10001:
    x+=1
    for i in lesser_primes:
        div = False
        if x%i == 0:
            div = True
            break
    if div == False:
        lesser_primes = [x] + lesser_primes
        counter += 1
print("10001 prime: " + str(x))
