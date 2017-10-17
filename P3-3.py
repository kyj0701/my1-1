# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def get_number():
	return input("수를 입력하세요.\n")

def print_result(srm,res):
	print(srm,"의 제곱근은",res,"입니다.")


def isfloat(s):
	(m,_,n) = s.partition(".")
	return m.isdigit() and (n.isdigit() or n=="") or \
				 m == "" and n.isdigit()
	
	
def stop():
	cont = input('계속하시겠습니까? (y/n)')
	while not (cont == 'y' or cont == 'n'):
		cont = input('계속하시겠습니까? (y/n)')
	return cont == 'n'

def safe_sqrt():
	import math
	print("제곱근을 구해드립니다.")
	print("0이상의 수를 입력하세요.")
	
	while True:
		srm = get_number()
		while not isfloat(srm):
			srm = get_number()
		res = math.sqrt(float(srm))
		print_result(srm,round(res,4))
		if stop():
			break
	print("안녕히 가세요.")

safe_sqrt()