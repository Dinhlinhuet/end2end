import random as rd
import itertools

def format2string():
	file = open('../dev/datetime_format_v2.txt','r')
	lines = file.readlines()

	O = (list(range(1,10)),'O')
	M = (list(range(1,10)),'M')
	L = (list(range(1930,2030)),'L')
	I = (list(range(1,13)),'I')
	D = (list(range(1,10)),'D')
	P = (list(range(1,31)), 'P')
	Q = (list(range(1,10)),'Q')
	Y = (list(range(10)),'Y')
	A = (list(range(10)), 'A')
	B = (list(range(3)),'B')

	out_file = open('../dev/datetime_text_v2.txt', 'w')
	annotation_file = open('../dev/annotation.txt', 'w')
	# sample_file = open('../dev/datetime_text_sample.txt', 'w+')
	total_sample = 0
	out_lines = []
	print('len', len(lines))
	j=0
	for line in lines:
		line = line.strip()
		ls_sign = []
		combination = []
		print('line', line, len(line))
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
			if char == 'B':
				ls_sign.append(B)
				combination.append(B[0])

		# print('combin', combination)
		'''numeric combination'''
		tp_signs = list(itertools.product(*combination))
		print('lssign',[sign[1] for sign in ls_sign])
		print('tp sign', len(tp_signs))
		print(tp_signs[0])
		total_sample+= len(tp_signs)
		leng_sign= len(ls_sign)
		'''toshow'''
		# for cb in [tp_signs[0]]:
		'''to full'''
		for cb in tp_signs:
			'''len(cb)=len(sign)'''
			# print('cb',cb)
			org_line = line
			#replace all sign occurences
			for i in range(leng_sign):
				'''replace all character'''
				org_line= org_line.replace(ls_sign[i][1],(str(cb[i])))
			out_lines.append(org_line)
			out_file.write(org_line+'\n')
			prefix_file = org_line
			if '/' in prefix_file: prefix_file = prefix_file.replace('/','s')
			textline= '%07d_%s.png %s\n'%(j,prefix_file, org_line)
			annotation_file.writelines(textline)
			# print('line', org_line)
			out_lines.append(org_line)
			j+=1
			# sample_file.write(org_line + '\n')
	out_file.close()
	annotation_file.close()
	print('total_sample', total_sample)


if __name__ == '__main__':
	format2string()