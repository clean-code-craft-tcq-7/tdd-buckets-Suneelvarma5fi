from detect_ranges_with_count import detect_ranges
from check_valid_input import check_valid
from print_reading_ranges import print_reading_ranges

assert(detect_ranges([3, 3, 5, 4, 10, 11, 12]) == [(3,5,4),(10,12,3)])
assert(detect_ranges([3, 3]) == [(3,3,2)])
assert(detect_ranges([4,5]) == [(4,5,2)]) #failing case

assert(check_valid("2,3,4,5,6,6,7,8") == True)
assert(check_valid([2,3,4,5,6,6,7,8]) == False)

assert(print_reading_ranges([(3,5,4),(10,12,3)]) == 'Range, Readings\n3-5, 4\n10-12, 3')
assert(print_reading_ranges([(3,3,2)]) == 'Range, Readings\n3-3, 4')