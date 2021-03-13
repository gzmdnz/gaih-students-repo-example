#!/usr/bin/env python
# coding: utf-8

# In[8]:


sorular = ['Kaymağı İle Ünlü Olan İlimiz ?', 
           'Çalışanların toplu olarak üye olduğu mesleki sivil toplum örgütlerine verilen isim?',
           'Deniz yolculuğunda toplu insan taşımacılığında kullanılan araçların ortak adı?', 
           'Japonların geleneksel güreşine ne ad verilir?', 
           'Belli bir süre eğitimi tamamladıktan sonra alınan, üniversite, okul ya da eğitim kurumu tarafından verilen belgenin adı?', 
           'Tarihin sıfır noktası olarak bilinen, insanlık tarihinin ilk somut kalıntılarının bulunduğu Göbekli tepe hangi ilimizdedir?', 
           'Dünyanın en büyük deniz kazalarından biri olarak tarihe geçti. 1912 yılında 1.550 kişiye mezar olan ünlü transatlantiğin adı nedir? Ödüllü Filmlere konu olmuştur', 
           'Boşanmış eşlerden birinin diğerine veya çocuklara boşanma sonrası ödediği aylık bedelin adı nedir?',
           "Rusya'nın Başkenti Moskova'da devletin resmi işlerinin de yürütüldüğü ünlü kızıl renkli görkemli sarayının adı nedir?", 
           "Türkiye'de Hava durumu tahminlerini yapan hava durumu bilgilerini kamuoyu ile paylaşan kurumumuzun adı nedir?"]


dogru_cevaplar = ['afyon', 'sendika', 'vapur', 'sumo', 'diploma', 'şanlıurfa', 'titanik','nafaka', 'kremlin', 'meteoroloji']


# In[ ]:


def sor():

    puan = 0

    print('Soru 1:',sorular[0])


    cevap_1 = input('Cevabınız Nedir: ')

    if (cevap_1.lower() == dogru_cevaplar[0]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap Afyon.')

    print('-'*50)
    
    
    print('Soru 2:',sorular[1])


    cevap_2 = input('Cevabınız Nedir: ')

    if (cevap_2.lower() == dogru_cevaplar[1]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap Sendika.')

    print('-'*50)
    
    print('Soru 3:',sorular[2])

   
    cevap_3 = input('Cevabınız Nedir: ')

    if (cevap_3.lower() == dogru_cevaplar[2]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap Vapur.')

    print('-'*50)
    
    
    print('Soru 4:',sorular[3])

   
    cevap_4 = input('Cevabınız Nedir: ')

    if (cevap_4.lower() == dogru_cevaplar[3]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap Sumo.')

    print('-'*50)
    
    print('Soru 5:',sorular[4])

   
    cevap_5 = input('Cevabınız Nedir: ')

    if (cevap_5.lower() == dogru_cevaplar[4]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap Diploma.')

    print('-'*50)
    
    
    print('Soru 6:',sorular[5])

   
    cevap_6 = input('Cevabınız Nedir: ')

    if (cevap_6.lower() == dogru_cevaplar[5]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap Şanlıurfa.')

    print('-'*50)
    
    
    print('Soru 7:',sorular[6])

   
    cevap_7 = input('Cevabınız Nedir: ')

    if (cevap_7.lower() == dogru_cevaplar[6]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap Titanik.')

    print('-'*50)
    
    print('Soru 8:',sorular[7])

   
    cevap_8 = input('Cevabınız Nedir: ')

    if (cevap_8.lower() == dogru_cevaplar[7]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap Nafaka.')

    print('-'*50)
    
    
    print('Soru 9:',sorular[8])

   
    cevap_9 = input('Cevabınız Nedir: ')

    if (cevap_9.lower() == dogru_cevaplar[8]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap Kremlin.')

    print('-'*50)
    
    
    print('Soru 10:',sorular[9])

   
    cevap_10 = input('Cevabınız Nedir: ')

    if (cevap_10.lower() == dogru_cevaplar[9]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap Meteoroloji.')

    print('-'*50)
    




    

    print('Soru Oyunumuz Bitmiştir. Toplamda {} Puan Aldınız.'.format(puan))



sor()


# In[ ]:




