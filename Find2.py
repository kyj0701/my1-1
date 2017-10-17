def __print_result():
	import os
	os.system('cat result.txt')

def find_all_count(filename,key):
	infile = open("article.txt", "r")
	outfile = open("result.txt", "w")
	text = infile.read()
	pos = text.find(key)
	count = 0
	if pos == -1:
		outfile.write(key + " is not found.\n")
		count = 0
		outfile.write(str(count))
	while not pos == -1:
		outfile.write(key + "is at" + str(pos) + ".\n")
		pos = text.find(key,pos+1)
		count += 1
	outfile.write(str(count))
	outfile.close()
	infile.close()
	print("done")

find_all_count("article,txt","컴퓨터")
__print_result()
find_all_count("article,txt","데스크탑")
__print_result()
find_all_count("article,txt","한양대")
__print_result()