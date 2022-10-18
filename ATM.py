print("Welcom to BankWord SBI")
print("Insert the Card ")
language=input("select the language")
if language=="English" or language=="Hindi":
    print(language)
    pin=int(input("enter no"))
    if pin>=1000 and pin<=9999:
        print(pin)
        actype=input("enter type of account")
        if actype=="saving" or actype=="currernt":
            print(actype)
            trnsection=(input("enter the transection"))
            withdrawl=int(input("enter amount"))
            balance=10000
            
            if trnsection=="withdrawl":
                # withdrawl=int(input("enter amount"))
                remain=balance-withdrawl
                print("remaning bankbalance",remain)
                print("Thanks for visiting")
            else:
                if trnsection=="deposit":
                    deposit=int(input("enter the ammount"))
                    remain=balance+deposit
                    recept=(input("do you want recept"))
                    if recept=="yes":
                        print("take recept")
                        print("Thanks for visiting")
                    else:
                        print("collect your recept")
                        print("Thanks")
                else:
                    print("add amount")
        else:
            print("choose the correct account")
    else:
        print("insert the correct pin")
else:
    print("select the language")



