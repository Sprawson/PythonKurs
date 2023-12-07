"""--- Part Two ---
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?

"""

import re

f = open("input.txt", 'r')
input_file = f.read()


def find_map(title):
    int_map = []
    # regex to find map or seeds is (?<=title\n)(.+\n)+|(?<=title: ).+
    #                               part for maps  or part for seeds
    search_regex = "(?<=" + re.escape(title) + "\n)(.+\n)+|(?<=" + re.escape(title) + " ).+"
    map_str = re.search(search_regex, input_file).group().split("\n")
    while '' in map_str:
        map_str.remove('')
    for line in map_str:
        numbers = [int(x) for x in line.split(" ")]
        int_map.append(numbers)
    return int_map


def convert_values(values, ratio_map):
    converted_values = []
    for value in values:
        for ratio in ratio_map:
            if value in range(ratio[1], ratio[1] + ratio[2]):
                converted_value = value - ratio[1] + ratio[0]
                converted_values.append(converted_value)
                break
        else:
            converted_value = value
            converted_values.append(converted_value)
    return converted_values


seeds = find_map("seeds:")[0]
seed_to_soil_map = find_map("seed-to-soil map:")
soil_to_fertilizer_map = find_map("soil-to-fertilizer map:")
fertilizer_to_water_map = find_map("fertilizer-to-water map:")
water_to_light_map = find_map("water-to-light map:")
light_to_temperature_map = find_map("light-to-temperature map:")
temperature_to_humidity_map = find_map("temperature-to-humidity map:")
humidity_to_location_map = find_map("humidity-to-location map:")

conversion_maps = [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map,
                   light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map]
# convert seeds to seed ranges:
seed_ranges = [range(seeds[x],seeds[x] + 5000000) for x in range(0, len(seeds), 2)]
seed_ranges_lowest_locations = []
# convert seeds through all maps all the way to location
for seed_range in seed_ranges:
    seeds = list(seed_range)
    #print(seeds)
    for conversion_map in conversion_maps:
        seeds = convert_values(seeds, conversion_map)
    lowest_location_in_seed_range = min(seeds)
    print(f"{lowest_location_in_seed_range} in {seed_range}")
    seed_ranges_lowest_locations.append(lowest_location_in_seed_range)

# print lowest location value from all converted seed ranges
print(min(seed_ranges_lowest_locations))
