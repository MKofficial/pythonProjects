# This code was authored by Jindrich Matuska and slightly refactored by Ondrej Borysek.

import os


# from typing import Optional


# def chosedir(songs_folder: str, force_i: Optional[int] = None):
def chosedir(songs_folder, force_i=None):
    dicts = os.listdir(songs_folder)

    # Print the songs with numbers
    for i in range(len(dicts)):
        # print(f'{str(i+1)}) {dicts[i]}')
        print(str(i + 1), dicts[i])

    # Load users choice
    chosen_i = force_i
    if not chosen_i:
        chosen_i = int(input())

    # Load chosen song
    song_name = dicts[chosen_i - 1]
    path_to_song_folder = songs_folder + '/' + song_name

    # with open(f'{path_to_song_folder}/init.txt') as file:
    with open(path_to_song_folder + '/init.txt') as file:
        desc = file.readline()[:-1]
        song = file.readline()[:-1]
        desc = strList(desc.replace(" ", ""))
        song = strList(song.replace(" ", ""))
        dt = float(file.readline()[:-1])

    return path_to_song_folder, desc, song, dt


def strList(string):  # Converts string rep of list to list
    listcreate = []
    if not ("," in string):
        if string == "[]":
            return []
        string = string.replace("'", "")
        try:
            return int(string)
        except:
            return string
    start = 1
    inside = 0
    for i in range(1, len(string) - 1):
        if string[i] == "[":
            inside += 1
        elif string[i] == "]":
            inside -= 1
        elif string[i] == ",":
            if inside == 0:
                listcreate.append(strList(string[start: i]))
                start = i + 1
    listcreate.append(strList(string[start: -1]))
    return listcreate