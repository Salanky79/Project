import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#     JSON string               JSON file
#        (str)                    (.json)
#          |                          |
#  -----------------           -----------------
#  |  json.loads()  |          |  json.load()  |
#  -----------------           -----------------
#          ↓                          ↓
#      Python object (dict, list, int, str, ... )
#          ↑                          ↑
#  -----------------           -----------------
#  | json.dumps()  |           | json.dump()   |
#  -----------------           -----------------
#        (str)                    (.json file)
#     JSON string               JSON file


# VD data => list
# [
#     {
#         "name": "My Playlist",
#         "description": "Some cool videos",
#         "rating": 4.5,
#         "videos": [
#             {"title": "Video 1", "link": "https://...", "seen": False},
#             {"title": "Video 2", "link": "https://...", "seen": True}
#         ]
#     },
#     {
#         "name": "Another Playlist",
#         "description": "More videos",
#         "rating": 5,
#         "videos": []
#     }
# ]
