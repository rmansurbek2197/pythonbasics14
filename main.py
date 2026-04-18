def ajratib_oling(matn):
    kichik_harflar = [harf for harf in matn if harf.islower()]
    return kichik_harflar

matn = "Salom Dunyo"
print(ajratib_oling(matn))