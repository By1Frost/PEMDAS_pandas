import pandas as pd

df_sampah = pd.read_excel('sampah_jabarprov\disperkim_jum_sampah.xlsx', sheet_name='data')

tahun = sorted(set(df_sampah['tahun']))
kota = list(df_sampah['nama_kabupaten_kota'])
kode = sorted(set(df_sampah['kode_kabupaten_kota']))

kota_lst = []
for i in range(len(kode)):
    kota_lst.append(kota[i])

def no1():
    print("========== N0.1 ==========")
    df_sampah.iloc[:,[4,5,6,7]]
    print(df_sampah.iloc[:,[4,5,6,7]])

    df_sampah.iloc[:,[4,5,6,7]].to_excel('No1.xlsx', index=True)
    df_sampah.iloc[:,[4,5,6,7]].to_csv('No1.csv', index=True)

def no2():
    print("========== N0.2 ==========")
    dictno2 = {}
    sampah_perthn = []
    for i in range(len(tahun)):
        tot_sampah = 0
        for index, row in df_sampah.iterrows():
            if (row['tahun']==tahun[i]):
                tot_sampah = row['jumlah_produksi_sampah'] + tot_sampah    
        sampah_perthn.append(round(float(tot_sampah),2))
        
        dictno2 = {
            'Tahun' : tahun,
            'Total sampah (Ton)' : sampah_perthn
        }
    print(dictno2)
    df_no2 = pd.DataFrame(dictno2)
    df_no2

    df_no2.to_excel('No2.xlsx', index=True)
    df_no2.to_csv('No4.csv', index=True)

def no3():
    print("========== N0.3 ==========")
    dictno3 = {}
    sampah_perthn = []
    for i in range(len(tahun)):
        tot_sampah = 0
        for index, row in df_sampah.iterrows():
            if (row['tahun']==tahun[i]):
                tot_sampah = row['jumlah_produksi_sampah'] + tot_sampah    
        sampah_perthn.append(round(float(tot_sampah),2))
        
        dictno3 = {
            'Tahun' : tahun,
            'Total sampah (Ton)' : sampah_perthn
        }
    print(dictno3)
    df_no3 = pd.DataFrame(dictno3)
    df_no3

    df_no3.to_excel('No3.xlsx', index=True)
    df_no3.to_csv('No3.csv', index=True)

def no4():
    print("========== N0.5 ==========")
    lstsmph = []
    dictno4 = {
        'Kode Kabupaten Kota' : kode,
        'Kabupaten/Kota' : kota_lst
    } 
    for i in range(len(tahun)):
        print(f"Tahun {2015+i}:")
        for index, row in df_sampah.iterrows():
            if (row['tahun']==tahun[i]):
                lstsmph.append(row['jumlah_produksi_sampah'])    

        dictno4[str(2015+i)] = lstsmph.copy()
        print(lstsmph)
        lstsmph.clear()
    print("DICTIONARY NO.4")
    print(dictno4)
    df_no4 = pd.DataFrame(dictno4)
    df_no4

    df_no4.to_excel('No4.xlsx', index=True)
    df_no4.to_csv('No4.csv', index=True)

no1()
no2()
no3()
no4()

