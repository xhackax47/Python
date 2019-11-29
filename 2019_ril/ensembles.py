tab = ["A", "B", "" or None]
if all(tab):
    print("Ok (all)")
else:
    print("Not OK (all)")
print("Ok (any)" if any(tab) else "Not Ok (any)")