#tuple - krotka
#róznica tuple a list () vs []
#tuple mozna tylko odczytywac READ ONLY

tax = (4, 5, 6, 7)
print(tax)
print(tax[2])

print(max(tax))

taxList = list(tax)
print(taxList)

tupleList = tuple(taxList)
print(tupleList)

(tax1, tax2, tax3, tax4) = tax
print(tax1,tax2,tax3,tax4)


