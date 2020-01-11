num_inputs = int(input())

inputs_list = []
for i in range(num_inputs):
    inputs_list.append(int(input()))

primes = set()
primes.add(2)
composites = set()
composites.add(1)



def find_primes(target):
    checked = {}



    for i in primes:
        if i not in checked:
            checked[target - i] = i
        else: 
            print(checked[i] ,i)
            return()    
  
    for i in range(max(primes),target):
        isPrime = True
        for x in range(2, (i//2)):

            if i % x == 0:
                isPrime = False
                break
        if isPrime == True:
            primes.add(i)
            #print(i)
            if i not in checked:
                checked[target - i] = i

                tempcheck = target-i
                for p in range(2,tempcheck//2):
                    if (tempcheck % p) == 0:
                        break
                else:
                    print(i, tempcheck)
                    return()

            else: 
                print(checked[i] ,i)
                #print(primes)
                return()
        else:
            composites.add(i)



for i in range(len(inputs_list)):
    find_primes(inputs_list[i]*2)





