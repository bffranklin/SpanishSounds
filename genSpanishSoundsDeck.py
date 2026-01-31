import genanki
import csv

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
        this_audioURL=row[1]

# Download Audio
# Create Note

sounds_note=LetterNote(
    model=sounds_model,
    fields=['Letter','Audio']
)

sounds_deck=genanki.Deck(
    1718394039,
    'Sounds of Spanish'
)

genanki.Package(sounds_deck).write_to_file('spanishsounds.apkg')