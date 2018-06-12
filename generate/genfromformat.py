import random as rd
import itertools

def format2string():
	file = open('../dev/datetime_format.txt','r')
	lines = file.readlines()
	# J = range(2)
	# M = range(10)
	# N = range(2)
	# C = range(4)
	# D = range(10)
	# Y = range(10)

	O = (list(range(1,10)),'O')
	M = (list(range(1,10)),'M')
	L = (list(range(1930,2030)),'L')
	I = (list(range(1,13)),'I')
	D = (list(range(1,10)),'D')
	P = (list(range(1,31)), 'P')
	Q = (list(range(1,10)),'Q')
	Y = (list(range(10)),'Y')
	A = (list(range(10)), 'A')

	# out_file = open('../dev/datetime_text.txt', 'r+')
	sample_file = open('../dev/datetime_text_sample.txt', 'w+')
	total_sample = 0
	out_lines = []
	print('len', len(lines))
	show_lines = []
	for line in lines:
		ls_sign = []
		combination = []
		print('line', line)
		'''each character correspond to a sign'''
		for char in line:
			if char == 'M':
				ls_sign.append(M)
				combination.append(M[0])
			if char == 'D':
				ls_sign.append(D)
				combination.append(D[0])
			if char == 'Y':
				ls_sign.append(Y)
				combination.append(Y[0])
			if char == 'O':
				ls_sign.append(O)
				combination.append(O[0])
			if char == 'L':
				ls_sign.append(L)
				combination.append(L[0])
			if char == 'I':
				ls_sign.append(I)
				combination.append(I[0])
			if char == 'P':
				ls_sign.append(P)
				combination.append(P[0])
			if char == 'Q':
				ls_sign.append(Q)
				combination.append(Q[0])
			if char == 'A':
				ls_sign.append(A)
				combination.append(A[0])

		#ls_sign:'YMND'

		# print('combin', combination)
		'''numeric combination'''
		tp_signs = list(itertools.product(*combination))
		print('lssign',[sign[1] for sign in ls_sign])
		print('tp sign', len(tp_signs))
		print(tp_signs[0])
		total_sample+= len(tp_signs)
		leng_sign= len(ls_sign)
		for cb in [tp_signs[0]]:
			'''len(cb)=len(sign)'''
			# print('cb',cb)
			org_line = line
			#replace all sign occurences
			for i in range(leng_sign):
				'''replace all character'''
				org_line= org_line.replace(ls_sign[i][1],(str(cb[i])))
			# out_lines.append(org_line)
			# out_file.write(org_line+'\n')
			print('line', org_line)
			# out_lines.append(org_line)
			sample_file.write(org_line + '\n')
	# out_file.close()
	print('total_sample', total_sample)


if __name__ == '__main__':
	format2string()