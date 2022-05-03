fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


price_mexican_pesos = [
    35000000.0,
    2000000.0,
    2700000.0,
    6347000.0,
    6994543.16,
    6617835.61,
    670000.0,
]
price_colombian_pesos = []
for price in price_mexican_pesos:
    price_colombian_pesos.append(price * 190)

print(price_colombian_pesos)

# above code with fewer lines
price_colombian_pesos = [price * 190 for price in price_mexican_pesos]

print(price_colombian_pesos)


records = [
    'sell,apartment,|México|Distrito Federal|Benito Juárez|,"19.384467,-99.135872",1860000.0,MXN,1843173.75,97996.85,,70.0,,26571.42857142857',
    'sell,apartment,|México|Distrito Federal|Iztapalapa|Cerro de La Estrella|,"19.324123,-99.074132",700000.0,MXN,693667.44,36880.53,,50.0,,14000.0',
    'sell,house,|México|Distrito Federal|La Magdalena Contreras|San Jerónimo Lídice|,"19.317653,-99.236291",3350000.0,MXN,3319694.98,176499.72,,350.0,,9571.42857142857',
    'sell,apartment,|México|Distrito Federal|Cuauhtémoc|,"19.446313,-99.14006",405108.0,MXN,401443.16,21343.71,,50.0,,8102.16',
    'sell,house,|México|Distrito Federal|Coyoacán|,"19.303906,-99.107812",7200000.0,MXN,7134866.79,379342.68,,250.0,,28800.0',
    'sell,apartment,|México|Distrito Federal|Benito Juárez|,"19.374171,-99.181264",2425000.0,MXN,2403062.73,127764.72,,96.0,,25260.416666666668',
    'sell,apartment,|México|Distrito Federal|Tlalpan|,"19.287428,-99.122283",1250000.0,MXN,1238692.07,65858.1,,65.0,,19230.76923076923',
    'sell,house,|México|Distrito Federal|Venustiano Carranza|,"19.436436,-99.117256",1362000.0,MXN,1349678.96,71758.99,,98.0,,13897.959183673467',
    'sell,apartment,|México|Distrito Federal|Benito Juárez|,"19.382429,-99.160199",2250000.0,MXN,2229645.73,118544.58,,90.0,,25000.0',
    'sell,house,|México|Distrito Federal|Tlalpan|Granjas Coapa|,"19.300456,-99.115741",3900000.0,MXN,3864719.42,205477.28,,153.0,,25490.19607843137',
    'sell,apartment,|México|Distrito Federal|Álvaro Obregón|,"19.363167,-99.276028",9000000.0,MXN,8918583.49,474178.35,,188.0,,47872.34042553192',
    'sell,house,|México|Distrito Federal|Coyoacán|Villa Coyoacán|,"19.348694,-99.16291",1150000.0,USD,21629775.0,1150000.0,,555.0,,2072.072072072072',
    'sell,house,|México|Distrito Federal|Tlalpan|,"19.300963,-99.144237",7500000.0,MXN,7432152.81,395148.62,,385.0,,19480.51948051948',
    'sell,house,|México|Distrito Federal|Coyoacán|Paseos de Taxqueña|,"19.343979,-99.124863",6310000.0,MXN,6252917.98,332451.71,,183.0,,34480.87431693989',
    'sell,apartment,|México|Distrito Federal|Coyoacán|San Diego Churubusco|,"19.354509,-99.149765",10000000.0,MXN,9909537.15,526864.83,,293.0,,34129.69283276451',
]
print([row for row in records if "house" in row])
