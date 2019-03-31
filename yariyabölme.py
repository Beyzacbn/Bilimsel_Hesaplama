#yariya bölme yöntemiyle köke yaklasiyoruz.

def f(x):
    return (x**2-4*x+3)

x1= int(input("baslangic tahmini"))
x2= int(input("bitis tahmini"))

if(f(x1)*f(x2)==0):   
    print("tahminlerinizden biri denklemin köküdür")

elif(f(x1)*f(x2)>0):
    print("girdiğiniz aralikta tek sayida kok yoktur")

else:
    for i in range (100):
        xr=(x1+x2)/2
        if(f(xr))==0:
            print("kök bulundu: ",xr,i)
            break
        elif(f(x1)*f(xr)<0):    
	# kök x1 ile x2 değil, x1 ile xr arasındadır
             x2=xr

        else:      
        # kök xr ile x2 arasındadır
             x1=xr
        print(xr)
       

