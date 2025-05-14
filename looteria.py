import random 
numsecret = random.randint(1,10)

adivinha = int(input('digite o numero q vc acaha q é: '))

while adivinha != numsecret :
    
    print('numero errado') 

    if adivinha > numsecret:
        print('numero muito alto')
    elif adivinha < numsecret:
        print('numero muito baixo ')

        adivinha = int(input('digite o numero q vc acaha q é: '))
        if adivinha == numsecret:
            print('numero correto parabens')


