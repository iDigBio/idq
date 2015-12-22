"""
    This file contains an example workflow class. It can also be run to start a harness server for that workflow.
"""

from helpers import filled, field_to_flag, WorkflowBase

class Workflow(WorkflowBase):
    """
        An example of a possible data quality workflow class.

        This simple class just converts text numbers in the dwc:decimalLatitude and dwc:decimalLongitude
        fields to their numeric equivalents. It also sets flags if the the numbers are either blank, or there
        is a conversion error.
    """

    def __init__(self):
        super(Workflow,self).__init__()
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
        r = super(Workflow,self).process(d)

        for f in self.required_fields:
            if filled(f,d):
                try:
                    r[f] = float(d[f])
                except:
                    r[f] = None

                    r["flags"].append(field_to_flag(f,"error"))
            else:
                r["flags"].append(field_to_flag(f,"blank"))

        return r

def main():
    from harness import create_harness
    w = Workflow()
    app = create_harness(w)
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()        