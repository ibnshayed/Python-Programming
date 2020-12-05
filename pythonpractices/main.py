import pyjokes

for joke in pyjokes.get_jokes('en','all'):
    print(joke)
    