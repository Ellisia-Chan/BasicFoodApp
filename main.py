import tkinter as tk
import datetime

class ReceiptProcess:
    def __init__(self, window):
        #access widgets in Window class
        self.window_widgets = window

        #var
        self.customerName = ""
        self.coffee_amount = 0
        self.croissant_amount = 0
        self.carbonara_amount = 0
        self.price = {"coffee": 123.00, "croissant": 85.00, "carbonara": 250.00}
        self.coffee_order_price = 0.00
        self.croissant_order_price = 0.00
        self.carbonara_order_price = 0.00
        self.receipt_txt = ""
        self.subtotal = 0.00
        self.discount = 0.00
        self.discount_percent = ""
        self.discounted_price = 0.00
        self.Total = 0.00

        #misc
        self.space = ""
    def amountToggle(self):
        if self.window_widgets.menu1.get() == True:
            self.window_widgets.btn_coffee_add.config(state=tk.NORMAL)
            self.window_widgets.btn_coffee_minus.config(state=tk.NORMAL)
        else:
            self.window_widgets.btn_coffee_add.config(state=tk.DISABLED)
            self.window_widgets.btn_coffee_minus.config(state=tk.DISABLED)
            self.window_widgets.lbl_coffee_amount.config(text=0)
        if self.window_widgets.menu2.get() == True:
            self.window_widgets.btn_croissant_add.config(state=tk.NORMAL)
            self.window_widgets.btn_croissant_minus.config(state=tk.NORMAL)
        else:
            self.window_widgets.btn_croissant_add.config(state=tk.DISABLED)
            self.window_widgets.btn_croissant_minus.config(state=tk.DISABLED)
            self.window_widgets.lbl_croissant_amount.config(text=0)
        if self.window_widgets.menu3.get() == True:
            self.window_widgets.btn_carbonara_add.config(state=tk.NORMAL)
            self.window_widgets.btn_carbonara_minus.config(state=tk.NORMAL)
        else:
            self.window_widgets.btn_carbonara_add.config(state=tk.DISABLED)
            self.window_widgets.btn_carbonara_minus.config(state=tk.DISABLED)
            self.window_widgets.lbl_carbonara_amount.config(text=0)

    def amountAdd_Minus(self, value):
        self.coffee_amount = self.window_widgets.lbl_coffee_amount.cget("text")
        self.croissant_amount = self.window_widgets.lbl_croissant_amount.cget("text")
        self.carbonara_amount = self.window_widgets.lbl_carbonara_amount.cget("text")

        #Coffee Add/Minus
        if value == "coffee+":
            self.coffee_amount += 1
            self.window_widgets.lbl_coffee_amount.config(text=self.coffee_amount)
        if value == "coffee-":
            if self.coffee_amount <= 0:
                self.coffee_amount = 0
            else:
                self.coffee_amount -= 1
                self.window_widgets.lbl_coffee_amount.config(text=self.coffee_amount)
        
        #Croissant Add/Minus
        if value == "croissant+":
            self.croissant_amount += 1
            self.window_widgets.lbl_croissant_amount.config(text=self.croissant_amount)
        if value == "croissant-":
            if self.croissant_amount <= 0:
                self.croissant_amount = 0
            else:
                self.croissant_amount -= 1
                self.window_widgets.lbl_croissant_amount.config(text=self.croissant_amount)

        #Carbonara Add/Minus
        if value == "carbonara+":
            self.carbonara_amount += 1
            self.window_widgets.lbl_carbonara_amount.config(text=self.carbonara_amount)
        if value == "carbonara-":
            if self.carbonara_amount <= 0:
                self.carbonara_amount = 0
            else:
                self.carbonara_amount -= 1
                self.window_widgets.lbl_carbonara_amount.config(text=self.carbonara_amount)

    def amountReceiptProcessing(self):
        self.customerName = self.window_widgets.ent_customerName.get()
        self.window_widgets.btn_enter.config(state=tk.DISABLED)
        self.window_widgets.btn_clear.config(bg="#931f1d")

        #Subtotal Calculation
        if self.coffee_amount > 0:
            self.subtotal += self.coffee_amount * self.price["coffee"]
            self.coffee_order_price = self.coffee_amount * self.price["coffee"]
            self.receipt_txt += f"Coffee{self.space:<25} x{self.coffee_amount:<5} ₱{self.coffee_order_price}\n"
        if self.croissant_amount > 0:
            self.subtotal += self.croissant_amount * self.price["croissant"]
            self.croissant_order_price = self.croissant_amount * self.price["croissant"]
            self.receipt_txt += f"Croissant{self.space:<20} x{self.croissant_amount:<5} ₱{self.croissant_order_price}\n"
        if self.carbonara_amount > 0:
            self.subtotal += self.carbonara_amount * self.price["carbonara"]
            self.carbonara_order_price = self.carbonara_amount * self.price["carbonara"]
            self.receipt_txt += f"Carbonara{self.space:<20} x{self.carbonara_amount:<5} ₱{self.carbonara_order_price}\n"


        #Total Calculation with/without Disccount
        self.setDiscount()

        self.discounted_price = self.discount * self.subtotal
        self.Total = self.subtotal - self.discounted_price

        #Receipt Processing
        self.window_widgets.lbl_receipt_timeDate.config(text=str(datetime.datetime.now()))
        self.window_widgets.lbl_receipt_customerName.config(text="Customer Name:" + " " * 5 + self.customerName)
        self.window_widgets.lbl_receipt_orders.config(text=self.receipt_txt)
        self.window_widgets.lbl_receipt_subtotal.config(text="Subtotal:" + " " * 35 + f"₱{self.subtotal}")
        self.window_widgets.lbl_receipt_discount.config(text="Discount:" + " " * 38 + f"{self.discount_percent}")
        self.window_widgets.lbl_receipt_total.config(text="Total:" + " " * 40 + f"₱{self.Total}")

        #Widgets Disabled
        self.window_widgets.ent_customerName.config(state=tk.DISABLED)

        self.window_widgets.ck_btn_coffee.config(state=tk.DISABLED)
        self.window_widgets.ck_btn_croissant.config(state=tk.DISABLED)
        self.window_widgets.ck_btn_carbonara.config(state=tk.DISABLED)
        
        self.window_widgets.btn_coffee_add.config(state=tk.DISABLED)
        self.window_widgets.btn_croissant_add.config(state=tk.DISABLED)
        self.window_widgets.btn_carbonara_add.config(state=tk.DISABLED)

        self.window_widgets.btn_coffee_minus.config(state=tk.DISABLED)
        self.window_widgets.btn_croissant_minus.config(state=tk.DISABLED)
        self.window_widgets.btn_carbonara_minus.config(state=tk.DISABLED)

        self.window_widgets.rd_btn_discount1.config(state=tk.DISABLED)
        self.window_widgets.rd_btn_discount2.config(state=tk.DISABLED)
        self.window_widgets.rd_btn_discount3.config(state=tk.DISABLED)
        self.window_widgets.rd_btn_discount4.config(state=tk.DISABLED)

    def setDiscount(self):
        self.DiscountVar = self.window_widgets.radio1.get()

        if self.DiscountVar == 2:
            self.discount = 0.5
            self.discount_percent = "5%"
        elif self.DiscountVar == 3:
            self.discount = 0.10
            self.discount_percent = "10%"
        elif self.DiscountVar == 4:
            self.discount = 0.15
            self.discount_percent = "15%"
        else:
            self.discount = 0.00
            self.discount_percent = "0%"

    def clear(self):
        self.coffee_order_price = 0.00
        self.croissant_order_price = 0.00
        self.carbonara_order_price = 0.00
        self.receipt_txt = ""
        self.subtotal = 0.00
        self.discount = 0.00
        self.discount_percent = ""
        self.discounted_price = 0.00
        self.Total = 0.00

        self.window_widgets.ck_btn_coffee.deselect()
        self.window_widgets.ck_btn_croissant.deselect()
        self.window_widgets.ck_btn_carbonara.deselect()

        self.window_widgets.lbl_receipt_timeDate.config(text="")

        self.window_widgets.ent_customerName.config(state=tk.NORMAL)
        self.window_widgets.ent_customerName.delete(0, tk.END)

        self.window_widgets.btn_coffee_add.config(state=tk.NORMAL)
        self.window_widgets.btn_croissant_add.config(state=tk.NORMAL)
        self.window_widgets.btn_carbonara_add.config(state=tk.NORMAL)

        self.window_widgets.btn_coffee_minus.config(state=tk.NORMAL)
        self.window_widgets.btn_croissant_minus.config(state=tk.NORMAL)
        self.window_widgets.btn_carbonara_minus.config(state=tk.NORMAL)

        self.window_widgets.lbl_coffee_amount.config(text=0)
        self.window_widgets.lbl_croissant_amount.config(text=0)
        self.window_widgets.lbl_carbonara_amount.config(text=0)
        
        self.window_widgets.lbl_receipt_customerName.config(text="Customer Name:")
        self.window_widgets.lbl_receipt_orders.config(text="")
        self.window_widgets.lbl_receipt_subtotal.config(text="Subtotal:")
        self.window_widgets.lbl_receipt_discount.config(text="Discount:")
        self.window_widgets.lbl_receipt_total.config(text="Total:")
        
        self.window_widgets.ck_btn_coffee.config(state=tk.NORMAL)
        self.window_widgets.ck_btn_croissant.config(state=tk.NORMAL)
        self.window_widgets.ck_btn_carbonara.config(state=tk.NORMAL)
        self.window_widgets.rd_btn_discount1.config(state=tk.NORMAL)
        self.window_widgets.rd_btn_discount2.config(state=tk.NORMAL)
        self.window_widgets.rd_btn_discount3.config(state=tk.NORMAL)
        self.window_widgets.rd_btn_discount4.config(state=tk.NORMAL)


        self.window_widgets.btn_enter.config(state=tk.NORMAL)
        self.window_widgets.btn_clear.config(bg="#3EFF8B")


class Window:
    def __init__(self):
        #Access win widgets to another class
        self.receipt_process = ReceiptProcess(self)   
        #Window config
        self.win = tk.Tk()
        self.win.title("Food Kiosk App")
        self.win.geometry("850x500")
        self.win.resizable(False, False)
        self.win.config(bg="#bdcfb5")
        
        #Const Var
        self.menu1, self.menu2, self.menu3 = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()
        self.radio1 = tk.IntVar()

        #miscellaneous
        self.space = ""
        
        #Call methods to create contents
        self.frames()
        self.create_widgets()
        
    def frames(self):
        #Frame
        self.frame1 = tk.Frame(self.win, width=400, height=450, bg="#eff1ed", bd=5, relief=tk.GROOVE)
        self.frame2 = tk.Frame(self.win, width=380, height=450, bg="#eff1ed", bd=5, relief=tk.GROOVE)

        #Frame pos
        self.frame1.place(x=20, y=20)
        self.frame2.place(x=450, y=20)

    def create_widgets(self):
    #Frame1 widgets
        #Label
        self.lbl_customerName = tk.Label(self.frame1, text="Customer Name:", font=("Helvetica", 14))
        self.lbl_menu = tk.Label(self.frame1, text="Menu", font=("Helvetica", 14))
        self.lbl_coffee_amount = tk.Label(self.frame1, text=0, font=("Helvetica", 14))
        self.lbl_croissant_amount = tk.Label(self.frame1, text=0, font=("Helvetica", 14))
        self.lbl_carbonara_amount = tk.Label(self.frame1, text=0, font=("Helvetica", 14))
        self.lbl_discount = tk.Label(self.frame1, text="Discount", font=("Helvetica", 14))

        #Label pos
        self.lbl_customerName.place(x=10, y=10)
        self.lbl_menu.place(x=155, y=50)
        self.lbl_coffee_amount.place(x=300, y=80)
        self.lbl_croissant_amount.place(x=300, y=110)
        self.lbl_carbonara_amount.place(x=300, y=140)
        self.lbl_discount.place(x=145, y=200)

        #Entry
        self.ent_customerName = tk.Entry(self.frame1, font=("Helvetica", 14), width=19)
        
        #Entry pos
        self.ent_customerName.place(x=160, y=10)
        
        #Checkbuttons
        self.ck_btn_coffee = tk.Checkbutton(self.frame1, text=f"Coffee{self.space:>10} ₱123.00", variable=self.menu1,
                                            font=("Helvetica", 14), command=self.receipt_process.amountToggle)
        self.ck_btn_croissant = tk.Checkbutton(self.frame1, text=f"Croissant{self.space:>6} ₱85.00", variable=self.menu2,
                                               font=("Helvetica", 14), command=self.receipt_process.amountToggle)
        self.ck_btn_carbonara = tk.Checkbutton(self.frame1, text=f"Carbonara{self.space:>4} ₱250.00", variable=self.menu3,
                                               font=("Helvetica", 14), command=self.receipt_process.amountToggle)

        #Checkbuttons pos
        self.ck_btn_coffee.place(x=30, y=80)
        self.ck_btn_croissant.place(x=30, y=110)
        self.ck_btn_carbonara.place(x=30, y=140)

        #Buttons
        self.btn_coffee_add = tk.Button(self.frame1, text="+", font=("Helvetica", 10), bg="#3EFF8B",
                                        activebackground="#E76D83", width=2, state=tk.DISABLED, command=lambda:self.receipt_process.amountAdd_Minus("coffee+"))
        self.btn_croissant_add = tk.Button(self.frame1, text="+", font=("Helvetica", 10), bg="#3EFF8B", 
                                           activebackground="#E76D83", width=2, state=tk.DISABLED, command=lambda:self.receipt_process.amountAdd_Minus("croissant+"))
        self.btn_carbonara_add = tk.Button(self.frame1, text="+", font=("Helvetica", 10), bg="#3EFF8B", 
                                           activebackground="#E76D83", width=2, state=tk.DISABLED, command=lambda:self.receipt_process.amountAdd_Minus("carbonara+"))

        self.btn_coffee_minus = tk.Button(self.frame1, text="-", font=("Helvetica", 10), bg="#3EFF8B", 
                                          activebackground="#E76D83", width=2, state=tk.DISABLED, command=lambda:self.receipt_process.amountAdd_Minus("coffee-"))
        self.btn_croissant_minus = tk.Button(self.frame1, text="-", font=("Helvetica", 10), bg="#3EFF8B", 
                                             activebackground="#E76D83", width=2, state=tk.DISABLED, command=lambda:self.receipt_process.amountAdd_Minus("croissant-"))
        self.btn_carbonara_minus = tk.Button(self.frame1, text="-", font=("Helvetica", 10), bg="#3EFF8B", 
                                             activebackground="#E76D83", width=2, state=tk.DISABLED, command=lambda:self.receipt_process.amountAdd_Minus("carbonara-"))

        self.btn_enter = tk.Button(self.frame1, text="Enter", font=("Helvetica", 14), bg="#3EFF8B", 
                                   activebackground="#E76D83", width=12, command=self.receipt_process.amountReceiptProcessing)
        self.btn_clear = tk.Button(self.frame1, text="Clear", font=("Helvetica", 14), bg="#3EFF8B", 
                                   activebackground="#E76D83", width=8, command=self.receipt_process.clear)

        #Buttons pos
        self.btn_coffee_add.place(x=330, y=80)
        self.btn_croissant_add.place(x=330, y=110)
        self.btn_carbonara_add.place(x=330, y=140)

        self.btn_coffee_minus.place(x=260, y=80)
        self.btn_croissant_minus.place(x=260, y=110)
        self.btn_carbonara_minus.place(x=260, y=140)

        self.btn_enter.place(x=120, y=320)
        self.btn_clear.place(x=140, y=380)

        #Radiobuttons
        self.rd_btn_discount1 = tk.Radiobutton(self.frame1, text="0%", font=("Helvetica", 14), variable=self.radio1, value=1)
        self.rd_btn_discount2 = tk.Radiobutton(self.frame1, text="5%", font=("Helvetica", 14), variable=self.radio1, value=2)
        self.rd_btn_discount3 = tk.Radiobutton(self.frame1, text="10%", font=("Helvetica", 14), variable=self.radio1, value=3)
        self.rd_btn_discount4 = tk.Radiobutton(self.frame1, text="15%", font=("Helvetica", 14), variable=self.radio1, value=4)

        #Radiobuttons pos
        self.rd_btn_discount1.place(x=30, y=230)
        self.rd_btn_discount2.place(x=110, y=230)
        self.rd_btn_discount3.place(x=190, y=230)
        self.rd_btn_discount4.place(x=270, y=230)

    #Frame 2 Widgets
        #Label
        self.lbl_receipt_title = tk.Label(self.frame2, text="Receipt", font=("Helvetica", 14))
        self.lbl_receipt_timeDate = tk.Label(self.frame2, text="", font=("Helvetica", 14))
        self.lbl_receipt_customerName = tk.Label(self.frame2, text="Customer Name: ", font=("Helvetica", 14))
        self.lbl_receipt_orders = tk.Label(self.frame2, text="", font=("Helvetica", 14))
        self.lbl_receipt_subtotal = tk.Label(self.frame2, text="Subtotal:", font=("Helvetica", 14))
        self.lbl_receipt_discount = tk.Label(self.frame2, text="Discount:", font=("Helvetica", 14))
        self.lbl_receipt_total = tk.Label(self.frame2, text="Total:", font=("Helvetica", 14))

        #Label pos
        self.lbl_receipt_title.place(x=150, y=5)
        self.lbl_receipt_timeDate.place(x=60, y=30)
        self.lbl_receipt_customerName.place(x=5, y=60)
        self.lbl_receipt_orders.place(x=10, y=135)
        self.lbl_receipt_subtotal.place(x=10, y=310)
        self.lbl_receipt_discount.place(x=10, y=340)
        self.lbl_receipt_total.place(x=10, y=400)

        #Line Separator
        lbl_receipt_lineSeparator = tk.Label(self.frame2, text="-" * 72 + "\n", font=("Helvetica", 11))
        lbl_receipt_lineSeparator2 = tk.Label(self.frame2, text="-" * 72 + "\n", font=("Helvetica", 11))

        lbl_receipt_lineSeparator.place(x=0, y=90)
        lbl_receipt_lineSeparator2.place(x=0, y=367)
  
window = Window()
window.win.mainloop()