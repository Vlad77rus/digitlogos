def sums (s: str):
    dig = ['0','1','2','3','4','5','6','7','8','9']
    z = 0 
    for si in s:
        if si in dig:
            z = z + int(si) 
    return z

def SumToOne (s: str):
    R=10
    while R > 9:
        R = sums(s)
        s=str(R)
    return R    
        
def ch1(s: str):    
    dig = ['1','2','3','4','5','6','7','8','9']
    if s[0] in dig:
        z = int(s[0])
    else:
        z = int(s[1]) 
    return z   

def matrix (s: str):
    dig = ['1','2','3','4','5','6','7','8','9']
    z = [0,0,0,0,0,0,0,0,0,0]
    for si in s:
        for i in dig:
            if si == i:
                z[int(i)] += 1
    #z  = z[1:] 
               
    return z        

def stroki (m: list):
    z = [0,0,0,0,0,0,0,0,0]
    z[1] = m[1]+m[4]+m[7] # цели
    z[2] = m[2]+m[5]+m[8] # семья             
    z[3] = m[3]+m[6]+m[9] # стабильность
    z[4] = m[1]+m[2]+m[3] # самоощенка
    z[5] = m[4]+m[5]+m[6] # деньги
    z[6] = m[7]+m[8]+m[9] # талант
    z[7] = m[3]+m[5]+m[7] # плотские
    z[8] = m[1]+m[5]+m[9] # духовные
    return z        

def det(m: list):
    Det = (m[1]*m[5]*m[9]+m[4]*m[8]*m[3]+m[2]*m[6]*m[7])-(m[3]*m[5]*m[7]+m[2]*m[4]*m[9]+m[6]*m[8]*m[1])
    delta = (m[1]*m[5]-m[2]*m[4])    
    return Det, delta        

def detinfo (Det, delta : int):
    inf1 = ['0', 'наводящий порядок', 'копирующий', 'создающий свой мир', 'ищущий новое', 'революционер', 'бунтарь, разрушитель']
    inf = ['0', 'Наблюдение', 'Приспосабливание', 'Преодоление', 'Поиск', 'Преобразование', 'Создание']
    if Det == 0 and delta == 0: z = 1
    elif Det != 0 and delta < 0: z = 2
    elif Det != 0 and delta > 0: z = 3
    elif Det != 0 and delta == 0: z = 4
    elif Det == 0 and delta < 0: z = 5
    elif Det == 0 and delta > 0: z = 6
    else: z = 0
    return z, inf[z]  

def all_numeric(d, m, g: str):
    s = d + m + g
    z1 = 0
    z2 = 0
    z3 = 0
    z4 = 0

    z1 = sums(s)
    z2 = sums(str(z1))
    z3 = z1-ch1(d)*2
    z4 = sums(str(z3))
    sz = str(z1) + str(z2) + str(z3) + str(z4)
    sob = s + sz
    Mtx = matrix(sob)
    strok = stroki(Mtx)
    Det, delta = det(Mtx)
    D, detinf = detinfo(Det, delta)
    DestinyNum = SumToOne(s)

    z = {'day': d ,
         'month': m ,
         'year': g ,           
         'add_num1': z1 ,
         'add_num2': z2 ,
         'add_num3': z3 ,
         'add_num4': z4,
         'matrix' : Mtx , 
         'stroki' : strok , 
         'Determinant': Det , 
         'delta' : delta , 
         'detNo' : D,
         'detInfo' : detinf,  
         'destinyNum': DestinyNum
        }

    return z

def type_of_thinking (d, m, g: str, let: int):

    z = []
    for i in range(let+1):
        data = all_numeric(d,m,g)
        g = str(int(g) + 1)
        z.append(data)
    return z    

def mod(x: int):
    if x<0: x = -x
    return x

def analyzToF(DetLet: dict): 
    
    mm = []
    for i in range(len(DetLet)):
        mm.append(DetLet[i]['detNo'])
    
    Etapmm = [0]
    
    for i in range(len(mm))[1:]: 

        if (mm[i-1]-mm[i]) == 0:
        # 2. Этапы застоя или накопления информации
        # Этапы когда уровень мышления на протяжении нескольких лет не меняется.
            Etapmm.append(2)


        elif (Etapmm[i-1]) == 2  and (mm[i-1]-mm[i]) != 0:
            # 3. Этапы практической реализации накопления информации
            # (Этап который начинается после застоя или накопления информации) 
            Etapmm.append(3)


        elif (mm[i]-mm[i-1]) >= 2 and mm[i] != 6:
            # 4. Пики всплесков и подъемов понтенциала возможностей (таланта) 
            # (резкий скачек вверх на два и более уровней, не выше уровня 5. )
            Etapmm.append(4)

        elif mm[i] == 6:
            # 5. Пик перелома или коренного изменения, разрушения 
            # (Подъем до уровня 6.)
            Etapmm.append(5)

        else:
            if ((mm[i-1]-mm[i]) >= 2  and (mm[i-1]-mm[i]) != 0) or mm[i] == 1:
            # 6. Спады и возможные кризисы 
            # (резкое снижение на два и более или до уровня 1.)
                Etapmm.append(6)


            elif mod((mm[i]-mm[i-1])) < 2  and (mm[i-1]-mm[i]) != 0:
            # 1. Этапы возникновения волны между уровнями
            # Этапы на которых уровни меняются между двумя соседними уровнями, образуя волну. 
                Etapmm.append(1)

            elif mod((mm[i-1]-mm[i])) > 2 and mm[i] != 1 and mm[i] != 6 and mm[i-1] != 6:
            # 7. Разброд мыслей и неопределенность 
            # (Резкие поочередные скачки более чем на 2 уровня, не выходя за 1 и 6)
                Etapmm.append(7)


        f = open('log.txt', 'a', encoding='UTF-8')
        f.write(str(mm[i])+'  '+str(Etapmm) + '\n')
        
        f.close()


    print(mm)
    print(Etapmm)
    return Etapmm   

def yearinfo (DyN, Let: int):
    Dst = str(Let)
    symb = Dst[-1:]
    s = Dst + symb + str(DyN)
    i = SumToOne(s)
    InYrSt = ['0',
              'Удачный год, удача во всем !',  
              'Плохой год, неудачный.',
              'Спокойный, стабильный год.',
              'Средний год.',
              'Хороший год.', 
              'Год отдыха.', 
              'Хороший год.', 
              'Неудачи в личной жизни.', 
              'Непринужденный и спокойный год.'
             ] 
    z = {'yr_num': i,  
         'yr_inf': InYrSt[i]   
        }        

    return z

def RazmerStr (s: str, Dlina: int):
    if len(s) < Dlina:
        Vp = Dlina - len(s)
        z = s +' '*Vp
    else: z=s    
    return z   

def num_of_fate (i: int):
    Inf = ['0',
           'Солнце - успех, удача, лидер, заметный человек, руководитель.',
           'Луна - эмоциональные с тонкой, ранимой натурой и сильной интуицией, художники, поэты, артисты ',
           'Юпитер - удача, счастье',
           'Уран - трудовлюбивые, сосредоточенные. Неожиданность',
           'Меркурий - языки, наука; журналисты, продавцы ',
           'Венера - Люди творчества поэты, музыканты. Cтабильные семьи много детей',
           'Нептун - Мыслители, философы, духовные люди, йоги',
           'Сатурн -  мудрые, надежные, стабильные люди',
           'Марс - Пожарные, военные, спасатели. Жизнь - борьба'
          ] 
    z = Inf[i]
    return z       
          
def energyDay (d, m, y, dlt, nof : int): 
    
    import datetime
    a = datetime.date(y, m, d)       
    EDinf = ['0', 
             'Лидерство, планирование, взятие на себя ответственности. (Соннечная активная муж. энергия)',
             'Разделение ответственности, партнерство. (Если в матрице нет или одна 2 то - болезненность, сомнения, страхи)',  
             'Удержание баланса, гармонии. Хорошо для учебы и творчества. (Возможны илюзии от дня, неоправданные ожидания)',
             'Энергичность и готовность всем помогать, драйв. (Если нет 4, то может быть трудный день)', 
             'Внутренний баланс, упокойствие, уриротворение. (Если нет 5, апатичность, обида на партнеров, притензии к миру)',
             'Управление людьми через давление, контроль, манипуляцию. (Если нет 6 - болезненность)',
             'Удача, ускорение всех процессов, направление на созидание, легкость, терпимость.',
             'Служение другим, уступчивость, изменчивость. Хорошая дата для духовной деятельности, родовых практик.',
             'Сила, воля, получение знаний, активность, спорт. Могут быть ссоры, склоки, недовольство, разрушение.'
            ]
    z =[]
    for i in range(dlt):
        b = a + datetime.timedelta(days=i)
        ny = str(b.year)
        nm = str(b.month)
        nd = str(b.day)
        NDt = ny+nm+nd
        Fd = SumToOne(str(SumToOne(NDt))+str(nof))
       
        z.append({'Data': NDt,
                  'EDnum': Fd,  
                  'EDInf': EDinf[Fd]   
                })


    return z

def zdorov ():
    pass
    ['желчный пузырь',                   # 0
     'мочевой пузырь',                   # 1
     'толстая кишка',                    # 2
     'желудок',                          # 3 
     'тонкая кишка',                     # 4
     'селезенка и поджелудочная железа', # 5
     'почки',                            # 6
     'сердце',                           # 7
     'печень',                           # 8
     'легкие'                            # 9
    ]    

def grafLife (d, m, y: str):
    z = int(d+m)*int(y)
    return z