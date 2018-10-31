#distancia em cada 1min

#def d(t):
#    print((v*t)/60)

v=12 
do=0
d=do
listad=[]

for t in range (25):
    listad.append(0)
    d = d + v*(1/60)
    listad.append(d)

print (listad)


    

