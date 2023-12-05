import os
import pdfrw
import tkinter as tk
from tkinter import ttk, filedialog

def combine_pdfs(directory_path, output_path, output_filename):
    pdf_files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]
    pdf_files.sort()

    pdf_writer = pdfrw.PdfFileWriter()
    file_streams = []

    try:
        for pdf_file in pdf_files:
            pdf_path = os.path.join(directory_path, pdf_file)
            file_stream = open(pdf_path, 'rb')
            file_streams.append(file_stream)
            
            pdf_reader = pdfrw.PdfFileReader(file_stream)
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page)

        full_output_path = os.path.join(output_path, output_filename)
        with open(full_output_path, 'wb') as out:
            pdf_writer.write(out)
    finally:
        for file_stream in file_streams:
            file_stream.close()

    return f"Combined {len(pdf_files)} PDFs into {full_output_path}"

def combine_button_clicked():
    input_dir = input_directory_entry.get()
    output_dir = output_directory_entry.get()
    output_filename = output_filename_entry.get() or "combined.pdf"
    
    if not input_dir or not output_dir:
        status_label["text"] = "Both directories must be provided."
        return

    try:
        message = combine_pdfs(input_dir, output_dir, output_filename)
        status_label["text"] = message
    except Exception as e:
        status_label["text"] = f"Error: {str(e)}"

def browse_input_directory():
    folder_selected = filedialog.askdirectory()
    input_directory_entry.delete(0, tk.END)
    input_directory_entry.insert(0, folder_selected)

def browse_output_directory():
    folder_selected = filedialog.askdirectory()
    output_directory_entry.delete(0, tk.END)
    output_directory_entry.insert(0, folder_selected)

# Create the main window
root = tk.Tk()
root.title("PDF Combiner")

# Create widgets
input_directory_label = ttk.Label(root, text="Input Folder:")
input_directory_entry = ttk.Entry(root, width=50)
input_directory_browse = ttk.Button(root, text="Browse", command=browse_input_directory)

output_directory_label = ttk.Label(root, text="Output Folder:")
output_directory_entry = ttk.Entry(root, width=50)
output_directory_browse = ttk.Button(root, text="Browse", command=browse_output_directory)

output_filename_label = ttk.Label(root, text="Output Filename:")
output_filename_entry = ttk.Entry(root, width=50)
output_filename_entry.insert(0, "combined.pdf")

combine_button = ttk.Button(root, text="Combine PDFs", command=combine_button_clicked)
status_label = ttk.Label(root, text="Status: Waiting for input...")

# Place widgets
input_directory_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
input_directory_entry.grid(row=0, column=1, padx=10, pady=5)
input_directory_browse.grid(row=0, column=2, padx=10, pady=5)

output_directory_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
output_directory_entry.grid(row=1, column=1, padx=10, pady=5)
output_directory_browse.grid(row=1, column=2, padx=10, pady=5)

output_filename_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
output_filename_entry.grid(row=2, column=1, padx=10, pady=5)

combine_button.grid(row=3, column=0, columnspan=3, pady=10)
status_label.grid(row=4, column=0, columnspan=3, pady=5)

root.mainloop()
