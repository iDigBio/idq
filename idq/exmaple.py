from helpers import filled, field_to_flag

class Workflow:

    def __init__(self):
        self.required_fields = [
            "dwc:decimalLatitude",
            "dwc:decimalLongitude",
        ]
        self.outputs = self.required_fields
        self.flags = [
            field_to_flag(f,"error") for f in self.required_fields
        ] + [
            field_to_flag(f,"blank") for f in self.required_fields
        ]

    def process(self, d):
        if not "flags" in d:
            d["flags"] = []

        for f in self.required_fields:
            if filled(f,d):
                try:
                    d[f] = float(d[f])        
                except:
                    d[f] = None

                    d["flags"].append(field_to_flag(f,"error"))
            else:
                d["flags"].append(field_to_flag(f,"blank"))

        return d

def main():
    from harness import create_harness
    w = Workflow()
    app = create_harness(w)
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()        