import json
import yaml
import os
import xmltodict
import tkinter as tk
from tkinter import filedialog, messagebox

def file_existing(file_1):
    if os.path.exists(file_1):
        return True
    else:
        messagebox.showerror("Error", "Invalid file name, try again!")
        return False

def json_to_xml(file_1, file_2):
    with open(file_1, "r") as file:
        data = json.load(file)
    
    if not isinstance(data, dict) or len(data) != 1:
        data = {"root": data}

    xml_data = xmltodict.unparse(data, pretty=True)
    with open(file_2, 'w', encoding='utf-8') as file:
        file.write(xml_data)

def json_to_yaml(file_1, file_2):
    with open(file_1, "r") as file:
        data = json.load(file)
    file_yaml = yaml.dump(data, sort_keys=False)
    with open(file_2, "w") as file:
        file.write(file_yaml)

def yaml_to_json(file_1, file_2):
    with open(file_1, "r") as file:
        data = yaml.safe_load(file)

    with open(file_2, "w") as file:
        json.dump(data, file)

def xml_to_json(file_1, file_2):
    with open(file_1, 'r', encoding='utf-8') as file:
        xml_content = file.read()
    data_dict = xmltodict.parse(xml_content)
    with open(file_2, "w") as file:
        json.dump(data_dict, file)

def xml_to_yaml(file_1, file_2):
    with open(file_1, 'r', encoding='utf-8') as file:
        xml_content = file.read()
    data_dict = xmltodict.parse(xml_content)
    file_yaml = yaml.dump(data_dict, sort_keys=False)
    with open(file_2, "w") as file:
        file.write(file_yaml)

def yaml_to_xml(file_1, file_2):
    with open(file_1, "r") as file:
        data = yaml.safe_load(file)
    
    if not isinstance(data, dict) or len(data) != 1:
        data = {"root": data}

    xml_data = xmltodict.unparse(data, pretty=True)
    with open(file_2, 'w', encoding='utf-8') as file:
        file.write(xml_data)

def convert():
    file_1 = file_input.get()
    file_2 = file_output.get()

    if not file_existing(file_1):
        return
    
    file_exp_1 = file_1.split(".")[-1]
    file_exp_2 = file_2.split(".")[-1]

    try:
        if file_exp_1 == "json" and file_exp_2 == "xml":
            json_to_xml(file_1, file_2)
        elif file_exp_1 == "json" and file_exp_2 == "yaml":
            json_to_yaml(file_1, file_2)
        elif file_exp_1 == "xml" and file_exp_2 == "json":
            xml_to_json(file_1, file_2)
        elif file_exp_1 == "xml" and file_exp_2 == "yaml":
            xml_to_yaml(file_1, file_2)
        elif file_exp_1 == "yaml" and file_exp_2 == "json":
            yaml_to_json(file_1, file_2)
        elif file_exp_1 == "yaml" and file_exp_2 == "xml":
            yaml_to_xml(file_1, file_2)
        else:
            messagebox.showerror("Error", "Unsupported file conversion")
            return
        
        messagebox.showinfo("Success", "Task successful")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_input_file():
    file_path = filedialog.askopenfilename()
    file_input.set(file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".xml",
                                             filetypes=[("All Files", "*.*"),
                                                        ("XML files", "*.xml"),
                                                        ("JSON files", "*.json"),
                                                        ("YAML files", "*.yaml")])
    file_output.set(file_path)

root = tk.Tk()
root.title("File Converter")

file_input = tk.StringVar()
file_output = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Input File:").grid(row=0, column=0, sticky="e")
tk.Entry(frame, textvariable=file_input, width=50).grid(row=0, column=1)
tk.Button(frame, text="Browse", command=select_input_file).grid(row=0, column=2)

tk.Label(frame, text="Output File:").grid(row=1, column=0, sticky="e")
tk.Entry(frame, textvariable=file_output, width=50).grid(row=1, column=1)
tk.Button(frame, text="Browse", command=select_output_file).grid(row=1, column=2)

tk.Button(frame, text="Convert", command=convert).grid(row=2, columnspan=3, pady=10)

root.mainloop()