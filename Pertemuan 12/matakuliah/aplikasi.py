import tkinter as tk
from tkinter import Frame, Label, Entry, Button, StringVar, messagebox, ttk, VERTICAL, YES, BOTH, END
from matakuliah import Matakuliah

class FormMatakuliah:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='ID:').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtID = Entry(mainFrame) 
        self.txtID.grid(row=0, column=1, padx=5, pady=5) 
        self.txtID.bind("<Return>", self.onCari)  # Menambahkan event Enter key

        Label(mainFrame, text='Kode MK:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtKodeMK = Entry(mainFrame) 
        self.txtKodeMK.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Nama MK:').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNamaMK = Entry(mainFrame) 
        self.txtNamaMK.grid(row=2, column=1, padx=5, pady=5) 

        Label(mainFrame, text='SKS:').grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtSKS = StringVar()
        Cbo = ttk.Combobox(mainFrame, width=27, textvariable=self.txtSKS) 
        Cbo.grid(row=3, column=1, padx=5, pady=5)
        Cbo['values'] = ('1', '2', '3', '4', '6')
        Cbo.current()      
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # Define columns
        columns = ('id', 'kodemk', 'namamk', 'sks')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # Define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('kodemk', text='Kode MK')
        self.tree.column('kodemk', width="60")
        self.tree.heading('namamk', text='Nama MK')
        self.tree.column('namamk', width="200")
        self.tree.heading('sks', text='SKS')
        self.tree.column('sks', width="30")
        # Set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtID.delete(0, END)
        self.txtID.insert(END, "")
        self.txtKodeMK.delete(0, END)
        self.txtKodeMK.insert(END, "")
        self.txtNamaMK.delete(0, END)
        self.txtNamaMK.insert(END, "")       
        self.txtSKS.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # Get data matakuliah
        mk = Matakuliah()
        result = mk.getAllData()

        # Hapus semua item dalam Treeview
        self.tree.delete(*self.tree.get_children())

        # Masukkan data baru ke dalam Treeview
        for row_data in result:
            self.tree.insert('', END, values=row_data)

    def onCari(self, event=None):
        id_matakuliah = self.txtID.get()
        mk = Matakuliah()
        res = mk.getById(id_matakuliah)
        rec = mk.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtKodeMK.focus()
        return res
        
    def TampilkanData(self, event=None):
        id_matakuliah = self.txtID.get()
        mk = Matakuliah()
        res = mk.getById(id_matakuliah)
        self.txtKodeMK.delete(0, END)
        self.txtKodeMK.insert(END, mk.kodemk)
        self.txtNamaMK.delete(0, END)
        self.txtNamaMK.insert(END, mk.namamk)
        self.txtSKS.set(mk.sks)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        id_matakuliah = self.txtID.get()
        kodemk = self.txtKodeMK.get()
        namamk = self.txtNamaMK.get()
        sks = self.txtSKS.get()
        
        mk = Matakuliah()
        mk.id = id_matakuliah
        mk.kodemk = kodemk
        mk.namamk = namamk
        mk.sks = sks
        if self.ditemukan:
            res = mk.update()  # Tidak perlu mengirim id karena sudah di-set sebelumnya
            ket = 'Diperbarui'
        else:
            res = mk.simpan()
            ket = 'Disimpan'
            
        rec = mk.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil " + ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal " + ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        id_matakuliah = self.txtID.get()
        mk = Matakuliah()
        mk.id = id_matakuliah
        if self.ditemukan:
            res = mk.delete()  # Tidak perlu mengirim id karena sudah di-set sebelumnya
            rec = mk.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # Memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormMatakuliah(root, "Aplikasi Data Matakuliah")
    root.mainloop()
