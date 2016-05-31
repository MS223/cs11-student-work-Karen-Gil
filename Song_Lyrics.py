class Song(object):

    def __init__(self, lyrics,title,artist):
        self.lyrics = lyrics
        self.artist= artist
        self.title= title

    def sing_me_a_song(self):
        print self.title
        print self.artist
        for line in self.lyrics:
            print line


happy_bday = Song(["Happy birthday to you",
                   "These lyrics are copyrighted",
                   "So I'll stop here"],"Happy Birthday","Who Knows")


hotline_bling = Song(["You used to call me on my",
                      "You used to, you used to",
                      "Yeah",],"Hotline Bling", "Drake")
# This is your daily reminder that Drake is Canadian

happy_bday.sing_me_a_song()
hotline_bling.sing_me_a_song()
