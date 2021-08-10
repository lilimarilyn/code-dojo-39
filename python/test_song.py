import unittest

from song import Singer

ORIGINAL_SONG = """There was an old lady who swallowed a fly.
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

SONG_WITH_ONE_ANIMAL = """There was an old lady who swallowed a fly...
...She's dead, of course!"""

SONG_WITH_TWO_ANIMALS = """There was an old lady who swallowed a fly.
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a spider...
...She's dead, of course!"""


class TestSong(unittest.TestCase):
    def test_original_song(self):
        singer = Singer()
        singer.choose_animals_for_song([])
        self.assertEqual(singer.sing(), ORIGINAL_SONG)

    def test_just_one_animal_song(self):
        singer = Singer()
        singer.choose_animals_for_song(['fly'])
        self.assertEqual(singer.sing(), SONG_WITH_ONE_ANIMAL)

    def test_two_animals_song(self):
        singer = Singer()
        singer.choose_animals_for_song(['fly', 'spider'])
        self.assertEqual(singer.sing(), SONG_WITH_TWO_ANIMALS)


if __name__ == '__main__':
    unittest.main()
