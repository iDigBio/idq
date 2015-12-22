from flask import Flask, render_template, flash, request, jsonify
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from flask_wtf import Form
from flask_wtf.file import FileField, FileRequired
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required, Email
import json
import unicodecsv
import random

def create_harness(w):
    app = Flask(__name__)
    app.secret_key = "idq_harness"
    Bootstrap(app)

    nav = Nav()

    nav.register_element('top', Navbar(
        View('iDigQuality','home'),
        View('Batch','batch'),
        View('Single','single'),
        View('API Documentation','apidocs'),
    ))

    nav.init_app(app)

    class SingleForm(Form):        
        pass

    for f in w.required_fields:
        f_name = f.replace(":","_")
        setattr(SingleForm,f_name,StringField(f))

    setattr(SingleForm,"submit",SubmitField(u'Process'))

    class BatchForm(Form):
        csv = FileField("CSV File (UTF-8 Required)", validators=[
            FileRequired()
        ])

        submit = SubmitField("Process")


    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route('/apidocs')
    def apidocs():
        numbers = [random.randint(0,99)/10.0 for f in w.required_fields+w.required_fields]
        return render_template("apidocs.html", numbers=numbers, req_fields=w.required_fields, output_fields=w.outputs, flags=w.flags)        

    @app.route('/batch', methods=('GET','POST'))
    def batch():
        form = BatchForm(csrf_enabled=False)
        output = None
        use_json = False

        if request.method == "POST":
            j = request.get_json()
            if j is None:
                if form.validate_on_submit():
                    output = []
                    r = unicodecsv.DictReader(form.csv.data)
                    for l in r:
                        output.append(w.process(l))
                else:
                    flash("CSV File Required.")
            else:
                output = []
                for d in j["items"]:
                    output.append(w.process(d))
                use_json = True

        if use_json:
            return jsonify({"items": output })
        else:
            return render_template("batch.html", form=form, req_fields=w.required_fields, output=json.dumps(output, indent=2).strip())

    @app.route('/single', methods=('GET','POST'))
    def single():
        form = SingleForm(csrf_enabled=False)
        output = None
        use_json = False

        if request.method == "POST":
            d = request.get_json()
            if d is None:
                d = {}
                for f in form._fields:
                    f_dict_name = f.replace("_",":")
                    if f_dict_name in w.required_fields:
                        d[f_dict_name] = form._fields[f].data
            else:
                use_json = True

            output = w.process(d)

        if use_json:
            return jsonify(output)
        else:
            return render_template("single.html", form=form, output=json.dumps(output, indent=2).strip())

    return app