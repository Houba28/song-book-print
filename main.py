

import sys


def convert(path):
	line_content = ""
	head = "<html><head><script>function printDiv(divName) {var printContents = document.getElementById(divName).innerHTML;var originalContents = document.body.innerHTML;     document.body.innerHTML = printContents;     window.print();document.body.innerHTML = originalContents;}</script><style>sup {color:red; font-weight: bold;} body {font-family: 'Arial';line-height: 150%} #header { font-size: 150%; line-height: 110%} #author{font-size: 100%; line-height: 400%}</style></head><body>"
	final = ''
	footer = "</body></html>"
	with open(fname, "r", encoding="utf8") as f:
		i = 0
		for line in f.readlines():
			if i ==0:
				chords = line.split()
				#print(chords)
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
	if len(sys.argv) <2:
		sys.exit("You did not entered the filename for conversion!")
		
	for fname in sys.argv:
		if fname != __file__:
			content = convert(fname)
			htmlsave(fname,content)