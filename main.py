# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import urllib


def download(url, prefix, files):
    file_save_dir = 'files'
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']
    for offset in range(files/len(chars)):
        for char in chars:
            imob = urllib.urlopen(url + prefix + str(chars[offset] + char))
            # read file and save
            f = open(file_save_dir + prefix + str(chars[offset] + char), "wb")
            f.write(imob.read())
            f.close()

            # display file information
            print(f"Downloaded file: {prefix + str(chars[offset] + char)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    download('http://google.com/', 'x', 26 * 26)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
