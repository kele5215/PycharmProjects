import pickle
import pprint
import sys

data1 = {"a": [1, 2.0, 3, 4 + 6j],
         "b": ("string", u"Unicode string"),
         "c": None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open("data.pkl", "wb")

pickle.dump(data1, output)

pickle.dump(selfref_list, output)

output.close()

pkl_file = open("data.pkl", "rb")
data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()

# while True:
#     try:
#         x = int(input("lsdfjslfj: "))
#         break
#     except ValueError:
#         print("cuo wu tyr again")

try:
    f = open("tmp/foo.txt")
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:{0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error: ", sys.exc_info()[0])
    raise
