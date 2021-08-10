song = """There was an old lady who swallowed a fly.
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a spider;
That wriggled and wiggled and tickled inside her.
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a bird;
How absurd to swallow a bird.
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a cat;
Fancy that to swallow a cat!
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a dog;
What a hog, to swallow a dog!
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a cow;
I don't know how she swallowed a cow!
She swallowed the cow to catch the dog,
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a horse...
...She's dead, of course!"""

ORIGINAL_ANIMALS_OF_THE_SONG = ['fly', 'spider', 'bird', 'cat', 'dog', 'cow', 'horse']


class Song:
    first_verse = "There was an old lady who swallowed a {}."
    middle_verse = "She swallowed the {} to catch the {};"
    last_verse = "I don't know why she swallowed a {} - perhaps she'll die!"
    final_verse_of_the_song = "There was an old lady who swallowed a {}...\n...She's dead, of course!"
    funny_verses = [
        'That wriggled and wiggled and tickled inside her.',
        'How absurd to swallow a {}.',
        'Fancy that to swallow a {}!',
        'What a hog, to swallow a {}!',
        "I don't know how she swallowed a {}!",
    ]

    def __init__(self, animals_for_song):
        if not animals_for_song:
            self.animals_for_song = ORIGINAL_ANIMALS_OF_THE_SONG
        else:
            self.animals_for_song = animals_for_song

    def adapt_original_lyrics(self):
        if len(self.animals_for_song) == 7:
            return song
        elif len(self.animals_for_song) == 1:
            final_verse_of_the_song = self.final_verse_of_the_song.format(self.animals_for_song[0])
            return final_verse_of_the_song
        else:
            amount_of_animals = len(self.animals_for_song)
            final_song = ""
            for position, animal in enumerate(self.animals_for_song):
                if position == 0:
                    final_song += self.first_verse.format(animal)
                    final_song += "\n" + self.last_verse.format(animal)
                elif position == amount_of_animals - 1:
                    final_song += "\n\n" + self.final_verse_of_the_song.format(animal)
                else:
                    pass
            return final_song


class Singer:
    def __init__(self):
        self.animals_for_song = []

    def choose_animals_for_song(self, animals_for_song):
        self.animals_for_song = animals_for_song

    def sing(self):
        return Song(self.animals_for_song).adapt_original_lyrics()


singer = Singer()
# singer.choose_animals_for_song(['fly', 'spider', 'bird', 'cat', 'dog', 'cow', 'horse'])
singer.choose_animals_for_song(['fly'])
print(singer.sing())
