import os
import subprocess


def all_list():
    source_dir = "Source"
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), source_dir))
    files_list = os.listdir(path=".")   #os.listdir(path=".") - список файлов и директорий в папке.
    return files_list


def main(files_list):
    print("---start program")
    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Source")
    result_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Result")
    for i in files_list:
        input_path = os.path.join(source_dir, i)
        output_path = os.path.join(result_dir, i)
        command_sips = 'sips --resampleWidth 200 input_path’ command_cp = 'cp output_path’
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        subprocess.run(command_sips, command_cp)
    print("----end program")


main(all_list())
