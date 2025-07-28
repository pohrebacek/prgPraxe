import csv
import random
import pandas as pd #díky týhle library se můžou ty soubory csv upravovat



def getSongs():
    songs = []
    with open("songs.csv", "r", encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
           songs.append(line["name"])
    return songs

#for song in songs:
#    print(song)

print("Write a number of an option below: ")
print("1. Generate songs")
print("2. Show all songs")
print("3. Add song")
print("4. Delete song")
print("5. Exit")
option = int(input("Option: "))
while (option != 5):

    match option:
        case 1:
            songs = getSongs()
            howMany = input("Write how many songs from "+str(len(songs))+ " you want to randomly generate: ")
            while not howMany.isnumeric():
                howMany = input("Please, write a number of how many songs from " + str(len(songs)) + " you want to randomly generate: ")
            print("-------------")
            for i in range(0, int(howMany)):
                generatedSong = songs[random.randint(0, len(songs)-1)]
                songs.remove(generatedSong)
                print(generatedSong)

        case 2:
            print("-------------")
            songs = getSongs()
            for i in range(len(songs)):
                print(str(i + 1) + ". " + str(songs[i]))

        case 3:
            songs = getSongs()
            songs = [song.lower() for song in songs]
            print("-------------")
            songToAdd = input("Write name of the song you want to add to the song list: ")
            while songToAdd.lower() in songs:
                print("Song you entered is already in the list!")
                songToAdd = input("Write name of the song you want to add to the song list: ")
            with open("songs.csv", "a", encoding="utf-8", newline="") as songs_file:
                songs_file_writer = csv.writer(songs_file)
                line = [songToAdd]
                songs_file_writer.writerow(line)
            print("Song added succefully!")
        case 4:
            songs = getSongs()
            songs = [song.lower() for song in songs]
            print("-------------")
            songToDelete = input("Write name of the song you want to delete from the song list: ")
            while songToDelete.lower() not in songs:
                print("Song you entered isn't in the list!")
                songToDelete = input("Write name of the song you want to delete from the song list: ")
            songs2 = getSongs()
            for song in songs2: #ošetři to když uživatel zadá lowercase songu, tak aby to poznalo jakou v tom souboru smazat, pokud se lowercase obou rovná, tak se songToDelete přepíše na ten song ze souboru
                if song.lower() == songToDelete.lower():
                    songToDelete = song
                    break
            df = pd.read_csv("songs.csv", index_col="name")
            df = df.drop(songToDelete)
            df.to_csv("songs.csv", index=True)
            print("Song deleted succefully!")

    print("-------------")
    print("Write a number of an option below: ")
    print("1. Generate songs")
    print("2. Show all songs")
    print("3. Add song")
    print("4. Delete song")
    print("5. Exit")
    option = int(input("Option: "))
