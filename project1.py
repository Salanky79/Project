import os
import webbrowser


class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.seen = False

    def open(self):
        webbrowser.open(self.link)
        self.seen = True


class Playlist:
    def __init__(self, name, description, rating, videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos


def read_video():
    title = input(f"Title: ")
    link = input(f"link: ")
    video = Video(title, link)
    return video


def read_videos():
    videos = []
    while True:
        try:
            a = int(input("Enter Number of videos: "))
            break
        except ValueError:
            print("Please enter a number.")
    for i in range(a):
        print(f"--VIDEO {i+1}---")
        video = read_video()
        videos.append(video)

    return videos


def print_video(video):
    print("Title: " + video.title)
    print("Link: " + video.link)


def print_videos(videos):
    for i in range(len(videos)):
        print(f"Vid {i + 1}:")
        print_video(videos[i])
        print("")


def write_vid_to_txt(video, f):
    f.write(video.title + "\n")
    f.write(video.link + "\n")


def write_vids_to_txt(videos, f):

    total = len(videos)
    f.write(str(total))
    f.write("\n")
    for i in range(len(videos)):
        write_vid_to_txt(videos[i], f)


def read_vid_from_txt(f):
    title = f.readline().strip()
    link = f.readline().strip()
    video = Video(title, link)
    return video


def read_vids_from_txt(f):

    videos = []
    total = f.readline()
    total = int(total)
    for i in range(total):
        video = read_vid_from_txt(f)
        videos.append(video)
    return videos


def print_vid_from_txt(video):
    print("Title: " + video.title)
    print("Link: " + video.link)


def print_vids_from_txt(videos):
    for i in range(len(videos)):
        print(f"Vid {i + 1}:")
        print_vid_from_txt(videos[i])
        print("")


def read_playlist():
    playlist_name = input("Enter playlist name: ")
    playlist_description = input("Enter playlist description: ")
    playlist_rating = rating_range("Enter playlist rating(0-5): ", 0, 5)
    playlist_videos = read_videos()
    playlist = Playlist(playlist_name, playlist_description,
                        playlist_rating, playlist_videos)
    return playlist


def rating_range(prompt, min, max):
    while True:
        rate = input(prompt)
        try:
            value = float(rate)
            if min <= value <= max:
                return value
            else:
                print(f"Please enter a number between {min} and {max}.")
        except ValueError:
            print("Enter a number")


def write_playlist_to_txt(playlist):
    with open("in4.txt", "w", encoding="utf-8") as f:
        f.write(playlist.name + "\n")
        f.write(playlist.description + "\n")
        f.write(str(playlist.rating) + "\n")
        write_vids_to_txt(playlist.videos, f)
    print("Successfully write playlist to txt")


def read_playlist_from_txt():
    with open("in4.txt", "r", encoding="utf-8") as f:
        playlist_name = f.readline().strip()
        playlist_description = f.readline().strip()
        playlist_rating = float(f.readline().strip())
        playlist_videos = read_vids_from_txt(f)

    playlist = Playlist(playlist_name, playlist_description,
                        playlist_rating, playlist_videos)
    return playlist


def print_playlist(playlist):
    print("Playlist name: " + playlist.name)
    print("Playlist description: " + playlist.description)
    print(f"Playlist rating: {playlist.rating:.1f}\n")
    print_videos(playlist.videos)


def show_menu():
    print("MAIN MENU: ")
    print("------------------------------")
    print("| Option 1: Create a playlist |")
    print("| Option 2: Show playlists    |")
    print("| Option 3: Play a video      |")
    print("| Option 4: Add a video       |")
    print("| Option 5: Update playlist   |")
    print("| Option 6: Remove a video    |")
    print("| Option 7: Save and exit     |")
    print("------------------------------")


def select_in_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(prompt)
    return int(choice)


def play_video(playlist):
    total = len(playlist.videos)
    for i in range(total):
        video = playlist.videos[i]
        print(f"Video {i + 1}: {video.title}")
    choice = select_in_range(f"Enter video to play (1 - {total}): ", 1, total)
    print(f"Open video {playlist.videos[choice - 1].title}")
    playlist.videos[choice - 1].open()
    print("\n")


def add_video(playlist):
    print("Enter video information: ")
    new_video_title = input(f"Title: ")
    new_video_link = input(f"link: ")
    new_video = Video(new_video_title, new_video_link)
    playlist.videos.append(new_video)
    return playlist


def update_playlist(playlist):
    while True:
        print("\nUpdate playlist: ")
        print("1. Playlist name: " + playlist.name)
        print("2. Playlist description: " + playlist.description)
        print("3. Playlist rating: " + str(playlist.rating))
        print("4. Back to main menu")

        choice = select_in_range(
            "Select what you want to change (1-4): ", 1, 4)
        if choice == 1:
            playlist.name = input("New name: ")
        elif choice == 2:
            playlist.description = input("New description: ")
        elif choice == 3:
            playlist.rating = rating_range("New rating (0-5): ", 0, 5)
        else:
            break

    return playlist


def remove_video(playlist):
    if not playlist.videos:
        print("No videos to remove.")
        return playlist

    total = len(playlist.videos)
    print("Videos in playlist: ")
    for i, video in enumerate(playlist.videos, start=1):
        print(f"Video {i}: {video.title}")

    choice = select_in_range(
        f"Choose a video to delete (1, {total}): ", 1, total)
    playlist.videos.pop(choice - 1)
    print(f"Removed video {choice}")

    return playlist


def main():
    # videos = read_videos()
    # print("\n---\n")
    # print_videos(videos)
    # write_vids_to_txt(videos)
    # print("\n\n\n")
    # a = read_vids_from_txt()
    # print_vids_from_txt(a)

    playlist = None
    # Kiểm tra file có tồn tại để load playlist
    if os.path.exists("in4.txt"):

        playlist = read_playlist_from_txt()
        print("Loaded existing playlist from file.\n")

    while True:
        show_menu()
        choice = select_in_range("Select an option (1 - 7): ", 1, 7)
        print("\n")
        if choice == 1:
            playlist = read_playlist()
            input("Press Enter to continue.")
        elif choice == 2:
            if playlist is None:
                print("\nPlaylist is not existed. Please Enter a playlist first.")
            else:
                print_playlist(playlist)
            input("Press Enter to continue.")
        elif choice == 3:
            if playlist is None:
                print("There's no videos to play")
            else:
                play_video(playlist)
            input("Press Enter to continue.")
        elif choice == 4:
            if playlist is None:
                print("Please create a playlist first.")
            else:
                # phai khai bao bien playlist de cap nhat global
                playlist = add_video(playlist)
        elif choice == 5:
            if playlist is None:
                print("Please create a playlist first.")
            else:
                # phai khai bao bien playlist de cap nhat global
                playlist = update_playlist(playlist)
                print("Updated sucessfully! ")
        elif choice == 6:
            if playlist is None:
                print("Please create a playlist first.")
            else:
                playlist = remove_video(playlist)
        elif choice == 7:
            if playlist is None:
                print("No playlist to save. Exiting without saving.")
            else:
                write_playlist_to_txt(playlist)
            break


main()
