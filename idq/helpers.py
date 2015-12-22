def filled(f,d):
    return f in d and d[f] is not None and d[f] != ""

def field_to_flag(f,suffix):
    return "{0}_{1}".format(f.replace(":","_"),suffix)

def flag_to_field(f):
    return ":".join(f.split("_")[:-1])