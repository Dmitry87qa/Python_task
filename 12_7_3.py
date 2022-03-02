money = int(input("Введите сумму вклада: "))

per_cent = {"tkb" : 5.6, "skb": 5.9, "vtb": 4.28, "sber": 4.0}

tkb = float(per_cent.get("tkb"))
skb = float(per_cent.get("skb"))
vtb = float(per_cent.get("vtb"))
sber = float(per_cent.get("sber"))

deposit = [int(tkb * money/100), int(skb * money/100), int(vtb * money/100), int(sber * money/100)]

max_deposit = int(max(deposit))

print(deposit)
print("Максимальная сумма, которую вы можете получить :", max_deposit)







