def detect_ranges(samples):
    samples.sort()
    current_range = [samples[0], samples[0]]
    count = 1
    result = []
    for i in range(1, len(samples)):
        if samples[i] == current_range[1] or samples[i] == current_range[1] + 1:
            current_range[1] = samples[i]
            count += 1
        else:
        	result.append((current_range[0],current_range[1],count))
            current_range = [samples[i], samples[i]]
            count = 1
    result.append((current_range[0],current_range[1],count))
    return result