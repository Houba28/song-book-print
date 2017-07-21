# -*- coding: <UTF-8> -*-

import sys
import os.path

def convert(path):
	line_content = ""
	head = "<html><head><style>sup {color:blue; font-weight: bold;} body {font-family: 'Arial';line-height: 150%} #header { font-size: 150%; line-height: 110%} #author{font-size: 100%; line-height: 400%}</style></head><body>"
	final = ''
	footer = "</body></html>"
	with open(path, "r", encoding="utf8") as f:
		i = 0
		for line in f.readlines():
			if i ==0:
				chords = line.split()
				chords[0] = chords[0][1:]
			elif i ==1:
				#nadpis
				final = final + "<div id=header>" + line + "</div>"
			elif i == 2:
				#autor
				final = final + "<div id=author><i>" + line + "</i></div>"
			elif i == 3:
				final = final + "<i>" + line + "</i>"
			else:
				words = line.split()
				for word in words:
					if word in chords:
						final = final + "<sup>"+str(word)+"</sup> "
					else:
						final= final + str(word) + " "
				final = final + "<br>\n"
			i+=1
	return head + final + footer

def htmlsave(name, cont):
	with open(name[:-4]+".html", "w") as f:
		f.write(cont)


if __name__ == "__main__":
	if len(sys.argv) > 1:
		if sys.argv[1] in ["help", "h", "?"]:
			#usage help
			sys.exit("for single file run with argument with path or a filename, else will search for all txt files")
	if len(sys.argv) == 1:
		print("Searching for all .txt files in this directory")
		path = os.getcwd()
		print(path)
		files = [f for f in os.listdir(path) if os.path.isfile(f)]
		for file in files:
			if file[-3:] != "txt":
				files.remove(file)
	else:
		files = [sys.argv[1]]
		if files[0][-4:] != ".txt":
			a = input("Bad file extension. Press any key to exit")
			sys.exit()

	for file in files:
		if file[-4:] == ".txt":
			print("converting: " + file)
			content = convert(file)
			htmlsave(file,content)
			print("saved")
	#a = input("Finished. Press any key to exit")
	sys.exit()