stock = {'apples':5,'oranges':0,'pears':7}
alreadyAte = ['john','prabu','ram']
food = input ('What food was eaten?')
person = input('Who ate food?')

def menu():

    print('Press 1: To enter stock')
    print('Press 2: To check stock')
    print('Press 3: To enter purchase')
    print('Press q: To quit the program')
    return input('What would you like to do?')

run = menu()


while True:
    if run == '1':
        print('ONE')
        addStock = input("Food to be added to the stock ?")
        amount = int(input("Quantity of food to be added in the stock"))
        stock[addStock] = amount
        run = menu()
    elif run == '2':
        print('TWO')
        for x in int:
            print('{f} : {n}'.format(f=x,n=stock[x]))
        run = menu()
    elif run== '3':
        print('THREE')
        if food in stock:
            if person in alreadyAte:
                print('{} already ate fruit'.format(person))
                run = menu()
            else:
                if stock[food] > 0:
                    stock[food] -= 1
                    alreadyAte.append(person)
                    print("{} ate {}".format(person,food))
                    run = menu()
                else:
                    print('{} did not eat because we are out of {}'.format(person,food))
                    run = menu()
        else:
            print('{} are out of stock'.format(food))
            run = menu()
    elif run == 'q':
        print(run)
        break

print("The program ended")