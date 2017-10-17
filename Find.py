

def __print_result():
	import os
	os.system('cat result.txt')

def find_last(filename,key) : 
    infile = open(filename, "r") 
    outfile = open("result.txt", "w") 
    text = infile.read() 
    pos = text.rfind(key) 
    if pos == -1: 
        outfile.write(key + " is not found.\n") 
    else: 
        outfile.write(key + " is at " + str(pos) + ".\n") 
    outfile.close() 
    infile.close()
    print("done")

find_last("article,txt","컴퓨터")
__print_result()
find_last("article,txt","데스크탑")
__print_result()
find_last("article,txt","한양대")
__print_result()



def find_all(filename,key):
	infile = open(filename, "r")
	outfile = open("result.txt", "w")
	text = infile.read()
	pos = text.find(key)
	if pos == -1:
		outfile.write(key + " is not found.\n")
	while not pos == -1:
		outfile.write(key + "is at" + str(pos) + ".\n")
		pos = text.find(key,pos+1)
	outfile.close()
	infile.close()
	print("done")

find_all("article,txt","컴퓨터")
__print_result()
find_all("article,txt","데스크탑")
__print_result()
find_all("article,txt","한양대")
__print_result()


def find_all_count(filename,key):
	infile = open(filename, "r")
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


def one_sentence_per_line(filename):
	infile = open(filename,"r")
	outfile = open("result.txt","w")
	text = infile.read()
	count = 0
	while not text == "":
		pos = text.find(".")
		pos2 = text.find("?")
		if pos < pos2 or pos2 == -1:
			c,_,d = text.partition(".")
			outfile.write(c+"."+"\n")
			pos = text.find(".",pos+1)
			text = d
			count += 1
		elif pos2 < pos or pos == -1:
			c,_,d = text.partition("?")
			outfile.write(c+"?"+"\n")
			pos2 = text.find("?",pos2+1)
			text = d
			count += 1
	outfile.write("문장이 총 " + str(count) + "개\n")
	outfile.close()
	infile.close()
	print("done")

one_sentence_per_line("article.txt")
__print_result()



def find_all_sentence(filename,key):
	infile = open(filename, "r")
	outfile = open("result.txt", "w")
	text = infile.read()
	count = 0
	count2 = 0
	count_b = 0
	count_a = 0
	ts = "." or "?"
	while not text == "":
		(a,t,b) = text.partition(ts)
		pos = a.find(key)
		while not pos == -1:
			pos = a.find(key,pos+1)
			count += 1
			count2 += 1
			count_a = count
		if count_a != 0:
			outfile.write("'" + key + "'" + "이(가)" + str(count_a) + "번 등장")
			outfile.write(a + t + "\n")
			count_b += 1
		text = b
		count = 0
		count_a = 0
	outfile.write(key + "이(가)" + str(count_b) + "개 문장에서" + str(count2) + "번 등장")
	outfile.close()
	infile.close()
	print("done")

find_all_sentence("article.txt","컴퓨터")
__print_result()