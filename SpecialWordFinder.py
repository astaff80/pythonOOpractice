
import wordfinder as wf

class SpecialWordFinder(wf.WordFinder):

	def __init__(self, file):

		super().__init__(file)


	def parse(self, filename):
		""" """
		file = open(filename, "r")
		out = []
		line = file.readline()
		while line:
			if not (line.strip() == "" or line[0] == "#"):
				out.append(line.strip())
			line = file.readline()
		file.close()
		return out