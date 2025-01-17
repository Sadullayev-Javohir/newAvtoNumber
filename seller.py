#   SOTUVCHI
import json

from datetime import datetime

purchase_time = datetime.now()

avtoNumber = ["01", "10", "20", "25", "30", "40", "50", "60","70", "75", "80", "85", "90", "95"]

lastID = 0



numberList = []

mainHistoryList = []
mainHistoryDic = {}

numberDict = {}





# keyingi ID funksiyasi
def nextID():
    global lastID
    lastID += 1
    return lastID

# oxirgi ID
def LoadLastID():
    global lastID  
    try:
        with open("numbers.json", "r") as json_file:
            numberList = json.load(json_file)
            if numberList:
                lastID = max(item["ID"] for item in numberList)
    except(FileNotFoundError, ValueError):
        lastID = 0

def space():
    print()
    print()

# Json faylga saqlash
def saveToJson():
    with open("numbers.json", "w") as json_file:
        json.dump(numberList, json_file, indent=4)
    

# Json da malumotlarni o'qish
def JsonRead():
    global numberList
    try:
        with open("numbers.json", "r") as json_file:
            numberList = json.load(json_file)
    except json.JSONDecodeError:
        numberList = []


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


# raqam ekanligini tekshirish
def isNum(cost):
    
    while True:
        if cost.count(".") <= 1 and cost.replace(".", "", 1).isdigit():
            cost = float(cost)
            if cost > 0:
                return cost
            else:
                print('xato 0 dan katta son kiriting.')
                cost = input("Narxni 0 dan katta kiriting: ")
        else:
            print('xato')
            cost = input("Qaytadan narxini so'mda kiriting: ")



LoadLastID()

JsonRead()

mainHistoryJsonRead()


# 1 Yangi raqam qo'shish
def addNumber():
    global id
    while True:
        number = input("Raqam qo'shing: ")
        if any(numDic["number"] == number for numDic in numberList):
            space()
            print("Bu raqam allaqachon mavjud! Iltimos, boshqa raqam kiriting.")
            space()
            continue

        # Ikkinchi ro'yxatni tekshirish
        if any(mainHistDic["AvtoNumber"] == number for mainHistDic in mainHistoryList):
            space()
            print("Bu raqam sotilgan! Iltimos, boshqa raqam kiriting.")
            space()
            continue
        else:
            first = number[:2]
            second = number[2:5]
            third = number[5:8]
            first2 = number[:2]
            second2 = number[2:3]
            third2 = number[3:6]
            four2 = number[6:8]

            if len(number) == 8:

                if (first in avtoNumber and second.isdigit() and third.isalpha() and third == third.upper()) or (first2 in avtoNumber and third2.isdigit() and four2.isalpha() and four2 == four2.upper() and second2.isalpha() and second2 == second2.upper()):
                    id = nextID()

                    cost = input("Narxini so'mda kiriting: ")
                    cost = isNum(cost)

                    numberDict = {
                        "ID": id,
                        "number" : number,
                        "cost": cost,
                        "putTime": purchase_time.strftime("%Y-%m-%d %H:%M:%S"),
                        "status": "Mavjud",
                    }
                    numberList.append(numberDict)
                    space()
                    saveToJson()
                    print("Raqam muvaffaqqiyatli qo'shildi")
                    space()
                    return
                else:
                    space()
                    number = input("Qaytadan kiriting: ")
                    space()
            else:
                print("Uzuligi 8 ta bo'lishi kerak")
                space()
                number = input("Qaytadan kiriting: ")
                space()

# 2 Raqamni tahrirlash
def editNum():

    if numberList == []:
        print()
        print("Ma'lumotlar yo'q")
        print()
        return
    
    for numDic in numberList:
        print(f"ID: {numDic["ID"]}, Holati: {numDic["status"]}, Avtoraqam: {numDic["number"]}, Narxi: {numDic["cost"]} so'm, Vaqti: {numDic["putTime"]}")
    print("Qaysi raqamni tahrirlamoqchisiz")
    editInputNum = input("Tahrirlamoqchi bo'lgan raqamni kiriting: ")
    
    while True:
        for i in range(len(numberList)):
            if numberList[i]["number"] == editInputNum:
                newCost = input("Yangi narx kiriting: ")
                newCost = isNum(newCost)
                numberList[i]["cost"] = newCost
                print()
                print("Raqamning narxi muvaffaqqiyatli yangilandi")
                saveToJson()
                print()
                return
        else:
            print("Qaytadan raqam kiriting: ")
            editInputNum = input("Qaytadan tahrirlamoqchi bo'lgan raqamni kiriting: ")
                
# 3 Raqamni o'chirish

def deleteNum():
    if numberList == []:
        print()
        print("Ma'lumotlar yo'q")
        print()
        return
    for numDic in numberList:
        print(f"ID: {numDic["ID"]}, Holati: {numDic["status"]}, Avtoraqam: {numDic["number"]}, Narxi: {numDic["cost"]} so'm, Vaqti: {numDic["putTime"]}")

    inputDelNum = input("O'chirmoqchi bo'lgan raqamni kiriting: ")

    while True:
        for i in range(len(numberList)):
            if numberList[i]["number"] == inputDelNum:
                del numberList[i]
                print()
                print("Muvaffaqqiyatli O'chirildi")
                saveToJson()
                print()
                return
        else:
            print("Topilmadi. Qaytadan kiriting: ")
            inputDelNum = input("O'chirmoqchi bo'lgan raqamni kiriting: ")



# 4 Sotilgan raqamlar statistikasi
def soldNumStatistic():
    if mainHistoryList == []:
        print()
        print("Sotilgan raqamlar hali yo'q")
        print()
    else:   
        
        for mainHistoryDic in mainHistoryList:
            print()
            print(f"Foydalanuvchi:\n\tID: {mainHistoryDic["userID"]}, Foydalanuvchi ismi: {mainHistoryDic["userName"]}, Manzili: {mainHistoryDic["userAddress"]}, Raqam Sotilgan vaqti: {mainHistoryDic["AvtoNumberSoldTime"]}\nAvto Raqam:\n\tAvto Raqam ID: {mainHistoryDic["AvtoNumberID"]}, Avto Raqam: {mainHistoryDic["AvtoNumber"]}, Avto Raqam narxi: {mainHistoryDic["AvtoNumberCost"]}, Avto Raqam qo'yilgan vaqti: {mainHistoryDic["AvtoNumberPutTime"]}, Avto Raqam xolati: {mainHistoryDic["AvtoNumberStatus"]}")
            print()



def sellerRun():
    print()
    print("\nSotuvchi Menyusi:")
    print()
    print("1. Yangi raqam qo'shish")
    print("2. Raqamni tahrirlash")
    print("3. Raqamni o'chirish")
    print("4. Sotilgan raqamlar statistikasi")
    print("5. Chiqish")

    choose = input("Tanlang: ")

    if choose == "1":
        addNumber()
        sellerRun() 
    elif choose == "2":
        editNum()
        sellerRun() 
    elif choose == "3":
        deleteNum()
        sellerRun() 
    elif choose == "4":
        soldNumStatistic()
        sellerRun() 
    elif choose == "4.1":
        print(numberList)
        sellerRun()
    elif choose == "5":
        print("Kuningiz yaxshi o'tsin")
        return
    else:
        print("\nIltimos, 1-5 oralig'ida tanlang.")
        sellerRun() 
