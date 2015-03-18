#file man demo
#loitd

f = open("main.cfg", "r")
print f.name, f.closed
for line in f:
	line = line.strip()
	if not line.startswith("#"):
		lsp = line.split("=")
		if len(lsp) == 2:
			print lsp
		#print line
f.close()
