import os
import function

def main():
    print("Pixiv Ugoira to APNG Converter")
    print("警告：")
    print("- 确保输入目录包含散装图片（jpg/png）和animation.json文件。")
    print("- animation.json应来自Pixiv的ugoira数据。")
    print("- 输出文件为APNG格式，会覆盖同名文件。")
    print("- 请遵守版权法，仅用于个人用途。")
    print("- 严禁用于合成或处理儿童色情内容，违反法律。")
    
    directory = input("请输入包含图片和JSON的目录路径：").strip()
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print("错误：目录不存在或不是有效目录。")
        return
    
    try:
        ls, js = function.read_floder(directory)
        if not ls:
            print("错误：目录中未找到图片文件（jpg/png）。")
            return
        if not js:
            print("错误：目录中未找到animation.json文件。")
            return
        
        output_path = input("请输入输出APNG文件路径（例如：output.apng）：").strip()
        if not output_path:
            print("错误：输出路径不能为空。")
            return
        
        png = function.create_apng_picture(directory, ls, js)
        png.save(output_path)
        print(f"成功！APNG已保存到：{output_path}")
    
    except Exception as e:
        print(f"错误：{e}")

if __name__ == "__main__":
    main()
