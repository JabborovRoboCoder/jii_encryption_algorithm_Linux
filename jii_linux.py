import math
# from termcolor import colored
try:
    from termcolor import colored
except ImportError:
    print("Sizning dasturingiz termcolor modulini o'rnatmagan. Uni o'rnatish uchun quyidagi komandani kiriting:")
    print("pip install termcolor")



# Shifrlash
def shifrlashMatn(matn):
    shifr = ""
    
    k_indx = 0

    matn_len = float(len(matn))
    matn_lst = list(matn)
    kalit_lst = sorted(list(kalit))

    ustun = len(kalit)
    
    qator = int(math.ceil(matn_len / ustun))

    fill_null = int((qator * ustun) - matn_len)
    matn_lst.extend('_' * fill_null)
 
    matritsa = [matn_lst[i: i + ustun] 
                for i in range(0, len(matn_lst), ustun)]

    for _ in range(ustun):
        curr_idx = kalit.index(kalit_lst[k_indx])
        shifr += ''.join([qator[curr_idx] 
                        for qator in matritsa])
        k_indx += 1

    royxat = ""
    for element in shifr:
        if element == '1':
            royxat += 'б'
        elif element == '2':
            royxat += 'и'
        elif element == '3':
            royxat += 'у'
        elif element == '4':
            royxat += 'т'
        elif element == '5':
            royxat += 'в'
        elif element == '6':
            royxat += 'о'
        elif element == '7':
            royxat += 'й'
        elif element == '8':
            royxat += 'с'
        elif element == '9':
            royxat += 'ч'
        else:
            royxat += element
    return royxat

# Shifrni ochish
def de_shifrlash(shifr):
    matn = ""

    k_indx = 0

    matn_indx = 0
    matn_len = float(len(shifr))
    matn_lst = list(shifr)

    ustun = len(kalit)
    
    qator = int(math.ceil(matn_len / ustun))

    kalit_lst = sorted(list(kalit))

    dec_shifr = []
    for _ in range(qator):
        dec_shifr += [[None] * ustun]

    for _ in range(ustun):
        curr_idx = kalit.index(kalit_lst[k_indx])

        for j in range(qator):
            dec_shifr[j][curr_idx] = matn_lst[matn_indx]
            matn_indx += 1
        k_indx += 1

    try:
        matn = ''.join(sum(dec_shifr, []))
    except TypeError:
        raise TypeError(colored("Bu shifrni dastur ocha olmaydi",
                        "boshqa so'zni kiritib ko'ring.","red"))

    null_count = matn.count('_')

    if null_count > 0:
        matn = matn[: -null_count]

    royxat = ""
    for element in matn:
        if element == 'б':
            royxat += '1'
        elif element == 'и':
            royxat += '2'
        elif element == 'у':
            royxat += '3'
        elif element == 'т':
            royxat += '4'
        elif element == 'в':
            royxat += '5'
        elif element == 'о':
            royxat += '6'
        elif element == 'й':
            royxat += '7'
        elif element == 'с':
            royxat += '8'
        elif element == 'ч':
            royxat += '9'
        else:
            royxat += element
    return royxat

# Asosiy kod
while True :
    kalit = str(input(colored("Kalit so'zni kiriting :-->  ","green")))
    if kalit.lower() == "chiqish":
        break

    tanlash = str(input(colored("Raqamni kiriting (1 oddiy so'z, 2 shifrlangan so'z):-->  ","blue")))

    if tanlash == "1":
        matn = str(input(colored("Matnni kiriting :-->  ","yellow")))
        shifr = shifrlashMatn(matn)
        print(colored("Shifrlangan matn : {}".
                    format(shifr),"red"))
    
    elif tanlash == "2":
        matn = str(input(colored("Shifrlangan matnni kiriting :-->  ","yellow")))
        de_shifr_matn = de_shifrlash(matn)
        print(colored("De-Shifrlangan matn : {}".
            format(de_shifr_matn),"red"))
    else:
        print("Xato Son: Noto'g'ri raqam kiritildi. Iltimos, faqat 1 yoki 2 raqamini kiriting.")
