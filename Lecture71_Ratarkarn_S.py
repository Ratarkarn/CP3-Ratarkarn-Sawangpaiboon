def showBill():
    totalPrice = 0
    print("---- My Food ----")
    for i in range(len(menuList)) :
        print(menuList[i],priceList[i])
        totalPrice += int(priceList[i])
    print("Total Price : %d THB" %totalPrice)

menuList = []
priceList = []
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit" :
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
