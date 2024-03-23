from flask import *
from gsheets import Sheets

app = Flask(__name__)


sheets_base_url = f"https://docs.google.com/spreadsheets/d/"

sheets = Sheets.from_files('client_secrets.json', 'storage.json')

def get_sheet(id, sheet_id=0): 
    url = sheets_base_url + id
    s = sheets.get(url)
    return s.sheets[sheet_id]

@app.route('/')
def slash():
    # attribute of id
    id_ = request.args.get('id')
    sheet_id = request.args.get('sheet_id', 0)
    if not id_:
        return 'No id provided'
    s = get_sheet(id_, sheet_id=int(sheet_id))
    print(sheet_id)
    print(id_)
    return s.values()


@app.route('/rf')
def rf():
    id_ = request.args.get('id')
    sheet_id = request.args.get('sheet_id', 0)
    if not id_:
        return 'No id provided'
    s = get_sheet(id_, sheet_id=int(sheet_id))
    return s.values()


@app.route('/cf')
def cf():
    id_ = request.args.get('id')
    sheet_id = request.args.get('sheet_id', 0)
    if not id_:
        return 'No id provided'
    s = get_sheet(id_, sheet_id=int(sheet_id))
    return s.values(column_major=True)

@app.route("/r/<index>")
def r(index):
    id_ = request.args.get('id')
    sheet_id = request.args.get('sheet_id', 0)
    if not id_:
        return 'No id provided'
    s = get_sheet(id_, sheet_id=int(sheet_id))
    try:
        return s.values()[int(index)]
    except IndexError:
        return 'Index out of range'

@app.route("/c/<index>")
def c(index):
    id_ = request.args.get('id')
    sheet_id = request.args.get('sheet_id', 0)
    if not id_:
        return 'No id provided'
    s = get_sheet(id_, sheet_id=int(sheet_id))
    try:
        return s.values(column_major=True)[int(index)]
    except IndexError:
        return 'Index out of range'
    
app.run(host="0.0.0.0", port=54321)