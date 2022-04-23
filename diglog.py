import defs

d, m, g = input ('ДАТА, МЕСЯЦ, ГОД -').split()
print('день -', d)
print('месяц -', m)
print('год -', g)

NumData = defs.all_numeric(d,m,g)

print (NumData)
s = d + m + g
z1 = 0
z2 = 0
z3 = 0
z4 = 0

z1 = NumData['add_num1']
z2 = NumData['add_num2']
z3 = NumData['add_num3']
z4 = NumData['add_num4']
sz = str(z1) + str(z2) + str(z3) + str(z4)
sob = s + sz
Mtx = NumData['matrix']
strok = NumData['stroki']
Det = NumData['Determinant']
delta = NumData['delta']
D = NumData['detNo']
detinf = NumData['detInfo']
DyN = NumData['destinyNum']


v1=('Дата - '+s+ '\n\n')
v2=('Доп числа - '+str(z1)+' '+ str(z2)+' ' + str(z3)+' ' + str(z4)+ '\n\n')
v3=''
for i in [1,2,3]:
    v3=v3+(str(Mtx[i]) +'     '+  str(Mtx[i+3]) +'     '+ str(Mtx[i+6]) + '    |'+str(strok[i])+ '\n')
v4 = ('_________________|'+ '\n')
v5 = (str(strok[4])+'     '+str(strok[5])+'     '+str(strok[6])+'    '+str(strok[7])+'/'+str(strok[8])+ '\n\n')
v6 = 'Число судьбы - '+str(DyN)+'   '+ defs.num_of_fate(DyN) + '\n'
v7 =''
for i in [1,2,3,4,5,6]:
    v7 =  v7 + f"{defs.info_s()[i]} - {str(strok[i])} \n"
v7 = v7 + f"{defs.info_s()[7]}\{defs.info_s()[8]} - {str(strok[7])}\{str(strok[8])} \n"    
vv = v1 + v2 + v6 +'\n'+ v3 + v4 + v5 + v7 + '\n'

let = input('Лет - ')
DetLet = defs.type_of_thinking(d,m,g,int(let))
x = []
y = []
ToF = []

ToF = defs.analyzToF(DetLet)
GF = defs.grafLife(d, m, g)
GFs = str(GF)
while int(let) > len(GFs):
    GFs = GFs + str(GF)

# mm = []
# for i in range(len(DetLet)):
#     mm.append(DetLet[i]['detNo'])



# d1, m1, g1 = input ('прогноз на ДАТА, МЕСЯЦ, ГОД -').split()
# dlt = input ('прогноз на сколько дней -')
# wd = int(d1)
# wm = int(m1)
# wg = int(g1)
# ENDAY = defs.energyDay(int(d1), int(m1), int(g1), int(dlt), DyN)


f_name = input('Введите ваше имя - ')+'_diglog.txt'



f = open(f_name, 'w', encoding='UTF-8')
f.write(vv + '\n')
f.write(' Лет/год   |      Стиль мышления        |       Энергитический прогноз на год      |\n')
for j in range(len(DetLet)):
    vp = defs.yearinfo(DyN, j)
    Yr_inf = str(vp['yr_num'])+' - '+defs.RazmerStr(vp['yr_inf'], 35)+'|'
    f.write(defs.RazmerStr(str(j),3)+' - '+
            DetLet[j]['year']+' |  ' + #GFs[j]+' |  '+ 
            str(DetLet[j]['detNo'])+' - '+
            defs.RazmerStr(DetLet[j]['detInfo'], 22) + '|   '+ 
            Yr_inf + '\n'
            )

f.write('\n\n')


# for j in range(len(ENDAY)):
#     f.write(defs.RazmerStr(ENDAY[j]['Data'],10) +' - ' +
#             str(ENDAY[j]['EDnum']) +' - ' +
#             ENDAY[j]['EDInf']+ '\n'
#             )


# f.write(str(mm)+ '\n')
# f.write(str(ToF)+ '\n')
f.close()

def graf (DetLet):
    import matplotlib.pyplot as plt
    for i in range(len(DetLet)):
        y.append(DetLet[i]['detNo'])
        x.append(i)
    plt.plot(x,y)
    plt.show()
