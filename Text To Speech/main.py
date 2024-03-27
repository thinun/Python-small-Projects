from gtts import gTTS

text = 'Hello World! My name is Thinun Tharuhsika'
language = 'en'

txt_1 = gTTS(text=text, lang=language, slow=False)
txt_1.save('hello_world_2.mp3')


