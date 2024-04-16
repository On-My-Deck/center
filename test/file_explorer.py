import file_explorer
import audio_play

files=file_explorer.list_files("/ESP")
# print(files)
print(audio_play.play("/ESP/BIZARRAP.MP3"))
# audio_play.set_volume(20)
# audio_play.pause()
# audio_play.resume()
# print(file_explorer.list())
# print(file_explorer.change_dir("/ESP"))
# print(file_explorer.list())
# print(file_explorer.cwd())
# print(file_explorer.exit_dir())
