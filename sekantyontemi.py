def f(x):
    return(x**2-4*x+3)

x1 = int(input("baslangic değeri: "))
x2 = int(input("bitis değeri: "))

if(f(x1)*f(x2)==0):
    print("girdiğiniz değerlerden biri kök")

else:
    while(abs(f(x1)-f(x2)>0.0001)):
    #for i in range(10):
        x3=x1-f(x1)*(x2-x1)/(f(x2)-f(x1))
#sağdaki ve soldaki değerleri değiştirdik
        x1,x2=x2,x3
# 0a bölünme hatasından dolayı kontrol ediyoruz
        if(f(x1)==f(x2)):
	         break
#if (f(x1)==f(x2))
#refactoring hali daha verimli
#değerler için fonksiyon çıktısını kontrol etmiyor tekrar
    print(x1,x2,f(x1),f(x2))
  
#3 ten büyük 2 değer girersek 3 e yaklaştırır

