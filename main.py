# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import urllib.request
import os


def download(url, prefix, files):
    file_save_dir = 'files/'
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']
    for offset in range(int(files / len(chars))):
        for char in chars:
            filename = prefix + str(chars[offset] + char)
            imob = urllib.request.urlopen(url + filename)
            print(f"Downloading {filename}\n")
            # read file and save
            if not os.path.exists(file_save_dir + filename):
                f = open(file_save_dir + filename, "wb")
                f.write(imob.read())
                f.close()

                # display file information
                print(f"Downloaded file: {prefix + str(chars[offset] + char)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    download('http://google.com/', 'x', 26 * 26)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
