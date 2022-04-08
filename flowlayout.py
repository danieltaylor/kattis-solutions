max_width = int(input())
while max_width != 0:
	layout_width = 0
	layout_height = 0

	row_width = 0
	row_height = 0

	rect_width, rect_height = map(int, input().split())
	while rect_width != -1:
		if row_width + rect_width > max_width:
			# add current row
			layout_width = max(layout_width, row_width)
			layout_height += row_height
			# start new row
			row_width = rect_width
			row_height = rect_height
		else:
			# continue current row
			row_width += rect_width
			row_height = max(row_height, rect_height)
		# add final row
		rect_width, rect_height = map(int, input().split())
	layout_width = max(layout_width, row_width)
	layout_height += row_height
	print(layout_width, 'x', layout_height)

	max_width = int(input())
