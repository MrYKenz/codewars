def song_decoder(song):
    song = song.split('WUB')
    original_song = []
    for word in song:
        if word != '':
            original_song.append(word)
    print(song)
    return ' '.join(original_song)

print(song_decoder("WUBWUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
