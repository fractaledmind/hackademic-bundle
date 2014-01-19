t = '- item 1\n\t- sub-item 1\n\t\t- sub-sub-item 1\n\t\t\t- sub-sub-sub-item 1\n\t\t- sub-sub-item 2\n\t- sub-item 2\n- item 2'

# replace tabs with 'x's
nt = t.replace('\t', 'x')

# create list from string
l = nt.split('\n')

# split list into list of prefixes and list of text
pre_l = []
text_l = []
for i in l:
	w = i.split(' ')
	pre = w[0]
	pre_l.append(pre)
	te = w[1:]
	text = ' '.join(te)
	text_l.append(text)

# prepare for numerical conversion
pre_l[0] = '1'

# convert prefixes to numbers
for i, item in enumerate(pre_l[:-1]):
	x = len(pre_l[i])
	y = len(pre_l[i + 1])
	# if x < y, then [i + 1] is child of [i]
	if x < y:
		num = int(pre_l[i])
		new = (num * 10) + 1
		new = str(new)
		pre_l[i + 1] = new
	# if x = y, then [i] and [i + 1] are siblings
	elif x == y:
		num = int(pre_l[i])
		new = (num + 1)
		new = str(new)
		pre_l[i + 1] = new
	# if x > y, then [i + 1] is sibling of some preceeding item
	elif x > y:
		rev = pre_l[::-1]
		r_in = (len(pre_l) - (i + 1))
		rev = rev[r_in:]
		for j, rev_item in enumerate(rev):
			if len(rev[j]) == y:
				pos = pre_l.index(rev[j])
				num = int(pre_l[pos])
				new = (num + 1)
				new = str(new)
				pre_l[i + 1] = new

# insert periods between multiple digit numbers
new_l = []
for t in pre_l:
	z = '.'.join([t[i:i+1] for i in range(0, len(t), 1)])
	new_l.append(z)


# add period after single digit items
l = []
for i, item in enumerate(new_l):
	if len(item) == 1:
		l.append(item)
		l.append('.')
		s = ''.join(l)
		new_l[i] = s
		l = []	

# add tabs back to list
for i, item in enumerate(new_l):
	if len(new_l[i]) == 3:
		new_l[i] = '\t' + item
	elif len(new_l[i]) == 5:
		new_l[i] = '\t\t' + item
	elif len(new_l[i]) == 7:
		new_l[i] = '\t\t\t' + item
	elif len(new_l[i]) == 9:
		new_l[i] = '\t\t\t\t' + item
	elif len(new_l[i]) == 11:
		new_l[i] = '\t\t\t\t\t' + item

#interlace prefix list and text list 
grouped_l = zip(new_l, text_l) 

# convert final list into string
for i in grouped_l:
	x = ' '.join(i)
	print x






	