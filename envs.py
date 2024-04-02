import json
envFile = open("envs.json","r").read()
envs= json.loads(envFile)

token = envs['bot-token']

tenorGifToken= envs["tenorGifToken"]