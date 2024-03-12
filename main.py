import tkinter as tk

class ReceiptProcess:
    def __init__(self) -> None:
        self.name = ""
        self.coffee_amount = 0
        self.Croissant_amount = 0
        self.Carbonara_amount = 0
        self.subTotal = 0.00
        self.discount = 0.00
        self.discounted_price = 0.00
        self.Total = 0.00
        self.coffee_price = 123.00
        self.croissant_price = 85.00
        self.carbonara_price = 250.00

    def receiptCalculation(self):
        self.name = ent_CustomerName.get()
        
        #Getting Discount
        if radio1.get() == 1:
            self.discount = 0.00
        elif radio1.get() == 2:
            self.discount = 0.05
        elif radio1.get() == 3:
            self.discount = 0.10
        elif radio1.get() == 4:
            self.discount = 0.15
        else: 
            self.discount = 0.00

        #Calculating Order SubTotal
        if self.coffee_amount > 0:
            self.subTotal += self.coffee_amount * self.coffee_price
        elif self.Croissant_amount > 0:
            self.subTotal += self.Croissant_amount * self.croissant_price
        elif self.carbonara_price > 0:
            self.subTotal += self.Carbonara_amount * self.carbonara_price
        else:
            self.subTotal = 0.00

        #Calculate Total after Discount
        if self.discount == 0.05:
            self.discounted_price = self.discount * self.subTotal
            self.Total = self.subTotal - self.discounted_price
        elif self.discount == 0.10:
            self.discounted_price = self.discount * self.subTotal
            self.Total = self.subTotal - self.discounted_price
        elif self.discount == 0.15:
            self.discounted_price = self.discount * self.subTotal
            self.Total = self.subTotal - self.discounted_price
        else:
            self.Total = self.subTotal

        #Receipt Output
           
    def amountToggle(self):
        if menu1.get() == True:
            btn_coffee_amount1.config(state=tk.NORMAL)
            btn_coffee_amount2.config(state=tk.NORMAL)
        else:
            btn_coffee_amount1.config(state=tk.DISABLED)
            btn_coffee_amount2.config(state=tk.DISABLED)
            lbl_Coffee_amount.config(text=0)
        
        if menu2.get() == True:
            btn_Croissant_amount1.config(state=tk.NORMAL)
            btn_Croissant_amount2.config(state=tk.NORMAL)
        else:
            btn_Croissant_amount1.config(state=tk.DISABLED)
            btn_Croissant_amount2.config(state=tk.DISABLED)
            lbl_Croissant_amount.config(text=0)

        if menu3.get() == True:
            btn_Carbonara_amount1.config(state=tk.NORMAL)
            btn_Carbonara_amount2.config(state=tk.NORMAL)
        else:
            btn_Carbonara_amount1.config(state=tk.DISABLED)
            btn_Carbonara_amount2.config(state=tk.DISABLED)
            lbl_Carbonara_amount.config(text=0)

    def amountAddingCoffee(self):
        self.coffee_amount = int(lbl_Coffee_amount.cget("text"))
        self.coffee_amount += 1
        lbl_Coffee_amount.config(text=self.coffee_amount)

    def amountMinusCoffee(self):
        if self.coffee_amount <= 0:
            lbl_Coffee_amount.config(text=0)
        else:
            self.coffee_amount -= 1
            lbl_Coffee_amount.config(text=self.coffee_amount)
    
    def amountAddingCroissant(self):
        self.Croissant_amount = int(lbl_Croissant_amount.cget("text"))
        self.Croissant_amount += 1
        lbl_Croissant_amount.config(text=self.Croissant_amount)

    def amountMinusCroissant(self):
        if self.Croissant_amount <= 0:
            lbl_Croissant_amount.config(text=0)
        else:
            self.Croissant_amount -= 1
            lbl_Croissant_amount.config(text=self.Croissant_amount)

    def amountAddingCarbonara(self):
        self.Carbonara_amount = int(lbl_Carbonara_amount.cget("text"))
        self.Carbonara_amount += 1
        lbl_Carbonara_amount.config(text=self.Carbonara_amount)
    
    def amountMinusCarbonara(self):
        if self.Carbonara_amount <= 0:
            lbl_Carbonara_amount.config(text=0)
        else:
            self.Carbonara_amount -= 1
            lbl_Carbonara_amount.config(text=self.Carbonara_amount)

run = ReceiptProcess()

#Window config
win = tk.Tk()
win.title("Food Kiosk App")
win.geometry("850x500")
win.resizable(False, False)
win.config(bg="#bdcfb5")

#Widgets
#Const var
menu1 = tk.BooleanVar()
menu2 = tk.BooleanVar()
menu3 = tk.BooleanVar()
radio1 = tk.IntVar()

#Labels
lbl_CustomerName = tk.Label(win, text="Customer Name:", font=("Helvetica", 16), bg="#bdcfb5")  
lbl_Menu = tk.Label(win, text="Menu", font=("Helvetica", 16), bg="#bdcfb5")
lbl_Discount = tk.Label(win, text="Discount", font=("Helvetica", 16), bg="#bdcfb5")

lbl_Coffee_price = tk.Label(win, text="123.00", font=("Helvetica", 16), bg="#bdcfb5")
lbl_Croissant_price = tk.Label(win, text="85.00", font=("Helvetica", 16), bg="#bdcfb5")
lbl_Carbonara_price = tk.Label(win, text="250.00", font=("Helvetica", 16), bg="#bdcfb5")

lbl_Coffee_amount = tk.Label(win, text=0, font=("Helvetica", 16), bg="#bdcfb5")
lbl_Croissant_amount = tk.Label(win, text=0, font=("Helvetica", 16), bg="#bdcfb5")
lbl_Carbonara_amount = tk.Label(win, text=0, font=("Helvetica", 16), bg="#bdcfb5")

lbl_receipt = tk.Label(win, text="Receipt", font=("Helvetica", 16), bg="#bdcfb5")
lbl_receipt_CustomerName = tk.Label(win, text="Customer Name:", font=("Helvetica", 16), bg="#bdcfb5")
lbl_receipt_Order = tk.Label(win, text="Orders:", font=("Helvetica", 16), bg="#bdcfb5")
lbl_receipt_Total = tk.Label(win, text="Total:", font=("Helvetica", 16), bg="#bdcfb5")

lbl_CustomerName.place(x=10, y=10)  
lbl_Menu.place(x=180, y=50)
lbl_Discount.place(x=180, y=240)

lbl_Coffee_price.place(x=200, y=85)
lbl_Croissant_price.place(x=200, y=125)
lbl_Carbonara_price.place(x=200, y=165)

lbl_Coffee_amount.place(x=350, y=85)
lbl_Croissant_amount.place(x=350, y=125)
lbl_Carbonara_amount.place(x=350, y=165)

lbl_receipt.place(x=600, y=10)
lbl_receipt_CustomerName.place(x=450, y=50)
lbl_receipt_Order.place(x=450, y=80)
lbl_receipt_Total.place(x=450, y=350)

#Entry
ent_CustomerName = tk.Entry(win, font=("Helvetica", 16))
ent_CustomerName.place(x=180, y=10)

#Checkbutton
ck_btn_Coffee = tk.Checkbutton(win, text="Coffee", font=("Helvetica", 16),
                                variable=menu1, bg="#bdcfb5", activebackground="#bdcfb5", command=run.amountToggle)
ck_btn_Croissant = tk.Checkbutton(win, text="Croissant", font=("Helvetica", 16),
                                  variable=menu2, bg="#bdcfb5", activebackground="#bdcfb5", command=run.amountToggle)
ck_btn_Carbonara = tk.Checkbutton(win, text="Carbonara", font=("Helvetica", 16),
                                  variable=menu3, bg="#bdcfb5", activebackground="#bdcfb5", command=run.amountToggle)

ck_btn_Coffee.place(x=50, y=80)
ck_btn_Croissant.place(x=50, y=120)
ck_btn_Carbonara.place(x=50, y=160)

#Radiobutton
rd_btn_Discount1 = tk.Radiobutton(win, text="0%", variable=radio1, value= 1,
                                  font=("Helvetica", 16), bg="#bdcfb5", activebackground="#bdcfb5")
rd_btn_Discount2 = tk.Radiobutton(win, text="5%", variable=radio1, value= 2,
                                  font=("Helvetica", 16), bg="#bdcfb5", activebackground="#bdcfb5")
rd_btn_Discount3 = tk.Radiobutton(win, text="10%", variable=radio1, value= 3,
                                  font=("Helvetica", 16), bg="#bdcfb5", activebackground="#bdcfb5")
rd_btn_Discount4 = tk.Radiobutton(win, text="15%", variable=radio1, value= 4,
                                  font=("Helvetica", 16), bg="#bdcfb5", activebackground="#bdcfb5")

rd_btn_Discount1.place(x=80, y=280)
rd_btn_Discount2.place(x=150, y=280)
rd_btn_Discount3.place(x=220, y=280)
rd_btn_Discount4.place(x=300, y=280)

#Button
btn_coffee_amount1 = tk.Button(win, text="+", font=("Helvetica", 12), bg="#E5F2C9", activebackground="#E76D83", width=2,
                                state=tk.DISABLED, command=run.amountAddingCoffee)
btn_coffee_amount2 = tk.Button(win, text="-", font=("Helvetica", 12), bg="#E5F2C9", activebackground="#E76D83", width=2,
                                state=tk.DISABLED, command=run.amountMinusCoffee)
btn_Croissant_amount1 = tk.Button(win, text="+", font=("Helvetica", 12), bg="#E5F2C9", activebackground="#E76D83", width=2,
                                   state=tk.DISABLED, command=run.amountAddingCroissant)
btn_Croissant_amount2 = tk.Button(win, text="-", font=("Helvetica", 12), bg="#E5F2C9", activebackground="#E76D83", width=2,
                                   state=tk.DISABLED, command=run.amountMinusCroissant)
btn_Carbonara_amount1 = tk.Button(win, text="+", font=("Helvetica", 12), bg="#E5F2C9", activebackground="#E76D83", width=2,
                                   state=tk.DISABLED, command=run.amountAddingCarbonara)
btn_Carbonara_amount2 = tk.Button(win, text="-", font=("Helvetica", 12), bg="#E5F2C9", activebackground="#E76D83", width=2,
                                   state=tk.DISABLED, command=run.amountMinusCarbonara)

btn_enter = tk.Button(win, text="Enter", font=("Helvetica", 16), bg="#E5F2C9", activebackground="#E76D83", width=15)
btn_clear = tk.Button(win, text="Clear", font=("Helvetica", 16), bg="#E5F2C9", activebackground="#E76D83", width=10)

btn_coffee_amount1.place(x=380, y=85)
btn_coffee_amount2.place(x=310, y=85)

btn_Croissant_amount1.place(x=380, y=125)
btn_Croissant_amount2.place(x=310, y=125)

btn_Carbonara_amount1.place(x=380, y=165)
btn_Carbonara_amount2.place(x=310, y=165)

btn_enter.place(x=135, y=350)
btn_clear.place(x=165, y=430)

#Window Loop
win.mainloop()
