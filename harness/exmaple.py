def filled(f,d):
    return f in d and d[f] is not None and d[f] != ""

class Workflow:

    def __init__(self):
        self.required_fields = [
            "dwc:decimalLatitude",
            "dwc:decimalLongitude",
        ]
        self.outputs = self.required_fields
        self.flags = [
            "{0}_error".format(f.replace(":","_")) for f in self.required_fields
        ] + [
            "{0}_blank".format(f.replace(":","_")) for f in self.required_fields
        ]

    def process(self, d):
        if not "flags" in d:
            d["flags"] = []

        for f in self.required_fields:
            flag_prefix = f.replace(":","_")
            if filled(f,d):
                try:
                    d[f] = float(d[f])        
                except:
                    d[f] = None

                    d["flags"].append(flag_prefix + "_error")
            else:
                d["flags"].append(flag_prefix + "_blank")

        return d