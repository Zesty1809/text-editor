# Program 12: Count file stats
def count_file_stats(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
        print(f"Lines: {num_lines}, Words: {num_words}, Characters: {num_chars}")