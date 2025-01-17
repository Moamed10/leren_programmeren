def get_value(data: str, separator: str, position: int) -> str:
    splitted_strings = data.split(separator)
    if 0 <= position < len(splitted_strings):
        value = splitted_strings[position]
        return value
    else:
        return None

toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
separator = ','
position = 5  

result = get_value(toets_data, separator, position)
print(result)  # 

voetbalclup= "fey#barc#ajax#liverbool#sparta"
clup = get_value(voetbalclup , "#" , 9)
print (clup)

auto = "merc/ bmw/opel/ford"
de_auto = get_value(auto , "/" , 1)
print(de_auto)


# splitted_strings = toets_data.split(separator) # string splits itself into collection of strings
# if 0 <= position< len(splitted_strings):
#   value = splitted_strings[position] # read value at position of split_values
# else:
#   value = None
 
# print(value) # prints: Bram:6