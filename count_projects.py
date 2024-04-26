import os
import sys

extensions= [".py",".c",".cpp",".rs",".lua",".js",".ts",".jsx",".tsx",".java"]
skipped_files = ["manage.py","settings.py"]
skipped_lines = ["{","}","}}","{{"]
separator = "\\" if sys.platform == "win32" else "/"

def main():
    lines_count = 0
    code_counts = {}
    for directory in os.walk("."):
        files = directory[2]
        dirname = directory[0]
        for file in files:
            extension = file[file.rindex("."):]
            skipped_file = file in skipped_files
            if extension in extensions and not skipped_file:
                code_counts[extension] = code_counts.get(extension,0) + 1
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
    for k,v in code_counts.items():
        print(f"{k}: {v}")
        print(f"lines of  code: {lines_count}")

if __name__ == "__main__":
    main()


