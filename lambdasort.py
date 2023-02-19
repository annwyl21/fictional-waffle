# Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# Country = Country, Population, Capital, Population of capital, Continent, Established, Currency, Religion, Official Languages
print()
countries = []
for line in open ('country.txt'):
    countries.append(line.split(','))

print("Population Statistics\n")

countries.sort(reverse=True, key=lambda c: int(c[3]))
# sorting into size order, smallest population first until reversed
# for each list(c) in the collection of lists called countries, convert the 4th item in list c into an integer and use it as a key to sort all the lists into decreasing order based on that number

header = ["Country", "Population (m)", "Capital", "Cap. City Pop.", "% Pop. in Capital", "Official Languages"]
for item in header:
    print(f"|{item:<18s}", end='')
for line in countries:
    elements = line[0].split(' = ') # spliting the string in the first element to isolate the country name
    x = 100/int(line[1])*int(line[3]) # finding out the percentage of the population that live in the capital city
    last_item = line[10].replace("'\n", '') # removing the '\n' from the end of each line
    print(f"\n|{elements[0]:<18}|{int(line[1])/1000000:<18.1f}|{line[2]:<18}|{int(line[3]):18,}|{x:18.1f}|{line[-3]}, {line[-2]}, {last_item}", end='')
# using the thousands specifier

#for line in countries:
    #print(','.join(line), end='')

print()
print()
print("Countries in order of date established\n")
countries.sort(key=lambda c: int(c[5]))
for data in countries:
    elements = data[0].split(' = ')
    print(f"{elements[0]:10}: Established {data[5]}")
print()
