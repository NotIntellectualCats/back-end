import vk_api

with open("config_example.txt", "r") as F:
  token = F.readline()

session = vk_api.VkApi(token=token)

vk = session.get_api()


#железное





def get_album(user_id, album_id):
  images = session.method("photos.get", {"owner_id": user_id, "album_id": album_id, "extended": 1})
  count_likes = []
  usernames = []
  for i in images["items"]:
    count_likes.append(i["likes"]["count"])
    usernames.append(str(i["user_id"]))

  for i in range(len(count_likes)):
    print(f'user with id "{usernames[i]}" have  {count_likes[i]} likes')


  


get_album(-197700721, 281940823)
#подача id сообщества и альбома в функцию
