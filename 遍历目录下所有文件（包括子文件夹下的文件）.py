import os


def find_all_file(directory):
    assert os.path.isdir(directory), '"{}" is not a directory.'.format(directory)
    all_files = []
    for root, ds, fs in os.walk(directory):
        for f in fs:
            fullname = os.path.join(root, f)
            all_files.append(fullname)
    return all_files


print(find_all_file(r'A:\LOL pixels'))
