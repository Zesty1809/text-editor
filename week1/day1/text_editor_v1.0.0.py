# 24 Oct 2025

def view_file(filename):
    with open(filename, 'r') as rf:
        size_to_read = 100

        rf_contents = rf.read(size_to_read)

        while len(rf_contents) > 0:
            print(rf_contents, end='')
            rf_contents = rf.read(size_to_read)


def write_file(filename, lines):
    with open(filename, 'w') as wf:
        wf.writelines(lines)


def append_file(filename, lines):
    with open(filename, 'a') as af:
        af.writelines(lines)


def replace_word(filename, old_word, new_word):
    with open(filename, 'r') as f:
        content = f.read()

    content = content.replace(old_word, new_word)

    with open(filename, 'w') as f:
        f.write(content)


def count_file_stats(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
        print(f"Lines: {num_lines}, Words: {num_words}, Characters: {num_chars}")