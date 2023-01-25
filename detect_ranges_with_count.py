def generate_result(result,item):
	result.append(item)
	return result


def detect_ranges(samples):
    samples.sort()
    current_range,count,result = [samples[0], samples[0]],1,[]
    for i in range(1, len(samples)):
        if samples[i] == current_range[1] or samples[i] == current_range[1] + 1:
            current_range[1] = samples[i]
            count += 1
        else:
        	result = generate_result(result,(current_range[0],current_range[1],count))
        	current_range = [samples[i], samples[i]]
        	count = 1
    result = generate_result(result,(current_range[0],current_range[1],count))
    return result
