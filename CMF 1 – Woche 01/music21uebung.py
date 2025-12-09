import music21 as m21
# Importieren der MusicXML-Datei "Aufgabe 03_MusicXML.musicxml" als "music21-Score" mithilfe der Methode ".converter.parse"
aufgabe04_musicxml = m21.converter.parse("Aufgabe 04_Eine-MusicXML-Datei.musicxml")

# Anzeige des "music21-Scores" "aufgabe03_musicxml" als Partitur mithilfe der Methode ".show()"
aufgabe04_musicxml.show()
