import os
import apng
import PIL
import json

def read_floder(directory):
    js=''
    directory=os.path.normpath(directory)
    if not os.path.exists(directory) or not os.path.isdir(directory):
        raise ValueError(f"Directory {directory} does not exist or is not a directory")
    ls=os.listdir(directory)
    li=[]
    for item in ls:
        part=item[-3:]
        if part=='jpg' or part=='png':
            li.append(item)
        else:
            part=item[-4:]
            if part=='json':
                js=item
    return li,js
def read_json(location):
    try:
        with open(location, "r", encoding="utf-8") as f:
            data=json.load(f)
        needed_list=data['ugokuIllustData']['frames']
        return needed_list
    except FileNotFoundError:
        raise ValueError(f"JSON file {location} not found")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {location}: {e}")
    except KeyError as e:
        raise ValueError(f"Missing key in JSON: {e}")

def create_apng_picture(directory,ls,js):
    picture=apng.APNG()
    if js != '':
        li=read_json(os.path.join(directory, js))
        for dictionary in li:
            file_name=dictionary['file']
            ms=int(dictionary['delay'])
            file_locate=os.path.join(directory, file_name)
            picture.append_file(file_locate, delay=ms)
    return picture
    


#test
if __name__=='__main__':
    pass  # 测试代码已删除