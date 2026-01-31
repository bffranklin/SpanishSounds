import genanki
import csv
from pytube import YouTube
import ffmpeg

sounds_deck=genanki.Deck(
    1718394039,
    'Sounds of Spanish'
)

sounds_model =genanki.Model(
    1395113399, # python3 -c "import random; print(random.randrange(1 << 30, 1 << 31))"
    'Sounds Model',
    fields = [
        {'name': 'Letter'},
        {'name': 'Audio'},
    ],
    templates=[
        {
            'name': 'Letter to Sound',
            'qfmt': '{{Letter}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Audio}}'
        },
    ]
)

class LetterNote(genanki.Note):
  @property
  def guid(self):
    return genanki.guid_for(self.fields[0])

# Open the CSV file
with open('mapping.csv', 'r') as mapping_file:
    reader = csv.reader(mapping_file)
    
    # Iterate through the rows
    for row in reader:
        this_letter=row[0]
        # Download Audio
        yt=YouTube(row[1])
        stream_url=yt.streams.all()[0].url
        audio, err=(
           ffmpeg
           .input(stream_url)
           .output(this_letter + ".mp3", acodec="mp3")
           .run()
        )
        # Create Note
        sounds_note=LetterNote(
            model=sounds_model,
            fields=[this_letter,this_letter + ".mp3"]
        )
        sounds_deck.add_note(sounds_note)

genanki.Package(sounds_deck).write_to_file('spanishsounds.apkg')