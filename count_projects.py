import os
import sys
import argparse

extensions:list[str]= [".py",".c",".cpp",".rs",".lua",".js",".ts",".jsx",".tsx",".java"]
skipped_files:list[str] = ["manage.py","settings.py"]
separator:str = "\\" if sys.platform == "win32" else "/"

def main():
    lines:int = 0
    code_counts:dict[str,int] = {}
    for directory in os.walk("."):
        files:list[str] = directory[2]
        dirname:str = directory[0]
        for file in files:
            extension:str = file[file.rindex("."):]
            skipped_file:bool = file in skipped_files
            if extension in extensions and not skipped_file:
                code_counts[extension] = code_counts.get(extension,0) + 1
                lines += count_lines(dirname,file)
    for k,v in code_counts.items():
        print(f"{k}: {v}")
        print(f"lines of  code: {lines}")

def count_lines(dirname,file) ->int:
    lines_count:int = 0
    skipped_lines:list[str] = ["{","}","}}","{{"]
    if dirname == ".":
        with open(f"{file}","r") as file_handle:
            for line in file_handle:
                if len(line) > 1 and line not in skipped_lines:
                    lines_count +=1
    else:
        with open(f"{dirname}{separator}{file}","r") as file_handle:
            for line in file_handle:
                if len(line) > 1 and line not in skipped_lines:
                    lines_count +=1
    return lines_count

if __name__ == "__main__":
    main()


