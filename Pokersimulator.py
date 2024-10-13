# gezogene Farbe kartenwert // 13
# gezogene Karte kartenwert % 13

# es gibt 52 Karten

# mögliche Kombinationen
# 1. Paar - zwei gleiche Zahlen
# 2. Zwei Paare - zwei Paare
# 3. Drilling - drei gleiche Zahlen
# 4. Straight - 5 aufeinanderfolgende Zahlen
# 5. Flush - 5 gleiche Farben
# 6. Full House - Drilling und Paar
# 7. Vierling - vier gleiche Zahlen
# 8. Straight Flush - Straight und Flush
# 9. Royal Flush - 10, Bube, Dame, K, Ass und gleiche Farben

import random

def getcolor(cardvalue, amountonecardset):
    number = cardvalue // amountonecardset
    return number

def getnumber(cardvalue, amountonecardset):
    number =  cardvalue  % amountonecardset
    return number

def ispair(cards):
    for c1 in cards:
        for c2 in cards:
            if c2 != c1:
                if getnumber(c1, 13) == getnumber(c2,13):
                    return "true"

def istwopairs(cards):
    value_count = {}
    pairs = 0
    for c in cards:
        card_number = getnumber(c, 13)
        if card_number in value_count:
            value_count[card_number] += 1
        else:
            value_count[card_number] = 1
    for count in value_count.values():
        if count == 2:
            pairs += 1
    if pairs == 2:
        return "true"
    return "false"


def isdrilling(cards):
    value_count = {}
    for c in cards:
        card_number = getnumber(c, 13)
        if card_number in value_count:
            value_count[card_number] += 1
        else:
            value_count[card_number] = 1
    for count in value_count.values():
        if count == 3:
            return "true"
    return "false"

def isstraight(cards):
    sortedcards = []
    for c in cards:
       sortedcards.append(getnumber(c, 13))
    for i in range(1, len(sortedcards)):
        if sortedcards[i] - sortedcards[i - 1] != 1:
            return "false"
    return "true"

def isflush(cards):
    for i in range(1, len(cards)):
        if getcolor(cards[i], 13) != getcolor(cards[i - 1], 13):
            return "false"
    return "true"


def isfullhouse(cards):
    value_count = {}
    has_triple = False
    has_pair = False

    for c in cards:
        card_number = getnumber(c, 13)
        if card_number in value_count:
            value_count[card_number] += 1
        else:
            value_count[card_number] = 1

    for count in value_count.values():
        if count == 3:
            has_triple = True
        elif count == 2:
            has_pair = True

    if has_triple and has_pair:
        return "true"
    return "false"


def isvierling(cards):
    value_count = {}
    for c in cards:
        card_number = getnumber(c, 13)
        if card_number in value_count:
            value_count[card_number] += 1
        else:
            value_count[card_number] = 1
    for count in value_count.values():
        if count == 4:
            return "true"
    return "false"

def isstraightflush(cards):
    if isstraight(cards) == "true" and isflush(cards) == "true":
        return "true"
    return "false"

def isroyalflush(cards):
    if isstraightflush(cards) == "true" and getnumber(cards[0], 13) == 8:
        return "true"
    return "false"

def pokerspiel(amountofcards):
    cards = []
    for i in range(amountofcards):
        card = random.randint(0, 51)
        while card in cards:
            card = random.randint(0, 51)
        cards.append(card)
    if isroyalflush(cards) == "true":
        return "Royal Flush"
    if isstraightflush(cards) == "true":
        return "Straight Flush"
    if isvierling(cards) == "true":
        return "Vierling"
    if isfullhouse(cards) == "true":
        return "Full House"
    if isflush(cards) == "true":
        return "Flush"
    if isstraight(cards) == "true":
        return "Straight"
    if isdrilling(cards) == "true":
        return "Drilling"
    if istwopairs(cards) == "true":
        return "Zwei Paare"
    if ispair(cards) == "true":
        return "Paar"
    return "Nichts"

def pokersimulation(amountofgames):
    kombinationen = {
        "Nichts": 0,
        "Paar": 0,
        "Zwei Paare": 0,
        "Drilling": 0,
        "Straight": 0,
        "Flush": 0,
        "Full House": 0,
        "Vierling": 0,
        "Straight Flush": 0,
        "Royal Flush": 0
    }
    for i in range(amountofgames):
        kombination = pokerspiel(5)
        if kombination in kombinationen:
            kombinationen[kombination] += 1
        else:
            kombinationen[kombination] = 1
    print(kombinationen)
    for key in kombinationen:
        kombinationen[key] = kombinationen[key] / amountofgames * 100
    return kombinationen

#print(ispair([1,3,12,14]))
#print(istwopairs([1,3,16,14]))
#print(isdrilling([5,18,31,7,43]))
#print(isstraight([5,19,7,8,9]))
#print(isflush([14,15,16,17,18]))
#print(isfullhouse([5,18,31,1,14]))
#print(isvierling([5,18,31,7,44]))
#print(isstraightflush([14,15,16,17,18]))
#print(isroyalflush([8,9,10,11,12]))
print(pokersimulation(10000))
print("Richtige Anteile aus Internet:")
print("Nichts: 50,117%, Paar: 42.256%, Zwei Paare: 4.753%, Drilling: 2.113%, Straight: 0.392%, Flush: 0.197%, Full House: 0.144%, Vierling: 0.024%, Straight Flush: 0.001%, Royal Flush: 0.000154%")






