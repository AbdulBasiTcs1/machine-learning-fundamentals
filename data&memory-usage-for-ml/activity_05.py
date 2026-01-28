# Dictionaries in Python works as a key value pairs and always get accessed using
# the key:value form , Like hashing in other languages in python the hashs are actually the kkeys and that's how these are accessed actually.

capitals={ 'USA':'Washingtion D.C.',
          'India':'New Delhi',
          'China' : 'Beijing',
          'Pakistan' : 'Islamabad'
          }
print("The dictionaries of the captitals of the countaries : ")
print(capitals)
print(capitals['China'])
print(capitals.get(1))
print(capitals)