# importing the requests library
import requests
import random
from envs import tenorGifToken



async def gif(message):
   if message.content.startswith("$gif"):
      URL = "https://g.tenor.com/v1/search?q="+message.content[3:]+"&key=$"+tenorGifToken+"&ContentFilter=G"
      r = requests.get(url = URL).json()

      print(r)
      random_index = random.randint(0, len(r['results']) - 1)
      result = r.results[random_index].url;

      await message.reply(result)