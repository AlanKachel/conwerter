# Gówny plik programu do konwersji json xml yaml
import json
import yaml
import sys
import os
import xmltodict

def test_argv():
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".xml"):
            file_1 = sys.argv[1]
        elif sys.argv[1].endswith(".json"):
            file_1 = sys.argv[1]
        elif sys.argv[1].endswith(".yaml"):
            file_1 = sys.argv[1]

        if sys.argv[2].endswith(".xml"):
            file_2 = sys.argv[2]
            return file_1, file_2
        elif sys.argv[2].endswith(".json"):
            file_2 = sys.argv[2]
            return file_1, file_2
        elif sys.argv[2].endswith(".yaml"):
            file_2 = sys.argv[2]
            return file_1, file_2
        return None, None
    
    elif len(sys.argv) > 1 and len(sys.argv) != 3:
        print("Invalid number of arguments")
        raise(NameError)
    else:
        print("No arguments")
        pass
    return None, None

def file_name_distributor(file_1, file_2):
    tem_list = file_1.split(".")
    file_exp_1 = tem_list[len(tem_list)-1]

    tem_list = file_2.split(".")
    file_exp_2 = tem_list[len(tem_list)-1]
    return file_exp_1, file_exp_2

def file_existing(file_1):
    if os.path.exists(file_1):
        pass
    else:
        print("Invalid file name, try again!")
        raise(TimeoutError)

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

if __name__=="__main__":
    file_1, file_2= test_argv()
    if type(file_1) == str:
        file_existing(file_1)
        file_exp_1, file_exp_2 = file_name_distributor(file_1, file_2)
        match file_exp_1:
            case "json":
                match file_exp_2:
                    case "xml":
                        json_to_xml(file_1, file_2)
                        print("Task successful")
                    case "yaml":
                        json_to_yaml(file_1, file_2)
                        print("Task successful")
            case "xml":
                match file_exp_2:
                    case "json":
                        xml_to_json(file_1, file_2)
                        print("Task successful")
                    case "yaml":
                        xml_to_yaml(file_1, file_2)
                        print("Task successful")
            case "yaml":
                match file_exp_2:
                    case "json":
                        yaml_to_json(file_1, file_2)
                        print("Task successful")
                    case "xml":
                        yaml_to_xml(file_1, file_2)
                        print("Task successful")
