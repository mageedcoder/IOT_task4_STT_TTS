# IOT_task4_STT_TTS
task4 (part1)

the goal is to make use of speech to text and text to speech services.

in the file *transcribe.py*, I started by creating ibm speech to text service in ibmcloud. I used speech to text service cloned from the realtime speach to text repositry made nicknochnack. I tweaked the apikeys and ragions according to my ibm service credentials. I tweaked the code so it writes the last recorded chunk of speech transcripts in the file named *output.txt*.

in the file *Speech-to-Text.py*, I used text to speach service which utilize the *output.txt* file created in the previous step. The returned output from text to speech service is written into *Speech-to-Text.mp3*
