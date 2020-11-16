import json
import time
import os.path
from os.path import join


def set_name_file(va_count, va_specialization, va_area):
    localtime = time.strftime("%d-%m-%Y_%H-%M-%S", time.localtime())
    name_of_file = localtime + '__' + str(va_count) + '_' + va_specialization + '_' + va_area + '.json'
    path = path_exist(name_of_file)
    return join(path, name_of_file)


def write_json_to_disk(data, va_count, va_specialization, va_area):
    json_f = json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
    with open(set_name_file(va_count, va_specialization=decode_spec_area(va_specialization),
                            va_area=decode_spec_area(va_area)), 'w',
              encoding="utf-8") as f:
        f.write(json_f)
        f.close()


def path_exist(name_of_file):

    if os.path.exists(os.getcwd() + "\\Output"):
        print("Saving in: " + os.getcwd() + "\\Output" + "\\" + name_of_file)
        return os.getcwd() + "\\Output"
    else:
        os.mkdir("Output")
        print("Creating and save in: " + os.getcwd() + "\\Output" + "\\" + name_of_file)
        return os.getcwd() + "\\Output"


def decode_spec_area(common_code):
    if common_code == "40":
        return "kz"
    elif common_code == "160":
        return "almaty"
    elif common_code == "159":
        return "astana"
    elif common_code == "1":
        return "it"
    elif common_code == "2":
        return "buh"
    elif common_code == "17":
        return "sales"
    else:
        return "NONE"
