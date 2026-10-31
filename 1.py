import csv

class Oquvchi:
    fayl="Oquvchi.csv"

    def __init__(self,ism,fan,baho):
        self.ism=ism
        self.fan=fan
        self.baho=baho

    def korish(self):
        print("****O'quvchi haqida****")
        print(f"Ismi: {self.ism}")
        print(f"fani: {self.fan}")
        print(f"Bahosi: {self.baho}")
        print("-"*20)

    def __str__(self):
        return f"{self.ism} {self.fan}- {self.baho}"

    @classmethod
    def sarlavha_yoz(cls):
        with open(cls.fayl, "a", encoding="UTF-8", newline="") as f:
            pass

        with open(cls.fayl, "r", encoding="UTF-8") as f:
            birinchi = f.readline()

        if birinchi.strip() != "ism,fan,baho":
            with open(cls.fayl, "r", encoding="UTF-8") as f:
                eski = f.read()
            with open(cls.fayl, "w", encoding="UTF-8", newline="") as f:
                f.write("ism,fan,baho\n" + eski)


    @classmethod
    def qoshish(cls,ism,fan,baho):
        with open(cls.fayl,"a",newline="",encoding="UTF-8") as f:
            writer=csv.writer(f)
            writer.writerow([ism,fan,baho])
            print("Muvaffaqiyatli qo'shildi!")

    @classmethod
    def all(cls):
        with open(cls.fayl,"r",encoding="UTF-8") as f:
            oqish=csv.DictReader(f)
            oquvchilar=[]
            for x in oqish:
                o=Oquvchi(x['ism'],x['fan'],float(x['baho']))
                oquvchilar.append(o)
        return oquvchilar

    @classmethod
    def ortacha(cls):
        oquvchilar=cls.all()
        if len(oquvchilar)==0:
            return 0
        yigindi=0
        for x in oquvchilar:
            yigindi+=x.baho

        return yigindi/len(oquvchilar)

Oquvchi.sarlavha_yoz()

while True:
    print("====Menu====")
    print("1 Barcha natijalar")
    print("2 Baho qo'shish")
    print("3 O'rtacha baho")
    print("4 Chiqish")
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        for o in Oquvchi.all():
            o.korish()

    elif tanlov == "2":
        ism = input("O'quvchi ismi: ")
        fan = input("Fan: ")
        baho = int(input("Baho: "))
        Oquvchi.qoshish(ism, fan, baho)

    elif tanlov == "3":
        print(f"O'rtacha baho: {Oquvchi.ortacha():.2f}")

    elif tanlov == "4":
        print("Dastur tugadi")
        break
