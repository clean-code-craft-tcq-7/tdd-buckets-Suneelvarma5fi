def print_reading_ranges(result):
	if len(result) == 0: return False
	print("Range, Readings")
	for start, end, count in result:
		print(f"{start}-{end}, {count}")
	return True