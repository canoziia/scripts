# 从根文件夹遍历，检测文件夹是否是年份，是年份则递归把文件夹下任何地方的所有照片移出该文件夹。
# 如果文件夹下没有照片，则删除该文件夹。

import os
import shutil


def move(destination, depth=""):
    print("正在移动: " + os.path.join(destination, depth))
    for file_or_dir in os.listdir(os.path.join(destination, depth)):
        if file_or_dir == "@eaDir":
            # 删除@eaDir文件夹以及其中的所有文件
            print("正在删除: " + os.path.join(destination, depth, file_or_dir))
            shutil.rmtree(os.path.join(destination, depth, file_or_dir))
            continue
        if os.path.isfile(os.path.join(destination, depth, file_or_dir)):
            try:
                shutil.move(os.path.join(
                    destination, depth, file_or_dir), destination)
            except shutil.Error as e:
                print(e)
                print("正在尝试覆盖复制文件:")
                # 移动并覆盖文件
                shutil.move(os.path.join(destination, depth, file_or_dir),
                            os.path.join(destination, file_or_dir))

        else:
            move(destination, os.path.join(depth, file_or_dir))
    os.rmdir(os.path.join(destination, depth))


def main(path):
    print("正在移动: " + path)
    for file_or_dir in os.listdir(path):
        if os.path.isdir(os.path.join(path, file_or_dir)):
            if file_or_dir.isdigit():
                move(path, file_or_dir)
            else:
                main(os.path.join(path, file_or_dir))


# python organize.py /path/to/your/photos
if __name__ == "__main__":
    import sys
    main(sys.argv[1])
