
import json
import itertools

def group(to_group, keys):  # function takes two arguments: a dict to_group and a list keys of fields to group by
    for i in range(len(keys)):
        func = lambda x: (x[keys[i]])
        grouped = itertools.groupby(to_group, key=func)

        r_dict = dict()
        for k, v in grouped:
                r_dict.update({k: list(v)})
        return r_dict 



#ref: 
# https://medium.com/swlh/grouping-list-of-dictionaries-by-specific-key-s-in-python-61edafbbc0ed
# https://www.pythonpool.com/pythons-itertools-groupby/
# https://www.saltycrane.com/blog/2014/10/example-using-groupby-and-defaultdict-do-same-task/
# https://www.geeksforgeeks.org/itertools-groupby-in-python/





# Initial working variant

# def group(d, keys):
# 
#     if len(keys) == 1:
#         func = lambda x: (x[keys[0]])
# 
#         grouped_d = itertools.groupby(sorted(d, key=func), func)
# 
#         new_d = {}
#         for k,v in grouped_d:
#             new_d[k] = list(v)
# 
#     if len(keys) > 1:
#         func = lambda x: (x[keys[0]], x[keys[1]], x[keys[2]])
# 
#         grouped_d = itertools.groupby(sorted(d, key=func), func)
# 
#         new_d = {}
#         for (k,l,o),v in grouped_d:
#             m = f'{k},{l},{o}'
#             new_d[m] = list(v)
# 
#     print(json.dumps(new_d, indent=2))
# 







