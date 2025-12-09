import music21 as m21
import matplotlib.pyplot as plt

omnesXML = m21.converter.parse("bach_omnes-generationes.mxl")

# for parts in omnesXML.parts:
#     print(parts.partName)

sopran_part = omnesXML.parts[0]
soprano_part_flattened = sopran_part.flatten()
soprano_notes = list(soprano_part_flattened.getElementsByClass(m21.note.Note))
sopran_intervals = []

for i in range(len(soprano_notes)-1):
	sopran_intervals.append(soprano_notes[i+1].pitch.midi - soprano_notes[i].pitch.midi)
	
pattern = [0, 0, 0, 0, -1] #ich weiß ja nicht
pattern2 = [0, 0, 0, 0, -2] #puh

def pattern_finder(scoreIntervals, patternIntervals):
	listFoundIndices = []
	for i in range(len(scoreIntervals)):
		if scoreIntervals[i : i+len(patternIntervals)] == patternIntervals:
			listFoundIndices.append(i)


	return listFoundIndices

patternsFoundIndecies = sorted(pattern_finder(sopran_intervals, pattern) + pattern_finder(sopran_intervals, pattern2))
print(patternsFoundIndecies)
patternsFoundOffset = []
for index in patternsFoundIndecies:
	patternsFoundOffset.append(soprano_notes[index].offset)
patternMeasures = [offset/4+1 for offset in patternsFoundOffset]
print(patternMeasures)

x = patternMeasures
y = ["Soprano 1"]*len(x)

plt.style.use("dark_background")

fick, ax = plt.subplots(figsize=(10,2.5))
ax.set_frame_on(False)
ax.scatter(x,y, c = "#6042DD", marker="|")
ax.set_xlabel("Measure", fontsize=10)

plt.show()

