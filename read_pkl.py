import pickle
import pprint

filepath = input("Input the file you would like to read\nThe file should terminate in .pkl\n")
if ".pkl" not in filepath:
    raise ValueError("Filepath does not terminate in .pkl")

# f = open('dns_rem_100IPs_constraint_mapping_dict.pkl', 'rb')
# f = open('dns_rem_100IPs_constraint_identified_cycles_results.pkl', 'rb')
f = open(filepath, 'rb')
d = pickle.load(f)
pprint.pprint(d)
