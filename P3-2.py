# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def remove_sign(s):
	if s[0] == '+':
		return s[1:]
	elif s[0] == '-':
		return s[1:]
	else:
		return s

def isfloat(s):
	(m,_,n) = s.partition(".")
	return (m.isdigit() and (n.isdigit() or n=="")) or m=="" and n.isdigit()

def get_float(message):
	s = input(message)
	while not (s.isdigit() or isfloat(s)):
		s = input(message)
	return float(s)

def get_fixed_signed(message):
	s = input(message)
	while not (isfloat(remove_sign(s))):
		s = input(message)
	return float(s)


print(get_fixed_signed("실수를 입력하시오"))