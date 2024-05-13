from sklearn import datasets

#try fetching records from all 3 methods , csv , excel and digits
digits = datasets.load_digits()
print("\ndata",digits.data)
print("\n\n Target ",digits.target)
print("\n\n Digit Images",digits.images[0])
print("\n\n Targe Names",digits.target_names)
print("\n\n Feature Names",digits.feature_names)
print("\n\n DESCR",digits.DESCR)

