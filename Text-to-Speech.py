
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'WUz2pqAbHmjUEEx4_Qo3hbBjpvybUO2VnCwGsbQrLVYL'
url = 'https://api.eu-de.text-to-speech.watson.cloud.ibm.com/instances/f95c96c3-1d37-4ca7-b8f9-bf87a31f01e0'

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)



with open('output.txt', 'r') as f:
    text = f.readlines()


text = [line.replace('\n','') for line in text]


text = ''.join(str(line) for line in text)

with open('text-to-speech.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content)


import json
voices = tts.list_voices().get_result()
print(json.dumps(voices, indent=2))

