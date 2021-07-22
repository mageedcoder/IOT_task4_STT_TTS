# IOT_task4_STT_TTS
task4 (subtask1)

the goal is to make use of speech to text and text to speech services.

in the file *transcribe.py*, after creating ibm speech to text service in ibmcloud. I cloned from the realtime speach to text repositry made nicknochnack. I tweaked the apikeys and ragions according to my ibm service credentials. through Web Socket Connection the audio from microphone is converted into text and printed on the screen, I tweaked the code so it writes the last recorded chunk of speech transcripts in the file named *output.txt*.

in the file *Speech-to-Text.py*, speach service was utilized by taking the *output.txt* file created in the previous step. The returned output from text to speech service is written into *Speech-to-Text.mp3*
