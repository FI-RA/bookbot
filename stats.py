def get_num_words(text):
  list_words = text.split()
  len_words = len(list_words)
  return len_words

def get_num_characters(words):
  words_lower = words.lower()
  dict_char = {}
  for char_lower in words_lower:
    if char_lower not in dict_char:
      dict_char[char_lower] = 1
    else:
      dict_char[char_lower] += 1
  return dict_char

def sort_on(items):
    return items["num"]

def get_dictionary_to_sorted(dictionary):
  dict_sorted = {}
  list_new = []
  sorted_list = []
  for element_dictionary in dictionary:
    if list_new == []:
      dict_sorted["char"] = element_dictionary
      dict_sorted["num"] = dictionary[element_dictionary]
      list_new.append(dict_sorted)
    else:
      dict_sorted = {}
      dict_sorted["char"] = element_dictionary
      dict_sorted["num"] = dictionary[element_dictionary]
      list_new.append(dict_sorted)
  list_new.sort(reverse=True, key=sort_on)
  return list_new
