ORIGINAL_ANIMALS_OF_THE_SONG = ['fly', 'spider', 'bird', 'cat', 'dog', 'cow', 'horse']

UN_ANIMAL=1

class Song:
    first_verse_of_the_song = "There was an old lady who swallowed a {}."
    first_verse = "There was an old lady who swallowed a {};"
    first_middle_verse = "She swallowed the {} to catch the {},"
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

        if len(self.animals_for_song) == UN_ANIMAL:
            return self.adaptar_cancion_para_un_solo_animal()
        else:
            amount_of_animals = len(self.animals_for_song)
            final_song = ""
            funny_verse_position = 0
            for position, animal in enumerate(self.animals_for_song):
                if position == 0:
                    final_song += self.first_verse_of_the_song.format(animal)
                    final_song += "\n" + self.last_verse.format(animal)
                elif position == amount_of_animals - 1:
                    final_song += "\n\n" + self.final_verse_of_the_song.format(animal)
                else:
                    final_song += "\n\n" + self.first_verse.format(animal)
                    if funny_verse_position == 0:
                        final_song += "\n" + self.funny_verses[funny_verse_position]
                    else:
                        final_song += "\n" + self.funny_verses[funny_verse_position].format(animal)
                    if position > 1:
                        amount_of_animals_for_use_in_middle_verse = position
                        while amount_of_animals_for_use_in_middle_verse > 0:
                            first_animal_in_verse = self.animals_for_song[amount_of_animals_for_use_in_middle_verse]
                            second_animal_in_verse = self.animals_for_song[
                                amount_of_animals_for_use_in_middle_verse - 1]
                            if amount_of_animals_for_use_in_middle_verse > 1:
                                final_song += "\n" + self.first_middle_verse.format(first_animal_in_verse,
                                                                                    second_animal_in_verse)
                            else:
                                final_song += "\n" + self.middle_verse.format(first_animal_in_verse,
                                                                              second_animal_in_verse)
                            amount_of_animals_for_use_in_middle_verse -= 1
                    else:
                        final_song += "\n" + self.middle_verse.format(animal, self.animals_for_song[position - 1])
                    final_song += "\n" + self.last_verse.format(self.animals_for_song[0])
                    if funny_verse_position == len(self.funny_verses) - 1:
                        funny_verse_position = 0
                    else:
                        funny_verse_position += 1
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
# singer.choose_animals_for_song(['fly'])
# singer.choose_animals_for_song(['fly', 'spider', 'bird', 'cat', 'dog', 'cow', 'horse', 'monkey'])
singer.choose_animals_for_song(
    ['perezoso', 'cucharacha', 'bb8', 'doraemon', 'marvinelmarciano', 'luisitocomunicia', 'messi', 'ibai'])
print(singer.sing())
