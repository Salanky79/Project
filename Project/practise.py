import os
import webbrowser
import json


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
            'title': self.title,
            'link': self.link,
            'seen': self.seen
        }

    @staticmethod
    def from_dict(data):
        v = Video(data['title'], data['link'])
        v.seen = data.get('seen', False)
        return v


class Playlist:
    def __init__(self, name, description, rating, videos):
        self.name = name
        self.desctiption = description
        self.rating = rating
        self.videos = videos

    def to_dict(self):
        vids = []
        for i in range(len(self.videos)):
            vids.append(self.videos[i].to_dict())
        return {
            'name': self.name,
            'description': self.desctiption,
            'rating': self.rating,
            'videos': vids
        }

    @staticmethod
    def from_dict(data):
        videos = []
        for i in range(data.get('videos', [])):
            videos.append(Video.from_dict(data['videos'][i]))
        return Playlist(data["name"], data["description"], data["rating"], videos)


def write_to_json(playlists):
    data = []
    for i in range(len(playlists)):
        data.append(playlists[i].to_dict())
    with open("in4.json", "w") as f:
        json.dump(f)
    print("Suceesfully write to json.")


def read_from_json():
    playlists = []
    if not os.path.exists("in4.json"):
        return playlists
    with open("in4.json", "r") as f:
        data = json.load(f)
    for i in range(len(data)):
        playlists.append(Playlist.from_dict(data[i]))

    return playlists
