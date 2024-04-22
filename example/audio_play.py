import audio_play


if __name__ == '__main__':
    # full path
    audio_play.play("/ESP/LOOK.MP3")

    audio_play.pause()
    audio_play.resume()

    # voluem：0～100
    audio_play.set_volume(20)