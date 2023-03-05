#Import
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import BazaUpis
from fpdf import FPDF
import datetime
import matplotlib.pyplot as plt
import numpy as np


#START GUI

#Glavni meni
def main_screen():
    global screen1
    screen1 = Tk()
    screen1.title("InvoiceApp")
    screen1.iconbitmap("C:\\Users\petar\Desktop\Seminarski rad A - projekat\Photo\Icon.ico")
    screen1.configure(bg="gray")
    Label(screen1, text="", bg="gray",).pack()
    Label(screen1, text="Dobro dosli!", font=("Arial", 20), bg="gray", fg="black").pack()
    Label(screen1, text="", bg="gray").pack()
    Label(screen1, text="", bg="gray").pack()
    frame = LabelFrame(screen1, text="Log in", padx=15, pady=10, bg="gray")
    frame.pack()
    Label(frame, text="", bg="gray").pack()
    global userName
    Label(frame, text="Korisnicko ime:", font=("Arial", 14), bg="gray").pack()
    userName = Entry(frame, width=30)
    userName.pack()
    global password
    Label(frame, text="Lozinka:", font=("Arial", 14), bg="gray").pack()
    password = Entry(frame, width=30)
    password.pack()
    Label(frame, text="", bg="gray").pack()
    Button(frame, text="Ulogujte se", font=("Arial", 14), width=15, height=2, command=log_in).pack()
    
    screen_width = screen1.winfo_screenwidth()
    screen_height = screen1.winfo_screenheight()

    width = 300
    height = 400
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    screen1.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    screen1.mainloop()
    

#Log in
def log_in():
    global user_data
    b = 0
    if (userName.get() == "admin" and password.get() == "admin"):
        screen1.destroy()
        admin_screen()
        b = 1
    else:
        user_data = BazaUpis.log_in_baza(userName.get(), password.get())
        b = 1
        screen1.destroy()
        user_screen()
    if b == 0:
        messagebox.showerror(title="Prijavljivanje", message="Neuspesna prijava")
        

#ADMIN GUI

#Admin stranica
def admin_screen():
    global screen2
    screen2 = Tk()
    screen2.title("InvoiceApp")
    screen2.iconbitmap("C:\\Users\petar\Desktop\Seminarski rad A - projekat\Photo\Icon.ico")
    screen2.configure(bg="gray")
    Label(screen2, text="", bg="gray").pack()
    Label(screen2, text="", bg="gray").pack()
    frame = LabelFrame(screen2, text="Admin", padx=15, pady=10, bg="gray")
    frame.pack()
    Button(frame, text="Registracija", width=15, height=3, command=reg_screen).pack()
    Label(frame, text="", bg="gray").pack()
    Button(frame, text="Promena", width=15, height=3, command = edit_screen).pack()
    Label(frame, text="", bg="gray").pack()
    Button(frame, text="Prikaz grafika", width=15, height=3, command= view_graph).pack()
    Label(frame, text="", bg="gray").pack()
    Button(frame, text="Izlogujte se", width=15, height=3, command= log_out_admin).pack()
    
    
    screen_width = screen2.winfo_screenwidth()
    screen_height = screen2.winfo_screenheight()

    width = 200
    height = 400
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    screen2.geometry('%dx%d+%d+%d' % (width, height, x, y))
    screen2.mainloop()

def log_out_admin():
    screen2.destroy()
    main_screen()
    


#Register stranica
def reg_screen():
    screen2.destroy()
    global screen3
    screen3 = Tk()
    screen3.title("InvoiceApp")
    screen3.iconbitmap("C:\\Users\petar\Desktop\Seminarski rad A - projekat\Photo\Icon.ico")
    screen3.configure(bg="gray")
    Label(screen3, text="", bg="gray").pack()
    frame = LabelFrame(screen3, text="Registracija", font=("Arial", 14), padx=15, pady=10, bg="gray", width=750, height=550)
    frame.pack()
    Label(frame, text="PIB:", font=("Arial", 14), bg="gray").pack()
    global oznaka, user_name, pass_word, imeFirme, adresa, grad, email, racun
    oznaka = Entry(frame, width=30)
    oznaka.pack()
    Label(frame, text="Korisnicko ime:", font=("Arial", 14), bg="gray").pack()
    user_name = Entry(frame, width=30)
    user_name.pack()
    Label(frame, text="Lozinka:", font=("Arial", 14), bg="gray").pack()
    pass_word = Entry(frame, width=30)
    pass_word.pack()
    Label(frame, text="Ime firme:", font=("Arial", 14), bg="gray").pack()
    imeFirme = Entry(frame, width=30)
    imeFirme.pack()
    Label(frame, text="Adresa:", font=("Arial", 14), bg="gray").pack()
    adresa = Entry(frame, width=30)
    adresa.pack()
    Label(frame, text="Grad:", font=("Arial", 14), bg="gray").pack()
    grad = Entry(frame, width=30)
    grad.pack()
    Label(frame, text="E-mail:", font=("Arial", 14), bg="gray").pack()
    email = Entry(frame, width=30)
    email.pack()
    Label(frame, text="Tekuci racun:", font=("Arial", 14), bg="gray").pack()
    racun = Entry(frame, width=30)
    racun.pack()
    Label(frame, text="", bg="gray").pack()
    Button(frame, text="Registruj", width=15, height=3, command=upis_korisnika).pack()
    Button(frame, text="Nazad", width=15, height=3, command = back_reg).pack()
    
    screen_width = screen3.winfo_screenwidth()
    screen_height = screen3.winfo_screenheight()

    width = 250
    height = 600
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    screen3.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    screen3.mainloop()
    
def back_reg():
    screen3.destroy()
    admin_screen()
    
    
#Upisivanje u fajl posle registracije:
    
def upis_korisnika():
    t = oznaka.get()!="" and user_name.get()!="" and pass_word.get()!="" and imeFirme.get()!="" and adresa.get()!="" and grad.get()!="" and email.get()!="" and racun.get()!="" 
    if t:
        BazaUpis.reg_kor_baza(int(oznaka.get()), user_name.get(), pass_word.get(), imeFirme.get(), adresa.get(), grad.get(), email.get(), int(racun.get()))
        BazaUpis.reg_bal(int(oznaka.get()))    

    
#Edit stranica
def edit_screen():
    global screen4
    screen4 = Tk()
    screen4.title("InvoiceApp")
    screen4.iconbitmap("C:\\Users\petar\Desktop\Seminarski rad A - projekat\Photo\Icon.ico")
    screen4.configure(bg="gray")
    frame = LabelFrame(screen4, text="Edit", padx=15, pady=10, bg="gray")
    frame.pack()
    global oznaka1, user_name1, pass_word1, imeFirme1, adresa1, grad1, email1, racun1
    Label(frame, text="PIB:", font=("Arial", 14), bg="gray").pack()
    oznaka1 = Entry(frame, width=30)
    oznaka1.pack()
    Label(frame, text="Korisnicko ime:", font=("Arial", 14), bg="gray").pack()
    user_name1 = Entry(frame, width=30)
    user_name1.pack()
    Label(frame, text="Lozinka:", font=("Arial", 14), bg="gray").pack()
    pass_word1 = Entry(frame, width=30)
    pass_word1.pack()
    Label(frame, text="Ime firme:", font=("Arial", 14), bg="gray").pack()
    imeFirme1 = Entry(frame, width=30)
    imeFirme1.pack()
    Label(frame, text="Adresa:", font=("Arial", 14), bg="gray").pack()
    adresa1 = Entry(frame, width=30)
    adresa1.pack()
    Label(frame, text="Grad:", font=("Arial", 14), bg="gray").pack()
    grad1 = Entry(frame, width=30)
    grad1.pack()
    Label(frame, text="E-mail:", font=("Arial", 14), bg="gray").pack()
    email1 = Entry(frame, width=30)
    email1.pack()
    Label(frame, text="Tekuci racun:", font=("Arial", 14), bg="gray").pack()
    racun1 = Entry(frame, width=30)
    racun1.pack()
    Label(frame, text="", bg="gray").pack()
    Button(frame, text="Promeni", width=15, height=3, command=edit_user).pack()
    Button(frame, text="Obrisi", width=15, height=3, command=delete_user).pack()
    Button(frame, text="Nazad", width=15, height=3, command=back_edit).pack()
    global del_label 
    del_label = Label(frame, text="", bg="gray")
    del_label.pack()
    
    screen_width = screen4.winfo_screenwidth()
    screen_height = screen4.winfo_screenheight()

    width = 250
    height = 630
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    screen4.geometry('%dx%d+%d+%d' % (width, height, x, y))
    screen2.destroy()
    
    screen4.mainloop()

def back_edit():
    screen4.destroy()
    admin_screen()
    
    
#Brisanje korisnika:
def delete_user():
    t = oznaka1.get()!=""
    if t:
        BazaUpis.del_kor_baza(int(oznaka1.get()))
        
#Brisanje korisnika:
def edit_user():
    t = oznaka1.get()!="" and user_name1.get()!="" and pass_word1.get()!="" and imeFirme1.get()!="" and adresa1.get()!="" and grad1.get()!="" and email1.get()!="" and racun1.get()!="" 
    if t:
        BazaUpis.upd_kor_baza(int(oznaka1.get()), user_name1.get(), pass_word1.get(), imeFirme1.get(), adresa1.get(), grad1.get(), email1.get(), int(racun1.get()))
    
#View stranica
def view_graph():
    labels = []
    user_out = []
    user_in = []
    userd = BazaUpis.sel_all_kor()
    for i in userd:
        baldata = BazaUpis.bal(i[0])
        usern = i[3]
        labels.append(usern)
        user_out.append(baldata[1])
        user_in.append(baldata[2])
    x = np.arange(len(labels))  
    width = 0.35  

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, user_out, width, label='Prodato')
    rects2 = ax.bar(x + width/2, user_in, width, label='Kupljeno')
    ax.set_title('Admin grafikon')
    ax.set_ylabel('Novac(din)')
    ax.set_xlabel('Naziv firme')
    ax.set_title('Grafik po protoku novca')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()
    


#USER GUI

#Main user page

def user_screen():
    global screen6
    screen6 = Tk()
    screen6.title("InvoiceApp")
    screen6.iconbitmap("C:\\Users\petar\Desktop\Seminarski rad A - projekat\Photo\Icon.ico")
    screen6.configure(bg="gray")
    Label(screen6, text="", bg="gray").pack()
    frame = LabelFrame(screen6, text="Podaci o korisniku", padx=30, pady=10, bg="gray")
    frame.pack() 
    podaci ="PIB: " + str(user_data[0]) + "\n" + "Ime firme: " + user_data[3] + "\n" + "Adresa: " + user_data[4] + "\n" + "Grad: " + user_data[5] + "\n" + "E-mail: " + user_data[6] + "\n" + "Ziro racun: " + str(user_data[7]) + "\n" 
    Label(frame, text=podaci, bg="gray", bd = 1, fg="black", justify="left", anchor="w").pack()
    Label(screen6, text="", bg="gray").pack()
    frame2 = LabelFrame(screen6, text="Opcije", padx=45, pady=10, bg="gray")
    frame2.pack() 
    Button(frame2, text="Unos proizvoda", width=15, height=3, command=unos_screen).pack()
    Button(frame2, text="Prodaja", width=15, height=3, command=fak_screen).pack()
    Button(frame2, text="Kupovina", width=15, height=3, command=unfak_screen).pack()
    Button(frame2, text="Status", width=15, height=3, command=graph_user).pack()
    Button(frame2, text="Izlogujte se", width=15, height=3, command= log_out_user).pack()
    
    
    screen_width = screen6.winfo_screenwidth()
    screen_height = screen6.winfo_screenheight()

    width = 270
    height = 550
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    screen6.geometry('%dx%d+%d+%d' % (width, height, x, y))
    screen6.mainloop()

def log_out_user():
    screen6.destroy()
    main_screen()
    

#Unos proizvoda/inventar

def unos_screen():
    global screen7
    screen7 = Tk()
    screen7.title("InvoiceApp")
    screen7.iconbitmap("C:\\Users\petar\Desktop\Seminarski rad A - projekat\Photo\Icon.ico")
    screen7.configure(bg="gray")
    Label(screen7, text="", bg="gray").pack()
    frame = LabelFrame(screen7, text="Unos proizvoda", padx=30, pady=10, bg="gray")
    frame.pack()
    global sifra, naziv, cena, kolicina, mera
    Label(frame, text="Id:", bg="gray").pack()
    sifra = Entry(frame, width=30)
    sifra.pack()
    Label(frame, text="Naziv:", bg="gray").pack()
    naziv = Entry(frame, width=30)
    naziv.pack()
    Label(frame, text="Cena:", bg="gray").pack()
    cena = Entry(frame, width=30)
    cena.pack()
    Label(frame, text="Kolicina:", bg="gray").pack()
    kolicina = Entry(frame, width=30)
    kolicina.pack()
    Label(frame, text="Jedinica mere:", bg="gray").pack()
    mera = Entry(frame, width=30)
    mera.pack()
    Label(frame, text="", bg="gray").pack()
    Button(frame, text="Enter product", width=15, height=3, command=unos).pack()
    Button(frame, text="Edit product", width=15, height=3, command=edit_proizv).pack()
    Button(frame, text="Delete product", width=15, height=3, command=del_proiz).pack()
    Button(frame, text="Back", width=15, height=3, command=back_unos).pack()
    global unos_label 
    unos_label = Label(frame, text="", bg="gray")
    unos_label.pack()
    
    screen_width = screen7.winfo_screenwidth()
    screen_height = screen7.winfo_screenheight()

    # calculate position x and y coordinates
    width = 280
    height = 550
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    screen7.geometry('%dx%d+%d+%d' % (width, height, x, y))
    screen6.destroy()
    screen7.mainloop()
    
def unos():
    t = sifra.get()!="" and naziv.get()!="" and cena.get()!="" and kolicina.get()!="" and mera.get()!=""
    if t:
        BazaUpis.reg_proiz_baza(int(user_data[0]), int(sifra.get()), naziv.get(), float(cena.get()), int(kolicina.get()), mera.get())    

def edit_proizv():
    t = sifra.get()!="" and naziv.get()!="" and cena.get()!="" and kolicina.get()!="" and mera.get()!=""
    if t:
        BazaUpis.edit_proiz_baza(int(sifra.get()), naziv.get(), float(cena.get()), int(kolicina.get()), mera.get())

def del_proiz():
    t = sifra.get()!=""
    if t:
        BazaUpis.del_proiz_baza(int(sifra.get()))

def back_unos():
    screen7.destroy()
    user_screen()

    

#Prodaja/pravljenje fakture
def fak_screen():
    screen6.destroy()
    global screen8
    screen8 = Tk()
    screen8.title("InvoiceApp")
    screen8.iconbitmap("C:\\Users\petar\Desktop\Seminarski rad A - projekat\Photo\Icon.ico")
    screen8.configure(bg="gray")
    table_frame = Frame(screen8)
    table_frame.pack(padx=15, pady=15)
    
    table_scroll = Scrollbar(table_frame)
    table_scroll.pack(side=RIGHT, fill=Y)
    
    table_scroll = Scrollbar(table_frame,orient='horizontal')
    table_scroll.pack(side= BOTTOM,fill=X)
    
    tabela = ttk.Treeview(table_frame,yscrollcommand=table_scroll.set, xscrollcommand =table_scroll.set)
    
    
    tabela.pack()
    
    table_scroll.config(command=tabela.yview)
    table_scroll.config(command=tabela.xview)
    
     
    tabela['columns'] = ('proizvod_id', 'proizvod_naziv', 'proizvod_cena', 'proizvod_kolicina', 'proizvod_mera')
    
    tabela.column("#0", width=0,  stretch=NO)
    tabela.column("proizvod_id",anchor=CENTER, width=80)
    tabela.column("proizvod_naziv",anchor=CENTER,width=80)
    tabela.column("proizvod_cena",anchor=CENTER,width=80)
    tabela.column("proizvod_kolicina",anchor=CENTER,width=80)
    tabela.column("proizvod_mera",anchor=CENTER,width=80)
    
    tabela.heading("#0",text="",anchor=CENTER)
    tabela.heading("proizvod_id",text="Id",anchor=CENTER)
    tabela.heading("proizvod_naziv",text="Naziv",anchor=CENTER)
    tabela.heading("proizvod_cena",text="Cena",anchor=CENTER)
    tabela.heading("proizvod_kolicina",text="Kolicina",anchor=CENTER)
    tabela.heading("proizvod_mera",text="Jed. mere",anchor=CENTER)
    
    count = 0
    tabelar = BazaUpis.tabela_baza(user_data[0])
    for i in tabelar:
        tabela.insert(parent='',index='end',iid=count,text='',
        values=(i[1],i[2],i[3],i[4], i[5]))
        count = count + 1
    
    tabela.pack()
    
    frame_faktura = LabelFrame(screen8, text="Prodaja - pravljenje fakture", bg="gray", padx=15, pady=15)
    frame_faktura.pack(padx=15, pady=20)
    Label(frame_faktura, text="Id proizvoda:", bg="gray").pack()
    global proiz_id, proiz_kol
    proiz_id = Entry(frame_faktura, width=30)
    proiz_id.pack()
    Label(frame_faktura, text="Kolicina", bg="gray").pack()
    proiz_kol = Entry(frame_faktura, width=30)
    proiz_kol.pack()
    global lista_id 
    lista_id = []
    global lista_kol 
    lista_kol = []
    Label(frame_faktura, text="", bg="gray").pack()
    Button(frame_faktura, text="Dodaj u fakturu", width=15, height=3, command=lista_proiz).pack()
    Label(frame_faktura, text="", bg="gray").pack()
    Label(frame_faktura, text="Da li zelite pdf fakturu?", bg="gray").pack()
    global r 
    r = IntVar()
    r.set("1")
    Radiobutton(frame_faktura, text="Da.", bg = "gray", variable=r, value = 1, command=radiobut1).pack()
    Radiobutton(frame_faktura, text="Ne.", bg = "gray",variable=r, value = 2, command=radiobut2).pack()
    Button(frame_faktura, text="Potvrdi", width=15, height=3, command=faktura_pdf).pack()
    Button(frame_faktura, text="Nazad", width=15, height=3, command=back_fak).pack()
    
    screen_width = screen8.winfo_screenwidth()
    screen_height = screen8.winfo_screenheight()

    width = 700
    height = 750
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    screen8.geometry('%dx%d+%d+%d' % (width, height, x, y))
    screen8.mainloop()

def back_fak():
    screen8.destroy()
    user_screen()
    lista_id.clear()
    lista_kol.clear()

def radiobut1():
    r.set("1")

def radiobut2():
    r.set("2")
    
def lista_proiz():
    kol1 = BazaUpis.prod_amount_baza(int(proiz_id.get()))
    if(kol1[0]>=int(proiz_kol.get()) and int(proiz_kol.get())>0):
        lista_id.append(int(proiz_id.get()))
        lista_kol.append(int(proiz_kol.get()))
        edit_proiz()
    else:
        messagebox.showerror(title="Fakturisanje", message="Neuspesno fakturisanje!")
def edit_proiz():
    kol1 = BazaUpis.prod_amount_baza(int(proiz_id.get()))
    kol2 = int(kol1[0]) - int(proiz_kol.get())
    BazaUpis.upd_proiz_baza(int(proiz_id.get()), kol2)
    messagebox.showinfo(title="Fakturisanje", message="Uspesno fakturisanje!")

class PDF(FPDF):
    def header(self):
        self.image("logo.png", 160, 3, 50)
        self.set_font('helvetica', 'B', 25)
        self.cell(0, 10, 'Faktura', border=False, align='C', ln=1)
        self.set_font('helvetica', 'I', 12)
        info = "PIB: " + str(user_data[0]) + "\nCompany: " + user_data[3] + "\nAddress: " + user_data[4] + "\nCity: " + user_data[5] + "\nE-mail: " + user_data[6] + "\nBank account: " + str(user_data[7]) + "\n"
        self.multi_cell(0, 5, info, border = False, align='L', ln=2)
        self.ln(25)
    def create_table(self, table_data, title='', data_size = 10, title_size=12, align_data='L', align_header='L', cell_width='even', x_start='x_default',emphasize_data=[], emphasize_style=None,emphasize_color=(0,0,0)): 
        default_style = self.font_style
        if emphasize_style == None:
            emphasize_style = default_style
        # default_font = self.font_family
        # default_size = self.font_size_pt
        # default_style = self.font_style
        # default_color = self.color # This does not work

        # Get Width of Columns
        def get_col_widths():
            col_width = cell_width
            if col_width == 'even':
                col_width = self.epw / len(data[0]) - 1  # distribute content evenly   # epw = effective page width (width of page not including margins)
            elif col_width == 'uneven':
                col_widths = []

                # searching through columns for largest sized cell (not rows but cols)
                for col in range(len(table_data[0])): # for every row
                    longest = 0 
                    for row in range(len(table_data)):
                        cell_value = str(table_data[row][col])
                        value_length = self.get_string_width(cell_value)
                        if value_length > longest:
                            longest = value_length
                    col_widths.append(longest + 4) # add 4 for padding
                col_width = col_widths



                        ### compare columns 

            elif isinstance(cell_width, list):
                col_width = cell_width  # TODO: convert all items in list to int        
            else:
                # TODO: Add try catch
                col_width = int(col_width)
            return col_width

        # Convert dict to lol
        # Why? because i built it with lol first and added dict func after
        # Is there performance differences?
        if isinstance(table_data, dict):
            header = [key for key in table_data]
            data = []
            for key in table_data:
                value = table_data[key]
                data.append(value)
            # need to zip so data is in correct format (first, second, third --> not first, first, first)
            data = [list(a) for a in zip(*data)]

        else:
            header = table_data[0]
            data = table_data[1:]

        line_height = self.font_size * 2.5

        col_width = get_col_widths()
        self.set_font(size=title_size)

        # Get starting position of x
        # Determin width of table to get x starting point for centred table
        if x_start == 'C':
            table_width = 0
            if isinstance(col_width, list):
                for width in col_width:
                    table_width += width
            else: # need to multiply cell width by number of cells to get table width 
                table_width = col_width * len(table_data[0])
            # Get x start by subtracting table width from pdf width and divide by 2 (margins)
            margin_width = self.w - table_width
            # TODO: Check if table_width is larger than pdf width

            center_table = margin_width / 2 # only want width of left margin not both
            x_start = center_table
            self.set_x(x_start)
        elif isinstance(x_start, int):
            self.set_x(x_start)
        elif x_start == 'x_default':
            x_start = self.set_x(self.l_margin)


        # TABLE CREATION #

        # add title
        if title != '':
            self.multi_cell(0, line_height, title, border=0, align='j', ln=3, max_line_height=self.font_size)
            self.ln(line_height) # move cursor back to the left margin

        self.set_font(size=data_size)
        # add header
        y1 = self.get_y()
        if x_start:
            x_left = x_start
        else:
            x_left = self.get_x()
        x_right = self.epw + x_left
        if  not isinstance(col_width, list):
            if x_start:
                self.set_x(x_start)
            for datum in header:
                self.multi_cell(col_width, line_height, datum, border=0, align=align_header, ln=3, max_line_height=self.font_size)
                x_right = self.get_x()
            self.ln(line_height) # move cursor back to the left margin
            y2 = self.get_y()
            self.line(x_left,y1,x_right,y1)
            self.line(x_left,y2,x_right,y2)

            for row in data:
                if x_start: # not sure if I need this
                    self.set_x(x_start)
                for datum in row:
                    if datum in emphasize_data:
                        self.set_text_color(*emphasize_color)
                        self.set_font(style=emphasize_style)
                        self.multi_cell(col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=self.font_size)
                        self.set_text_color(0,0,0)
                        self.set_font(style=default_style)
                    else:
                        self.multi_cell(col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=self.font_size) # ln = 3 - move cursor to right with same vertical offset # this uses an object named self
                self.ln(line_height) # move cursor back to the left margin
        
        else:
            if x_start:
                self.set_x(x_start)
            for i in range(len(header)):
                datum = header[i]
                self.multi_cell(col_width[i], line_height, datum, border=0, align=align_header, ln=3, max_line_height=self.font_size)
                x_right = self.get_x()
            self.ln(line_height) # move cursor back to the left margin
            y2 = self.get_y()
            self.line(x_left,y1,x_right,y1)
            self.line(x_left,y2,x_right,y2)


            for i in range(len(data)):
                if x_start:
                    self.set_x(x_start)
                row = data[i]
                for i in range(len(row)):
                    datum = row[i]
                    if not isinstance(datum, str):
                        datum = str(datum)
                    adjusted_col_width = col_width[i]
                    if datum in emphasize_data:
                        self.set_text_color(*emphasize_color)
                        self.set_font(style=emphasize_style)
                        self.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=self.font_size)
                        self.set_text_color(0,0,0)
                        self.set_font(style=default_style)
                    else:
                        self.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=self.font_size) # ln = 3 - move cursor to right with same vertical offset # this uses an object named self
                self.ln(line_height) # move cursor back to the left margin
        y3 = self.get_y()
        self.line(x_left,y3,x_right,y3)

def faktura_pdf():
    if r.get() == 1:
        pdf = PDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_auto_page_break(True, margin=15)
        pdf.set_font('Times', '', 10)
        x = datetime.datetime.now()
        naziv_pdf = str(x.year) + str(x.month) + str(x.day) + str(x.hour) + str(x.minute) + str(x.second)
        data = []
        data2 = ['ID', 'Proizvod', 'Cena', 'Kolicina', 'Mera', 'Ukupno']
        data.append(data2)
        j = 0
        uk = 0.0
        for i in lista_id:
            p = BazaUpis.pdf_baza(i)
            ukupno = round(float(p[3]) * lista_kol[j], 2)
            uk = uk + float(ukupno)
            data1 = [str(p[1]), str(p[2]), str(p[3]), str(lista_kol[j]), str(p[5]), str(ukupno)]
            BazaUpis.ins_inv_baza(naziv_pdf, i, p[2], p[3], lista_kol[j], p[5], user_data[0])
            j = j + 1
            data.append(data1)
        
        balpod = BazaUpis.bal(user_data[0])
        ukbal = float(balpod[1]) + uk
        BazaUpis.upd_out_bal(user_data[0], ukbal)

        data2 = ['','','','','',str(uk)]
        data.append(data2)
        pdf.create_table(table_data = data, cell_width = 'even')
        pdf.ln(5)
        fk = "Faktura broj: " + naziv_pdf
        pdf.cell(15, 5, fk)
        pdf.ln(25)
        pdf.cell(0, 0, "M.P.", align='C')
        visina = 106 + 5 * j
        pdf.image("stamp.png", 80, visina, 50)
        naziv_pdf = naziv_pdf + ".pdf"
        pdf.output(name = naziv_pdf)
        lista_id.clear()
        lista_kol.clear()
    elif r.get()==2:
        x = datetime.datetime.now()
        naziv_pdf = str(x.year) + str(x.month) + str(x.day) + str(x.hour) + str(x.minute) + str(x.second)
        j = 0
        for i in lista_id:
            p = BazaUpis.pdf_baza(i)
            ukupno = round(float(p[3]) * lista_kol[j], 2)
            uk = uk + float(ukupno)
            BazaUpis.ins_inv_baza(naziv_pdf, i, p[2], p[3], lista_kol[j], p[5])
            j = j + 1
        balpod = BazaUpis.bal(user_data[0])
        ukbal = float(balpod[1]) + uk
        BazaUpis.upd_out_bal(user_data[0], ukbal)
        lista_id.clear()
        lista_kol.clear()


#Kupovina/unos fakture

def unfak_screen():
    screen6.destroy()
    global screen9
    screen9 = Tk()
    screen9.title("InvoiceApp")
    screen9.iconbitmap("C:\\Users\petar\Desktop\Seminarski rad A - projekat\Photo\Icon.ico")
    screen9.configure(bg="gray")
    Label(screen9, text="", bg="gray").pack()
    frame = LabelFrame(screen9, text="Kupovina/unos fakture", padx=15, pady=10, bg="gray")
    frame.pack()
    Label(frame, text="Broj fakture:", font=("Arial", 14), bg="gray").pack()
    global Brfak
    Brfak = Entry(frame, width=30)
    Brfak.pack()
    Label(frame, text="", bg="gray").pack()
    Button(frame, text="Unesi fakturu", width=15, height=3, command=unos_fakture).pack()
    Button(frame, text="Nazad", width=15, height=3, command=back_unfak).pack()

    screen_width = screen9.winfo_screenwidth()
    screen_height = screen9.winfo_screenheight()

    width = 250
    height = 400
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    screen9.geometry('%dx%d+%d+%d' % (width, height, x, y))
    screen9.mainloop()

def unos_fakture():
    try:
        fakdata = BazaUpis.sel_inv_baza(int(Brfak.get()))
        used = False
        baldata = BazaUpis.bal(user_data[0])
        suma = 0.0
        for i in fakdata:
            suma = suma + float(i[3] * i[4])
            if i[7]==1:
                used=True
        suma = suma + float(baldata[2])
        if used==False:
            BazaUpis.upd_in_bal(user_data[0], suma)
            for i in fakdata:
                BazaUpis.used(i[0])
        else:
            messagebox.showerror("Neuspesno", "Faktura je uneta.")
    except Exception as e:
        print(e)

def back_unfak():
    screen9.destroy()
    user_screen()
        

#Status/grafik unos/izvoz

def graph_user():
    baldata = BazaUpis.bal(user_data[0])
    usern = BazaUpis.name_baza(user_data[0])
    labels = []
    labels.append(usern[0])
    user_out = []
    user_in = []
    user_out.append(baldata[1])
    user_in.append(baldata[2])

    x = np.arange(len(labels))  
    width = 0.35  

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, user_out, width, label='Prodato')
    rects2 = ax.bar(x + width/2, user_in, width, label='Kupljeno')

    ax.set_title('Korisnik grafikon')
    ax.set_ylabel('Novac(din)')
    ax.set_title('Grafik po protoku novca')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()
    


#Main
main_screen()