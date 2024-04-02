from commands.ping.message import ping
from commands.avatar.message  import avatar
from commands.gif.message  import gif
commands = [
   ping,
   avatar,
   gif
]


async def sync(messageCommandName, message):
   for x in commands:
      
      if x.__name__ in messageCommandName[1:]:
       await  x(message)
       print(message.author, "usou:", x.__name__)