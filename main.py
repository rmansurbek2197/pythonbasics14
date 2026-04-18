def hisobla(lugat):
    yigindisi = 0
    for kalit, qiymat in lugat.items():
        if isinstance(qiymat, (int, float)):
            yigindisi += qiymat
    return yigindisi

lugat = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 'qiqi',
    'e': 40,
}

print(hisobla(lugat))
yigindisi = hisobla(lugat)
if yigindisi > 50:
    print("yig'indisi 50 dan katta")
else:
    print("yig'indisi 50 dan kichik yoki teng")
    
lugat2 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
}

print(hisobla(lugat2))
lugat3 = {
    'a': 100,
    'b': 200,
    'c': 'salom',
    'd': 300,
}
print(hisobla(lugat3))