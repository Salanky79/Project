import os
import webbrowser
import json

# ---------------------Define Object-------------------------


class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.seen = False

    def open(self):
        webbrowser.open(self.link)
        self.seen = True

    def to_dict(self):
        return {
            "title": self.title,
            "link": self.link,
            "seen": self.seen
        }

    @staticmethod
    def from_dict(data):
        v = Video(data["title"], data["link"])
        v.seen = data.get("seen", False)
        return v


class Playlist:
    def __init__(self, name, description, rating, videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos

    def to_dict(self):
        vids = []
        for i in range(len(self.videos)):
            vids.append(self.videos[i].to_dict())
        return {
            "name": self.name,
            "description": self.description,
            "rating": self.rating,
            "videos": vids
        }

    @staticmethod
    def from_dict(data):
        videos = []
        for i in range(len(data.get("videos", []))):
            videos.append(Video.from_dict(data["videos"][i]))
        return Playlist(data["name"], data["description"], data["rating"], videos)


# ----------------------- File JSON --------------------------------

def write_playlists_to_json(playlists):
    data = []
    for i in range(len(playlists)):
        data.append(playlists[i].to_dict())
    with open("in4.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("💾 Successfully saved playlists to JSON.\n")


def read_playlists_from_json():
    playlists = []
    if not os.path.exists("in4.json"):
        return playlists
    with open("in4.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for i in range(len(data)):
        playlists.append(Playlist.from_dict(data[i]))
    return playlists


# ------------------- Video functions -------------------

def read_video():
    title = input("🎬 Title: ")
    link = input("🔗 Link: ")
    return Video(title, link)


def read_videos():
    videos = []
    while True:
        try:
            a = int(input("Enter number of videos: "))
            break
        except ValueError:
            print("⚠️ Please enter a number.")
    for i in range(a):
        print(f"\n-- VIDEO {i+1} --")
        videos.append(read_video())
    return videos


def print_video(video):
    print("🎬 Title: " + video.title)
    print("🔗 Link: " + video.link)


def print_videos(videos):
    for i in range(len(videos)):
        print(f"Vid {i+1}:")
        print_video(videos[i])


# ------------------- Playlist operations -------------------

def read_playlist():
    playlist_name = input("📝 Enter playlist name: ")
    playlist_description = input("📝 Enter playlist description: ")
    playlist_rating = rating_range("⭐ Enter playlist rating(0-5): ", 0, 5)
    playlist_videos = read_videos()
    return Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)


def print_playlist(playlist):

    print("📛 Name: " + playlist.name)
    print("📝 Description: " + playlist.description)
    print(f"⭐ Rating: {playlist.rating:.1f}")
    print_videos(playlist.videos)
    print("\n")


def select_playlist(playlists):
    if len(playlists) == 0:
        print("⚠️ No playlists exist.")
        return None
    print("\n📂 Playlists:")
    for i in range(len(playlists)):
        print(f"{i+1}. {playlists[i].name}")
    choice = select_in_range("Select playlist: ", 1, len(playlists))
    return playlists[choice-1]


def update_playlist(playlist):
    while True:
        print("\n🔧 Update playlist: ")
        print("1. 📛 Playlist name: " + playlist.name)
        print("2. 📝 Playlist description: " + playlist.description)
        print("3. ⭐ Playlist rating: " + str(playlist.rating))
        print("4. 🔙 Back to playlist menu")

        choice = select_in_range(
            "Select what you want to change (1-4): ", 1, 4)
        if choice == 1:
            playlist.name = input("📛 New name: ")
        elif choice == 2:
            playlist.description = input("📝 New description: ")
        elif choice == 3:
            playlist.rating = rating_range("⭐ New rating (0-5): ", 0, 5)
        else:
            break
    print("✅ Updated successfully!")


def delete_playlist(playlists):
    if len(playlists) == 0:
        print("⚠️ No playlists to delete.")
        return
    for i in range(len(playlists)):
        print(f"{i+1}. {playlists[i].name}")
    choice = select_in_range(
        f"Select a playlist to delete (1-{len(playlists)}): ", 1, len(playlists))
    removed = playlists.pop(choice-1)
    print(f"🗑️ Deleted playlist: {removed.name}")


def search_playlists(playlists):
    keyword = input("🔍 Enter keyword to search: ").lower()
    found = []
    for i in range(len(playlists)):
        if keyword in playlists[i].name.lower() or keyword in playlists[i].description.lower():
            found.append(playlists[i])

    if len(found) >= 1:
        for i in range(len(found)):
            print("Playlist(s) found: ")
            print(
                f"{i+1}. {found[i].name} | {found[i].description} | ⭐ {found[i].rating}")
        a = select_in_range("Pick a playlist: ", 1, len(found))
        return found[a - 1]
    else:
        print("⚠️ No playlists found.")
        return None
    # ------------------- Playlist functions -------------------


def play_video(playlist):
    total = len(playlist.videos)
    if total == 0:
        print("⚠️ No videos in this playlist.")
        return

    while True:
        print("How do you want to choose a video?")
        print("1. 🔍 Search by keyword")
        print("2. 📋 Show all videos")
        choice_method = select_in_range("Select an option (1-2): ", 1, 2)

        if choice_method == 2:
            for i in range(total):
                status = "✅" if playlist.videos[i].seen else "🔴"
                print(f"{i+1}.{status} {playlist.videos[i].title}")
            choice = select_in_range(
                f"Enter video to play (1 - {total}): ", 1, total)
            print(f"▶️ Opening video: {playlist.videos[choice-1].title}")
            playlist.videos[choice-1].open()
            print("\n")
            break
        else:
            found = []
            a = playlist.videos
            keyword = input("Enter keywords: ").lower()
            for i in range(len(a)):
                if keyword in a[i].title.lower():
                    print(f"{i + 1}. {a[i].title}")
                    found.append(a[i])

            if len(found) >= 1:
                choice = select_in_range(
                    f"Enter video to play(1-{len(found)}) : ", 1, len(found))
                print(f"▶️ Opening video: {found[choice-1].title}")
                found[choice-1].open()
                break
            else:
                print("No videos found.\n")


def add_video(playlist):
    print("➕ Enter video information: ")
    playlist.videos.append(read_video())
    print("✅ Added video successfully!")


def remove_video(playlist):
    if len(playlist.videos) == 0:
        print("⚠️ No videos to remove.")
        return

    for i in range(len(playlist.videos)):
        print(f"{i+1}. {playlist.videos[i].title}")
    choice = select_in_range(
        f"Choose a video to delete (1-{len(playlist.videos)}): ", 1, len(playlist.videos))
    removed = playlist.videos.pop(choice-1)
    print(f"🗑️ Removed video: {removed.title}")


def rating_range(prompt, min, max):
    while True:
        rate = input(prompt)
        try:
            value = float(rate)
            if min <= value <= max:
                return value
            else:
                print(f"⚠️ Please enter a number between {min} and {max}.")
        except ValueError:
            print("⚠️ Enter a number")


# ------------------- Menu & Helper -------------------

def show_main_menu():
    print("\nMAIN MENU: ")
    print("------------------------------")
    print("| 1: 🎵 Create a playlist    |")
    print("| 2: 📂 Show playlists       |")
    print("| 3: ▶️ Select a playlist     |")
    print("| 4: ❌ Delete a playlist    |")
    print("| 5: 🔎 Search playlists     |")
    print("| 6: 💾 Save and exit        |")
    print("----------------------------------")


def show_playlist_menu(playlist):
    print(f"\nPlaylist: {playlist.name}")
    print("------------------------------")
    print("| 1: ▶️ Play a video         |")
    print("| 2: ➕ Add a video         |")
    print("| 3: ✏️ Update playlist      |")
    print("| 4: 🗑️ Remove a video       |")
    print("| 5: 🔙 Back to main menu   |")
    print("----------------------------------")


def select_in_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(prompt)
    return int(choice)


# ------------------- Main program -------------------

def main():
    playlists = read_playlists_from_json()
    if len(playlists) > 0:
        print("💾 Loaded existing playlists from JSON.\n")

    while True:
        show_main_menu()
        choice = select_in_range("Select an option (1-6): ", 1, 6)

        if choice == 1:
            playlists.append(read_playlist())
            input("Press Enter to continue.")
        elif choice == 2:
            if len(playlists) == 0:
                print("⚠️ No playlists exist.")
            else:
                for i in range(len(playlists)):
                    print(f"Playlist {i + 1}: ")
                    print_playlist(playlists[i])
            input("Press Enter to continue.")
        elif choice == 3:
            playlist = select_playlist(playlists)
            if playlist is None:
                input("Press Enter to continue.")
                continue
            while True:
                show_playlist_menu(playlist)
                sub_choice = select_in_range("Select an option (1-5): ", 1, 5)
                if sub_choice == 1:
                    play_video(playlist)
                    input("Press Enter to continue.")
                elif sub_choice == 2:
                    add_video(playlist)
                    input("Press Enter to continue.")
                elif sub_choice == 3:
                    update_playlist(playlist)
                    input("Press Enter to continue.")
                elif sub_choice == 4:
                    remove_video(playlist)
                    input("Press Enter to continue.")
                elif sub_choice == 5:
                    break
        elif choice == 4:
            delete_playlist(playlists)
            input("Press Enter to continue.")
        elif choice == 5:
            playlist = search_playlists(playlists)
            while True:
                show_playlist_menu(playlist)
                sub_choice = select_in_range("Select an option (1-5): ", 1, 5)
                if sub_choice == 1:
                    play_video(playlist)
                    input("Press Enter to continue.")
                elif sub_choice == 2:
                    add_video(playlist)
                    input("Press Enter to continue.")
                elif sub_choice == 3:
                    update_playlist(playlist)
                    input("Press Enter to continue.")
                elif sub_choice == 4:
                    remove_video(playlist)
                    input("Press Enter to continue.")
                elif sub_choice == 5:
                    break
        elif choice == 6:
            if len(playlists) > 0:
                write_playlists_to_json(playlists)
            print("👋 Exiting program...")
            break


main()
