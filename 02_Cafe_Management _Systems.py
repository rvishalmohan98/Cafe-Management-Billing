from tkinter import*
import random
import time
import datetime
from tkinter import *
root = Tk()
root.geometry("1350x750+0+0")
root.title("Cafe Management Systems")
root.configure(background='powder blue')

#==================================create Freames====================================

Tops = Frame(root, width=1350, height=100, bd=14, relief='raise')
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=650, bd=8, relief='raise')
f1.pack(side=LEFT)

f2 = Frame(root, width=440, height=650, bd=8, relief='raise')
f2.pack(side=RIGHT)

f1a = Frame(f1, width=900, height=330, bd=8, relief='raise')
f1a.pack(side=TOP)

f2a = Frame(f1, width=900, height=320, bd=6, relief='raise')
f2a.pack(side=BOTTOM)
                                                             
ft2 = Frame(f2, width=440, height=450, bd=12, relief='raise')
ft2.pack(side=TOP)

fb2 = Frame(f2, width=440, height=250, bd=16, relief='raise')
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=330, bd=16, relief='raise')
f1aa.pack(side=LEFT)

f1ab = Frame(f1a, width=400, height=330, bd=16, relief='raise')
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=14, relief='raise')
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width=450, height=330, bd=14, relief='raise')
f2ab.pack(side=RIGHT)

Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')

#=====METHODS=====
#===========================Cost of Items==================================
def CostofItems():
    Item1=float(E_Latte.get())
    Item2=float(E_Expresso.get())
    Item3=float(E_Iced_Latte.get())
    Item4=float(E_Vale_Caffee.get())
    Item5=float(E_Cappuccino.get())
    Item6=float(E_African_Caffee.get())
    Item7=float(E_Americana_Caffee.get())
    Item8=float(E_Iced_Cappuccino.get())

    Item9=float(E_Coffee_Cake.get())
    Item10=float(E_Red_Velvet_Cake.get())
    Item11=float(E_Black_Forest_Cake.get())
    Item12=float(E_Boston_Cream_Cake.get())
    Item13=float(E_Lagos_Chocolate_Cake.get())
    Item14=float(E_Kilburn_Chocolate_Cake.get())
    Item15=float(E_Carlton_Hill_Chocolate_Cake.get())
    Item16=float(E_Queen_Park_Chocolate_Cake.get())

    PriceofDrinks = (Item1 * 25) + (Item2 * 20) + (Item3 * 30)\
                    + (Item4 * 35) + (Item5 * 40) + (Item6 * 40)\
                    +(Item7 * 45) + (Item8 * 50)

    PriceofCakes = (Item9 * 100) + (Item10 * 120) + (Item11 * 115)\
                    + (Item12 * 110) + (Item13 * 130) + (Item14 * 145)\
                    +(Item15 * 150) + (Item16 * 150)

    DrinksPrice = "Rs.",str("%.2f" %(PriceofDrinks))
    CakesPrice = "Rs.",str("%.2f" %(PriceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC="Rs.",str("%.2f" %(25))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs.",str("%.2f" %(PriceofDrinks + PriceofCakes + 25))
    SubTotal.set(SubTotalofITEMS)

    Tax="Rs.",str("%.2f" %((PriceofDrinks + PriceofCakes + 25)*0.15))
    PaidTax.set(Tax)
    TT=((PriceofDrinks + PriceofCakes + 25)*0.15)
    TC="Rs.",str("%.2f" %(PriceofDrinks + PriceofCakes + 25 + TT))
    TotalCost.set(TC)
    
def qExit():
    root.destroy()
       
def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)
    
    E_Latte.set("0")
    E_Expresso.set("0")
    E_Iced_Latte.set("0")
    E_Vale_Caffee.set("0")
    E_Cappuccino.set("0")
    E_African_Caffee.set("0")
    E_Americana_Caffee.set("0")
    E_Iced_Cappuccino.set("0")

    E_Coffee_Cake.set("0")
    E_Red_Velvet_Cake.set("0")
    E_Black_Forest_Cake.set("0")
    E_Boston_Cream_Cake.set("0")
    E_Lagos_Chocolate_Cake.set("0")
    E_Kilburn_Chocolate_Cake.set("0")
    E_Carlton_Hill_Chocolate_Cake.set("0")
    E_Queen_Park_Chocolate_Cake.set("0")

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")
    
    txtLatte.configure(state=DISABLED)
    txtExpresso.configure(state=DISABLED)
    txtIced_Latte.configure(state=DISABLED)
    txtVale_Caffee.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtAfrican_Caffee.configure(state=DISABLED)
    txtAmericana_Caffee.configure(state=DISABLED)
    txtIced_Cappuccino.configure(state=DISABLED)

    txtCoffee_Cake.configure(state=DISABLED)
    txtRed_Velvet_Cake.configure(state=DISABLED)
    txtBlack_Forest_Cake.configure(state=DISABLED)
    txtBoston_Cream_Cake.configure(state=DISABLED)
    txtLagos_Chocolate_Cake.configure(state=DISABLED)
    txtKilburn_Chocolate_Cake.configure(state=DISABLED)
    txtCarlton_Hill_Chocolate_Cake.configure(state=DISABLED)
    txtQueen_Park_Chocolate_Cake.configure(state=DISABLED)

def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10908,500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL"+randomRef)

    txtReceipt.insert(END,"Receipt Ref:\t\t\t"+Receipt_Ref.get() + "\t\t" + DateofOrder.get()+"\n")
    txtReceipt.insert(END,"Items\t\t\t"+"Cost of Items \n\n")
    txtReceipt.insert(END,"Latte:\t\t\t\t"+E_Latte.get()+"\n")
    txtReceipt.insert(END,"Expresso:\t\t\t\t"+ E_Expresso.get()+"\n")
    txtReceipt.insert(END,"Iced Latte:\t\t\t\t"+ E_Iced_Latte.get()+"\n")
    txtReceipt.insert(END,"Vale Caffee:\t\t\t\t"+E_Vale_Caffee.get()+"\n")
    txtReceipt.insert(END,"Cappuccino:\t\t\t\t"+E_Cappuccino.get()+"\n")
    txtReceipt.insert(END,"African Caffee:\t\t\t\t"+E_African_Caffee.get()+"\n")
    txtReceipt.insert(END,"Americana Caffee:\t\t\t\t"+E_Americana_Caffee.get()+"\n")
    txtReceipt.insert(END,"Iced Cappuccino:\t\t\t\t"+E_Iced_Cappuccino.get()+"\n")
    txtReceipt.insert(END,"Coffee Cake:\t\t\t\t"+E_Coffee_Cake.get()+"\n")
    txtReceipt.insert(END,"Red Velvet Cake:\t\t\t\t"+E_Red_Velvet_Cake.get()+"\n")
    txtReceipt.insert(END,"Black Forest Cake:\t\t\t\t"+E_Black_Forest_Cake.get()+"\n")
    txtReceipt.insert(END,"Boston Cream Cake:\t\t\t\t"+E_Boston_Cream_Cake.get()+"\n")
    txtReceipt.insert(END,"Lagos Chocolate Cake:\t\t\t\t"+E_Lagos_Chocolate_Cake.get()+"\n")
    txtReceipt.insert(END,"Kilburn Chocolate Cake:\t\t\t\t"+E_Kilburn_Chocolate_Cake.get()+"\n")
    txtReceipt.insert(END,"Carlton Hill Chocolate Cake:\t\t\t\t"+E_Carlton_Hill_Chocolate_Cake.get()+"\n")
    txtReceipt.insert(END,"Queen Park Chocolate Cake:\t\t\t\t"+E_Queen_Park_Chocolate_Cake.get()+"\n")
    txtReceipt.insert(END,"Cost of drinks:\t\t\t"+CostofDrinks.get()+"\nTax Paid\t\t\t"+PaidTax.get()+"\n")
    txtReceipt.insert(END,"Cost of Caks:\t\t\t"+CostofCakes.get()+"\nSub Total\t\t\t"+SubTotal.get()+"\n")
    txtReceipt.insert(END,"Service Charge:\t\t\t"+ServiceCharge.get()+"\nTotal Cost\t\t\t"+TotalCost.get()+"\n")

#================================Heading=============================
lblInfo = Label(Tops, font=('arial',70,'bold'),text = "  Cafe Management Systems  ", bd=10)
lblInfo.grid(row=0,column=0)
#========================================checkbutton=======================

def chkbutton_value():
    if(var1.get() == 1):
        txtLatte.configure(state=NORMAL)
    elif var1.get() == 0:
        txtLatte.configure(state=DISABLED)
        E_Latte.set("0")
        
    if(var2.get() == 1):
        txtExpresso.configure(state=NORMAL)
    elif var2.get() == 0:
        txtExpresso.configure(state=DISABLED)
        E_Expresso.set("0")
        
    if(var3.get() == 1):
        txtIced_Latte.configure(state=NORMAL)
    elif var3.get() == 0:
        txtIced_Latte.configure(state=DISABLED)
        E_Iced_Latte.set("0")

    if(var4.get() == 1):
        txtVale_Caffee.configure(state=NORMAL)
    elif var4.get() == 0:
        txtVale_Caffee.configure(state=DISABLED)
        E_Vale_Caffee.set("0")

    if(var5.get() == 1):
        txtCappuccino.configure(state=NORMAL)
    elif var5.get() == 0:
        txtCappuccino.configure(state=DISABLED)
        E_Cappuccino.set("0")

    if(var6.get() == 1):
        txtAfrican_Caffee.configure(state=NORMAL)
    elif var6.get() == 0:
        txtAfrican_Caffee.configure(state=DISABLED)
        E_African_Caffee.set("0")

    if(var7.get() == 1):
        txtAmericana_Caffee.configure(state=NORMAL)
    elif var7.get() == 0:
        txtAmericana_Caffee.configure(state=DISABLED)
        E_Americana_Caffee.set("0")

    if(var8.get() == 1):
        txtIced_Cappuccino.configure(state=NORMAL)
    elif var8.get() == 0:
        txtIced_Cappuccino.configure(state=DISABLED)
        E_Iced_Cappuccino.set("0")

    if(var9.get() == 1):
        txtCoffee_Cake.configure(state=NORMAL)
    elif var9.get() == 0:
        txtCoffee_Cake.configure(state=DISABLED)
        E_Coffee_Cake.set("0")

    if(var10.get() == 1):
        txtRed_Velvet_Cake.configure(state=NORMAL)
    elif var10.get() == 0:
        txtRed_Velvet_Cake.configure(state=DISABLED)
        E_Red_Velvet_Cake.set("0")

    if(var11.get() == 1):
        txtBlack_Forest_Cake.configure(state=NORMAL)
    elif var11.get() == 0:
        txtBlack_Forest_Cake.configure(state=DISABLED)
        E_Black_Forest_Cake.set("0")

    if(var12.get() == 1):
        txtBoston_Cream_Cake.configure(state=NORMAL)
    elif var12.get() == 0:
        txtBoston_Cream_Cake.configure(state=DISABLED)
        E_Boston_Cream_Cake.set("0")

    if(var13.get() == 1):
        txtLagos_Chocolate_Cake.configure(state=NORMAL)
    elif var13.get() == 0:
        txtLagos_Chocolate_Cake.configure(state=DISABLED)
        E_Lagos_Chocolate_Cake.set("0")

    if(var14.get() == 1):
        txtKilburn_Chocolate_Cake.configure(state=NORMAL)
    elif var14.get() == 0:
        txtKilburn_Chocolate_Cake.configure(state=DISABLED)
        E_Kilburn_Chocolate_Cake.set("0")

    if(var15.get() == 1):
        txtCarlton_Hill_Chocolate_Cake.configure(state=NORMAL)
    elif var15.get() == 0:
        txtCarlton_Hill_Chocolate_Cake.configure(state=DISABLED)
        E_Carlton_Hill_Chocolate_Cake.set("0")

    if(var16.get() == 1):
        txtQueen_Park_Chocolate_Cake.configure(state=NORMAL)
    elif var16.get() == 0:
        txtQueen_Park_Chocolate_Cake.configure(state=DISABLED)
        E_Queen_Park_Chocolate_Cake.set("0")
        

#================================Variables===========================
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

E_Latte = StringVar()
E_Expresso = StringVar()
E_Iced_Latte = StringVar()
E_Vale_Caffee = StringVar()
E_Cappuccino = StringVar()
E_African_Caffee = StringVar()
E_Americana_Caffee = StringVar()
E_Iced_Cappuccino = StringVar()

E_Coffee_Cake = StringVar()
E_Red_Velvet_Cake = StringVar()
E_Black_Forest_Cake = StringVar()
E_Boston_Cream_Cake = StringVar()
E_Lagos_Chocolate_Cake = StringVar()
E_Kilburn_Chocolate_Cake = StringVar()
E_Carlton_Hill_Chocolate_Cake = StringVar()
E_Queen_Park_Chocolate_Cake = StringVar()

E_Latte.set("1")
E_Expresso.set("1")
E_Iced_Latte.set("1")
E_Vale_Caffee.set("1")
E_Cappuccino.set("1")
E_African_Caffee.set("1")
E_Americana_Caffee.set("1")
E_Iced_Cappuccino.set("1")

E_Coffee_Cake.set("1")
E_Red_Velvet_Cake.set("1")
E_Black_Forest_Cake.set("1")
E_Boston_Cream_Cake.set("1")
E_Lagos_Chocolate_Cake.set("1")
E_Kilburn_Chocolate_Cake.set("1")
E_Carlton_Hill_Chocolate_Cake.set("")
E_Queen_Park_Chocolate_Cake.set("1")

DateofOrder.set(time.strftime("%d/%m/%Y"))


#===================================Drinks====================================================

Latte = Checkbutton(f1aa,text="Latte:Rs.25", variable = var1, onvalue=1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=0,sticky=W)

Expresso = Checkbutton(f1aa,text="Expresso:Rs.20", variable = var2, onvalue=1, offvalue=0,
                       font=('arial',18,'bold'),command=chkbutton_value).grid(row=1,sticky=W)

Iced_Latte = Checkbutton(f1aa,text="Iced Latte:Rs.30", variable = var3, onvalue=1, offvalue=0,
                         font=('arial',18,'bold'),command=chkbutton_value).grid(row=2,sticky=W)

Vale_Caffee = Checkbutton(f1aa,text="Vale Caffee:Rs.35", variable = var4, onvalue=1, offvalue=0,
                          font=('arial',18,'bold'),command=chkbutton_value).grid(row=3,sticky=W)

Cappuccino = Checkbutton(f1aa,text="Cappuccinoa:Rs.40", variable = var5, onvalue=1, offvalue=0,
                         font=('arial',18,'bold'),command=chkbutton_value).grid(row=4,sticky=W)

African_Caffee  = Checkbutton(f1aa,text="African Caffee:Rs.40", variable = var6, onvalue=1, offvalue=0,
                              font=('arial',18,'bold'),command=chkbutton_value).grid(row=5,sticky=W)

Americana_Caffee = Checkbutton(f1aa,text="Americana Caffee:Rs.45", variable = var7, onvalue=1, offvalue=0,
                               font=('arial',18,'bold'),command=chkbutton_value).grid(row=6,sticky=W)

Iced_Cappuccino = Checkbutton(f1aa,text="Iced Cappuccino:Rs.50", variable = var8, onvalue=1, offvalue=0,
                              font=('arial',18,'bold'),command=chkbutton_value).grid(row=7,sticky=W)

#===========================================Cakes==========================================


Coffee_Cake = Checkbutton(f1ab,text="Coffee Cake:Rs.100", variable = var9, onvalue=1, offvalue=0,
                          font=('arial',18,'bold'),command=chkbutton_value).grid(row=0,sticky=W)

Red_Velvet_Cake = Checkbutton(f1ab,text="Red Velvet Cake:Rs.120", variable = var10, onvalue=1, offvalue=0,
                              font=('arial',18,'bold'),command=chkbutton_value).grid(row=1,sticky=W)

Black_Forest_Cake = Checkbutton(f1ab,text="Black Forest Cake:Rs.115", variable = var11, onvalue=1, offvalue=0,
                                font=('arial',18,'bold'),command=chkbutton_value).grid(row=2,sticky=W)

Boston_Cream_Cake = Checkbutton(f1ab,text="Boston Cream Cake:Rs.110", variable = var12, onvalue=1, offvalue=0,
                                font=('arial',18,'bold'),command=chkbutton_value).grid(row=3,sticky=W)

Lagos_Chocolate_Cake = Checkbutton(f1ab,text="Lagos Chocolate Cake:Rs.130", variable = var13, onvalue=1, offvalue=0,
                                   font=('arial',18,'bold'),command=chkbutton_value).grid(row=4,sticky=W)

Kilburn_Chocolate_Cake = Checkbutton(f1ab,text="Kilburn Chocolate Cake:Rs.145", variable = var14, onvalue=1, offvalue=0,
                                     font=('arial',18,'bold'),command=chkbutton_value).grid(row=5,sticky=W)

Carlton_Hill_Chocolate_Cake = Checkbutton(f1ab,text="Carlton Hill Chocolate Cake:Rs.150", variable = var15, onvalue=1, offvalue=0,
                                          font=('arial',18,'bold'),command=chkbutton_value).grid(row=6,sticky=W)

Queen_Park_Chocolate_Cake = Checkbutton(f1ab,text="Queen Park Chocolate Cake:Rs.150", variable = var16, onvalue=1, offvalue=0,
                                        font=('arial',18,'bold'),command=chkbutton_value).grid(row=7,sticky=W)

#====================================Enter Weight of drinks=========================================

txtLatte = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6,\
                 justify='left',textvariable=E_Latte,state= DISABLED)
txtLatte.grid(row=0,column=1)

txtExpresso = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6,\
                    justify='left',textvariable=E_Expresso,state= DISABLED)
txtExpresso.grid(row=1,column=1)

txtIced_Latte = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6,\
                      justify='left',textvariable=E_Iced_Latte,state= DISABLED)
txtIced_Latte.grid(row=2,column=1)

txtVale_Caffee = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6,\
                       justify='left',textvariable=E_Vale_Caffee,state= DISABLED)
txtVale_Caffee.grid(row=3,column=1)

txtCappuccino = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6,\
                      justify='left',textvariable=E_Cappuccino,state= DISABLED)
txtCappuccino.grid(row=4,column=1)

txtAfrican_Caffee = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6,\
                          justify='left',textvariable=E_African_Caffee,state= DISABLED)
txtAfrican_Caffee.grid(row=5,column=1)

txtAmericana_Caffee = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6,\
                            justify='left',textvariable=E_Americana_Caffee,state= DISABLED)
txtAmericana_Caffee.grid(row=6,column=1)

txtIced_Cappuccino = Entry(f1aa,font=('arial',16,'bold'), bd=8, width=6,\
                           justify='left',textvariable=E_Iced_Cappuccino,state= DISABLED)
txtIced_Cappuccino.grid(row=7,column=1)


#=========================================Enter Weight of Cakes=========================================

txtCoffee_Cake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                       justify='left',textvariable=E_Coffee_Cake,state= DISABLED)
txtCoffee_Cake.grid(row=0,column=1)

txtRed_Velvet_Cake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                           justify='left',textvariable=E_Red_Velvet_Cake,state= DISABLED)
txtRed_Velvet_Cake.grid(row=1,column=1)

txtBlack_Forest_Cake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                             justify='left',textvariable=E_Black_Forest_Cake,state= DISABLED)
txtBlack_Forest_Cake.grid(row=2,column=1)

txtBoston_Cream_Cake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                             justify='left',textvariable=E_Boston_Cream_Cake,state= DISABLED)
txtBoston_Cream_Cake.grid(row=3,column=1)

txtLagos_Chocolate_Cake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                                justify='left',textvariable=E_Lagos_Chocolate_Cake,state= DISABLED)
txtLagos_Chocolate_Cake.grid(row=4,column=1)

txtKilburn_Chocolate_Cake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                                  justify='left',textvariable=E_Kilburn_Chocolate_Cake,state= DISABLED)
txtKilburn_Chocolate_Cake.grid(row=5,column=1)

txtCarlton_Hill_Chocolate_Cake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                                       justify='left',textvariable=E_Carlton_Hill_Chocolate_Cake,state= DISABLED)
txtCarlton_Hill_Chocolate_Cake.grid(row=6,column=1)

txtQueen_Park_Chocolate_Cake = Entry(f1ab,font=('arial',16,'bold'), bd=8, width=6,\
                                     justify='left',textvariable=E_Queen_Park_Chocolate_Cake,state= DISABLED)
txtQueen_Park_Chocolate_Cake.grid(row=7,column=1)
       
#========================================Information========================================
lblReceipt = Label(ft2,font=('arial',12,'bold'),text="Receipt:",bd=2,anchor='w')
lblReceipt.grid(row=0,column=0,sticky=W)
txtReceipt = Text(ft2, width=59,height=22,bg="White",bd=8,font=('arial',11,'bold'))
txtReceipt.grid(row=1,column=0)
#====================================Cost Items Information=====================================

lblCostofDrinks=Label(f2aa,font=('arial',16,'bold'),text="     Cost of Drinks     ",bd=8,anchor='w')
lblCostofDrinks.grid(row=2,column=0,sticky=W)
txtCostofDrinks=Entry(f2aa,font=('arial',16,'bold'),bd=8,
                      insertwidth=2,justify="left",textvariable=CostofDrinks)
txtCostofDrinks.grid(row=2,column=1)

lblCostofCakes=Label(f2aa,font=('arial',16,'bold'),text="     Cost of Cakes     ",bd=8,anchor='w')
lblCostofCakes.grid(row=3,column=0,sticky=W)
txtCostofCakes=Entry(f2aa,font=('arial',16,'bold'),bd=8,
                     insertwidth=2,justify="left",textvariable=CostofCakes)
txtCostofCakes.grid(row=3,column=1)

lblServiceCharge=Label(f2aa,font=('arial',16,'bold'),text="     Service Charge     ",bd=8,anchor='w')
lblServiceCharge.grid(row=4,column=0,sticky=W)
txtServiceCharge=Entry(f2aa,font=('arial',16,'bold'),bd=8,
                       insertwidth=2,justify="left",textvariable=ServiceCharge)
txtServiceCharge.grid(row=4,column=1)
#=======================================Payment Information============================================
lblPaidTax=Label(f2ab,font=('arial',16,'bold'),text="     Paid Tax     ",bd=8)
lblPaidTax.grid(row=2,column=0,sticky=W)
txtPaidTax=Entry(f2ab,font=('arial',16,'bold'),bd=8,
                 insertwidth=2,justify="left",textvariable=PaidTax)
txtPaidTax.grid(row=2,column=1)

lblSubTotal=Label(f2ab,font=('arial',16,'bold'),text="     Sub Total     ",bd=8)
lblSubTotal.grid(row=3,column=0,sticky=W)
txtSubTotal=Entry(f2ab,font=('arial',16,'bold'),bd=8,
                  insertwidth=2,justify="left",textvariable=SubTotal)
txtSubTotal.grid(row=3,column=1)

lblTotalCost=Label(f2ab,font=('arial',16,'bold'),text="     Total Cost     ",bd=8)
lblTotalCost.grid(row=4,column=0,sticky=W)
txtTotalCost=Entry(f2ab,font=('arial',16,'bold'),bd=8,
                      insertwidth=2,justify="left",textvariable=TotalCost)
txtTotalCost.grid(row=4,column=1)

#======================================Buttons===============================================
btnTotal=Button(fb2,padx=16,pady=1, bd=2, fg="black",font=('arial',16,'bold'),width=3,
                text="Total",command=CostofItems).grid(row=0,column=0)

btnReceipt=Button(fb2,padx=16,pady=1, bd=2, fg="black",font=('arial',16,'bold'),width=4,
                text="Receipt",command=Receipt).grid(row=0,column=1)

btnReset=Button(fb2,padx=16,pady=1, bd=2, fg="black",font=('arial',16,'bold'),width=3,
                text="Reset",command=Reset).grid(row=0,column=2)

btnExit=Button(fb2,padx=16,pady=1, bd=2, fg="black",font=('arial',16,'bold'),width=2,
                text="Exit",command=qExit).grid(row=0,column=3)

#========================================================================================

root.mainloop()






