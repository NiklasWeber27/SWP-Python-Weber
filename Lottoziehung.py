import random

def lottoziehung():
    #print("Lottoziehung")
    gezogeneZahlen = []
    for i in range(6):
        zahl = random.randint(1, 45)
        while zahl in gezogeneZahlen:
            zahl = random.randint(1, 45)
        gezogeneZahlen.append(zahl)
    #for zahl in gezogeneZahlen:
    #   print(zahl)
    return gezogeneZahlen

def lottoziehungStatistik(dic, zahlen):
    for zahl in zahlen:
        dic[zahl] += 1

#lottoziehung()

stat = {i + 1: 0 for i in range(45)}

for i in range(1000):
    lottoziehungStatistik(stat, lottoziehung())

print(stat)
