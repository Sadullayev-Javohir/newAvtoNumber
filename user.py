import json
from datetime import datetime

class Datas:
    def __init__(self, cash, numberList, soldNumList, mainHistoryDic, mainHistoryList, soldNumDic, lastID):
        self.cash = cash
        self.numberList = numberList
        self.soldNumList = soldNumList
        self.mainHistoryDic = mainHistoryDic
        self.mainHistoryList = mainHistoryList
        self.soldNumDic = soldNumDic
        self.lastID = lastID

cash = Datas.cash = 0
numberList = Datas.numberList = []
soldNumList = Datas.soldNumList = []
mainHistoryDic = Datas.mainHistoryDic = {}
mainHistoryList = Datas.mainHistoryList = []
soldNumDic = Datas.soldNumDic = {}
lastID = Datas.lastID = 0

# Hozirgi vaqtni olish
purchaseTime = datetime.now()




# keyingi ID ni olish
def nextID():
    global lastID
    lastID += 1
    return lastID


# oxirgi ID
def LoadLastID():
    global lastID
    try:
        with open("users.json", "r") as json_file:
            soldNumList = json.load(json_file)
            if soldNumList:
                lastID = max(item["ID"] for item in soldNumList)
    except (FileNotFoundError, ValueError):
        lastID = 0


# foydalanuvchi ma'lumotlarini saqlash
def saveToJson():
    with open("users.json", "w") as json_file:
        json.dump(soldNumList, json_file, indent=4)


# Sotuvchining ma'lumotlarini yangilash
def saveToSellerJson():
    with open("numbers.json", "w") as json_file:
        json.dump(numberList, json_file, indent=4)


# barcha tarixlarni saqlash
def saveToMainHistoryJson():
    with open("mainHistory.json", "w") as json_file:
        json.dump(mainHistoryList, json_file, indent=4)


# barcha tarixlarni o'qish
def mainHistoryJsonRead():
    global mainHistoryList
    try:
        with open("mainHistory.json", "r") as json_file:
            mainHistoryList = json.load(json_file)
    except json.JSONDecodeError:

        mainHistoryList = []


# numberList dagi ma'lumotlarni o'qish
def JsonRead():
    global numberList
    try:
        with open("numbers.json", "r") as json_file:
            numberList = json.load(json_file)
    except json.JSONDecodeError:
        numberList = []


# foydalanuvchi ma'lumotlarini o'qish
def UsersJsonRead():
    global soldNumList
    try:
        with open("users.json", "r") as json_file:
            soldNumList = json.load(json_file)
    except json.JSONDecodeError:
        soldNumList = []


# foydalanuvchi ismini tekshirish
class UserNameCheck:
    def usernameCheck():
        username = input("Ismingizni kiriting: ")

        if (
            username.isalpha() == True
            and username[0].isupper() == True
            and len(username) > 2
        ):
            return username
        else:
            print("Xato qaytadan kiriting: Misol, Javohir")
            return UserNameCheck.usernameCheck()

# foydalunvchining familyasini tekshirish
class UserLastNameCheck:
    def userLastNameCheck():
        userLastName = input("Familyangizni kiriting: ")

        if (
            userLastName.isalpha() == True
            and userLastName[0].isupper() == True
            and len(userLastName) > 2
        ):
            return userLastName
        else:
            print("Xato qaytadan kiriting: Misol, Sadullayev")
            return UserLastNameCheck.userLastNameCheck()

# Parolni tekshirish

class UserPasswordCheck:
    def userPasswordCheck():
        password = input("Parol yarating: ")
        
        if password.isdigit() and len(password) > 7:
            return password
        else:
            print("Xato qaytadan kiriting: Faqat raqam va uzuligi 8 ta bo'lishi kerak")
            return UserPasswordCheck.userPasswordCheck()


# foydalanuvchi manzilini tekshirish
class AddressNameCheck:
    def addressnameCheck():
        address = input("Manzilingizni kiriting: ")

        if address.isalpha() == True and address[0].isupper() == True and len(address) > 2:
            return address
        else:
            return AddressNameCheck.addressnameCheck()



JsonRead()

UsersJsonRead()

mainHistoryJsonRead()

LoadLastID()


# 1. Mavjud raqamlarni ko'rish
class ViewNum:
    def viewNum():
        if numberList == []:
            print()
            print("Hali ma'lumotlar yo'q")
            print()
            return
        for numDic in numberList:
            print()
            print(
                f"ID: {numDic["ID"]}, Avtoraqam: {numDic["number"]}, Narxi: {numDic["cost"]} so'm, Qo'yilgan vaqti: {numDic["putTime"]}, Xolati: {numDic["status"]}"
            )
            print()


# 2. Raqam sotib olish
class BuyNum:
    def buyNum():
        if numberList == []:
            print()
            print("Hali ma'lumotlar yo'q")
            print()
            return

        ViewNum.viewNum()
        
        def save():
            inputNum = input("Sotib olmoqchi bo'lgan avtoraqamni kiriting: ")
            for i in range(len(numberList)):
                if numberList[i]["number"] == inputNum:
                    if numberList[i]["cost"] <= cash:
                        print(f"Qolgan pul: {cash - numberList[i]['cost']} so'm")
                        
                        userName = UserNameCheck.usernameCheck()
                        userLastName = UserLastNameCheck.userLastNameCheck()
                        userAddress = AddressNameCheck.addressnameCheck()
                        numberList[i]["status"] = "Sotilgan"
                        
                        soldNumDic = {
                            "ID": nextID(),
                            "userName": userName,
                            "userLastName": userLastName,
                            "userAddress": userAddress,
                            "soldNumber": numberList[i]["number"],
                            "soldTime": purchaseTime.strftime("%Y-%m-%d %H:%M:%S"),
                        }
                        mainHistoryDic = {
                            "AvtoNumberID": numberList[i]["ID"],
                            "AvtoNumber": numberList[i]["number"],
                            "AvtoNumberCost": numberList[i]["cost"],
                            "AvtoNumberPutTime": numberList[i]["putTime"],
                            "AvtoNumberStatus": numberList[i]["status"],
                            "userID": soldNumDic["ID"],
                            "userName": soldNumDic["userName"],
                            "userLastName": soldNumDic["userLastName"],
                            "userAddress": soldNumDic["userAddress"],
                            "AvtoNumberSoldTime": soldNumDic["soldTime"],
                        }
                        soldNumList.append(soldNumDic)
                        mainHistoryList.append(mainHistoryDic)
                        del numberList[i]

                        saveToJson()
                        saveToSellerJson()
                        saveToMainHistoryJson()

                        print("\nMuvaffaqqiyatli sotib oldingiz\n")
                        return
                    else:
                        cashMinus = numberList[i]["cost"] - cash
                        print()
                        print(f"Sizga {cashMinus} so'm kerak")
                        print("Pul yetarli emas. Bosh menyuga qaytishingiz mumkin.")
                        print()
                        return
            else:
                print("Avtoraqam topilmadi. Qayta urinib ko'ring.")
                return 

        save()



# 3. Xarid tarixini ko'rish
class BuyHistory:

    def buyHistory():
        if soldNumList == []:
            print()
            print("Hali xarid qilmagansiz")
            print()
        else:
            for soldNumDic in soldNumList:
                print()
                print(
                    f"ID: {soldNumDic["ID"]}, Foydalanuvchi ismi: {soldNumDic["userName"]}, Foydalanuvchi familyasi: {soldNumDic["userLastName"]}, Manzili: {soldNumDic["userAddress"]}, Sotilgan vaqti: {soldNumDic["soldTime"]}"
                )
                print()

class CashView:

    def cashView():
        print("1.Pul qo'shing")
        print("2.Pul ko'rish")
        chooseCash = input("Tanlang (1-2): ")
        if chooseCash == "1":

            def cashAdd():
                cashInput = input("Pul kiriting: ")
                if cashInput.isdigit():
                    cashInput = int(cashInput)
                    global cash
                    cash += cashInput
                    print()
                    print(f"Pul qo'shildi {cash} so'm")
                    print()
                    return
                else:
                    print("Qaytadan kiriting: ")
                    cashAdd()

            cashAdd()
        elif chooseCash == "2":
            print()
            print(f"Sizda {cash} so'm pul bor")
            print()
        else:
            print()
            print("Qaytadan kiriting: ")
            print()
            CashView.cashView()

class User:
    def user():
        print()
        print("Foydalanuvchi Menyusi:")
        print()
        print("1. Mavjud raqamlarni ko'rish")
        print("2. Raqam sotib olish")
        print("3. Xarid tarixini ko'rish")
        print("4. Mablag'ni ko'rish")
        print("5. Sozlamalar")
        print("6. Sozlamalardagi ma'lumotlarni ko'rish")
        print("7. Chiqish")

        choose = input("Tanlang: ")

        if choose == "1":
            ViewNum.viewNum()
            User.user()
        elif choose == "2":
            BuyNum.buyNum()
            User.user()
        elif choose == "3":
            BuyHistory.buyHistory()
            User.user()
        elif choose == "4":
            CashView.cashView()
            User.user()
        elif choose == "5":
            Setting.setting()
            User.user()
        elif choose == "6":
            UserDataSettingView.userDataSettingView()
            User.user()
        elif choose == "7":
            print()
            print("Kuningiz yaxshi o'tsin")
            print()
            return
        else:
            print("1-4 gacha son kiriting: ")
            User.user()

class Setting:
    def setting():
            userDataSettingList.clear()
            userName = UserNameCheck.usernameCheck()
            userLastName = UserLastNameCheck.userLastNameCheck()
            userPassword = UserPasswordCheck.userPasswordCheck()
            userDataSettingDict = {
                "userName": userName,
                "userLastName": userLastName,
                "userPassword": userPassword,
            }
            userDataSettingList.append(userDataSettingDict)
            print()
            print("Siz sozlamalarni muvafaqqiyatli yangiladingiz!")
            print()
            User.user()

userDataSettingList = []
userDataSettingDict = {}

class UserSignCheck:
    def userSignCheck():
        if userDataSettingList != []:
            print()
            print("Siz ro'yxatdan o'tgansiz.")
            print()
            return
        
        else:
            print()
            print("Ro'yxatdan o'tish menyusi.")
            print()
            userName = UserNameCheck.usernameCheck()
            userLastName = UserLastNameCheck.userLastNameCheck()
            userPassword = UserPasswordCheck.userPasswordCheck()
            userDataSettingDict = {
                "userName": userName,
                "userLastName": userLastName,
                "userPassword": userPassword,
            }
            userDataSettingList.append(userDataSettingDict)
            print()
            print("Siz muvafaqqiyatli ro'yxatdan o'tdingiz!")
            print()
            User.user()  # Muvaffaqiyatli ro'yxatdan o'tgandan keyin menyuni ko'rsatish

class UserLogIn:
    def userLogIn():
        if not userDataSettingList:
            print("\nFoydalanuvchilar ro'yxati bo'sh! Avval ro'yxatdan o'ting.")
            return UserSignCheck.userSignCheck()
        
        while True:
            username = input("Ism kiriting: ")
            settingDic = next(
                (d for d in userDataSettingList if d["userName"] == username), None
            )
            if not settingDic:
                print("Ism noto'g'ri! Qayta urinib ko'ring.")
                continue

            userlastname = input("Familyangizni kiriting: ")
            if settingDic["userLastName"] != userlastname:
                print("Familiya noto'g'ri! Qayta urinib ko'ring.")
                continue

            userpassword = input("Parol kiriting: ")
            if settingDic["userPassword"] != userpassword:
                print("Parol noto'g'ri! Qayta urinib ko'ring.")
                continue

            print("\nSiz muvafaqqiyatli kirdingiz!")
            break
        
        User.user()  # Muvaffaqiyatli kirgandan keyin menyuni ko'rsatish


class UserDataSettingView:
    def userDataSettingView():
        if userDataSettingList == []:
            print()
            print("Hali ma'lumotlar yo'q")
            print()
            return
        for settingDic in userDataSettingList:
            print()
            print(
                f"Ismingiz: {settingDic["userName"]}, Familyangiz: {settingDic["userLastName"]}, Parolingiz: {settingDic["userPassword"]}"
            )
            print()