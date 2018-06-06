import re

# file = open('/media/warrior/Ubuntu/corp_workspace/data_gen/dev/text.txt','r')
# text = file.read()
# text = re.sub('[A-Za-z0-9]', '', text)

in_file = open('/media/warrior/Ubuntu/corp_workspace/data_gen/dev/text_out.txt','r')
lines = in_file.readlines()
# print('lines', lines)
out_lines = []
for line in lines:
	# print(line)
	leng = len(line)
	coef = 40
	if leng>coef:
		n_lines = leng // coef
		for j in range(n_lines):
			# print('subline',line[j*45:(j+1)*45])
			out_lines.append(line[j*coef:(j+1)*coef]+'\n')
		out_lines.append(line[(n_lines)*coef:leng])
	else:
		out_lines.append(line)

out_file = open('/media/warrior/Ubuntu/corp_workspace/data_gen/dev/text_out_2.txt','w+')
out_file.writelines(out_lines)