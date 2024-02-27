import pioneer
import qrscanner

pn = pioneer.Pioneer()
# pn.move_pioneer(0.9,0.9)

while True:
    qrscanner.open_window()
    val = qrscanner.qr_detect()
    print(val)

    if val == "maju": 
        pn.move_pioneer(3,3)

    elif val == "mundur":
        pn.move_pioneer(-1,-1)

    elif val == "kanan":
        pn.move_pioneer(2,-2)

    elif val == "kiri":
        pn.move_pioneer(-2,2)


    else:
        pn.move_pioneer(0,0)


        
   


