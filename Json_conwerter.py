# Gówny plik programu do konwersji json xml yaml
import json
import yaml
import xml.etree.cElementTree as ET
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
        print("Inwalid number of argument")
        raise(NameError)
    else:
        print("0 argument")
        pass
    return None, None

def file_existing(file_1):
    if os.path.exists(file_1):
        print("Plik istnieje")
        pass
    else:
        raise(TimeoutError)


def json_to_xml(file_1, file_2):
    with open(file_1, "r") as file:
        data = json.load(file)
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


if __name__=="__main__":
    file_1, file_2 = test_argv()
    print(file_1, file_2)
    if type(file_1) == str:
        file_existing(file_1)
        xml_to_json(file_1, file_2)

