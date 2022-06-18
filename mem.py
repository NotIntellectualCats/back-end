import vk_api

with open("config_example.txt", "r") as F:
  token = F.readline()

session = vk_api.VkApi(token=token)

vk = session.get_api()




def create_memes():
  result = []

  
  images = session.method("photos.get", {"owner_id": -197700721, "album_id": 281940823, "extended": 1})
  for i in range(len(images["items"])):
    result.append([images["items"][i]["sizes"][-1]["url"], images["items"][i]["likes"]["count"]])

  images = session.method("photos.get", {"owner_id": -107232016, "album_id": 242754859, "count": 300, "extended": 1})
  for i in range(len(images["items"])):
    result.append([images["items"][i]["sizes"][-1]["url"], images["items"][i]["likes"]["count"]])
  print(len(result))
  return result

