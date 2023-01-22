my_list = []

my_list.append("Linda")

my_list.append("Bergsängel")

my_list.reverse()

my_list.clear()

my_list.append("Linda")

my_list.append("Bergsängel")

count = my_list.count("Kyckling")

element = my_list.pop()

my_list.append("Ludwig")
my_list.append("Luna")
my_list.append("Mollie")
my_list.sort(reverse=True)
print(my_list, count, element)

list2 = [1, 10, 43, 4, True, False]
list2.sort()
print(list2)

my_string = "Hej jag heter Linda"
print(my_string)
my_string_list = list(my_string)
print(my_string_list)

my_split_string = my_string.split('h')
print(my_split_string)

my_email = "test@testsson.se"
my_domain = my_email.split('@')[1].split('.')[0]
print(my_domain)

my_untrimmed_string = "     Linda     "
# print(my_untrimmed_string)
my_trimmed_String = my_untrimmed_string.strip()
print(my_trimmed_String)

letter_list = ["L", "I", "N", "D", "A"]

my_name = "".join(letter_list)
print(my_name)
