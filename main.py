import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Birleştirici")
        
        self.pdf_files = []

        self.label = tk.Label(root, text="Birleştirilecek PDF dosyalarını seçin:")
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.add_button = tk.Button(root, text="PDF Ekle", command=self.add_pdf)
        self.add_button.pack(pady=5)

        self.merge_button = tk.Button(root, text="Birleştir ve İndir", command=self.merge_pdfs)
        self.merge_button.pack(pady=5)

    def add_pdf(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)
                self.listbox.insert(tk.END, file)

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showwarning("Uyarı", "Lütfen en az bir PDF dosyası ekleyin.")
            return
        
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if not output_file:
            return
        
        merger = PdfMerger()

        for pdf in self.pdf_files:
            merger.append(pdf)

        try:
            merger.write(output_file)
            merger.close()
            messagebox.showinfo("Başarılı", "PDF dosyaları başarıyla birleştirildi ve kaydedildi.")
        except Exception as e:
            messagebox.showerror("Hata", f"PDF dosyaları birleştirilemedi: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.geometry("500x400")
    root.mainloop()
