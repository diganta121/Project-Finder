import os, sys, time, re

search_folders = ["C:\\Users\\dutta\\Desktop\\projects"]
search_file_type = ["txt", "py", "js", "jsx", "ts", "ino", "c", "java", "cpp", "md"]


def main():
    while True:
        print("what do you want to find? (\\n > exit)")
        inp = input(">  ").lower()
        if len(inp) < 2:
            return
        dirs = get_dir_r(search_folders[0])
        found_folders = filter_files(inp, dirs)
        print(dirs)
        print(found_folders)


def get_dir_r(parent_dir):
    # sub = os.walk(parent_dir)
    # sub = [i for i in sub]
    # print(sub)
    sub_ = os.listdir(parent_dir)
    sub_dirs = [x.lower() for x in sub_]
    return sub_dirs


def find_word_substring(word_list, substring):
    pattern = re.compile(re.escape(substring))
    matching_words = [word for word in word_list if pattern.search(word)]
    return matching_words


def filter_files(inp, dir_list):
    # func to read files and filter matches
    m = find_word_substring(dir_list, inp)  # match file names

    return m


main()
# get_dir_r(search_folders[0])
