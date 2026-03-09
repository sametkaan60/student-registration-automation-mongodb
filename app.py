from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MongoDB Configuration
class MockTable:
    def __init__(self):
        self.data = [
            {"no": 101, "ad": "Örnek", "soyad": "Öğrenci"},
            {"no": 102, "ad": "Modern", "soyad": "Arayüz"}
        ]
    def find(self, query=None, projection=None):
        return self.data if not query else [item for item in self.data if all(item.get(k) == v for k, v in query.items())]
    def find_one(self, query, projection=None):
        res = self.find(query)
        return res[0] if res else None
    def insert_one(self, doc):
        self.data.append(doc)
    def delete_one(self, query):
        initial_len = len(self.data)
        self.data = [item for item in self.data if not all(item.get(k) == v for k, v in query.items())]
        class Result: 
            def __init__(self, count): self.deleted_count = count
        return Result(initial_len - len(self.data))

try:
    client = MongoClient(host='localhost', port=27017, serverSelectionTimeoutMS=2000)
    db = client['db_ogrenciler']
    table = db['ogrenci']
    client.admin.command('ping')
    print("Connected to MongoDB")
except Exception as e:
    print(f"MongoDB connection failed, using Mock Mode. Error: {e}")
    table = MockTable()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/students', methods=['GET'])
def get_students():
    students = list(table.find({}, {'_id': 0}))
    return jsonify(students)

@app.route('/api/students', methods=['POST'])
def add_student():
    data = request.json
    if not data or 'no' not in data or 'ad' not in data or 'soyad' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    try:
        # Check if student already exists
        if table.find_one({"no": int(data['no'])}):
             return jsonify({"error": "Student number already exists"}), 400
             
        table.insert_one({
            "no": int(data['no']),
            "ad": data['ad'],
            "soyad": data['soyad']
        })
        return jsonify({"message": "Student added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/students/bulk', methods=['DELETE'])
def delete_all_students():
    # For mock table support
    if hasattr(table, 'data'):
        count = len(table.data)
        table.data = []
        return jsonify({"message": f"All {count} students deleted successfully"}), 200
    
    result = table.delete_many({})
    return jsonify({"message": f"All {result.deleted_count} students deleted successfully"}), 200

@app.route('/api/students/<int:student_no>', methods=['DELETE'])
def delete_student(student_no):
    result = table.delete_one({"no": student_no})
    if result.deleted_count > 0:
        return jsonify({"message": "Student deleted successfully"}), 200
    else:
        return jsonify({"error": "Student not found"}), 404

@app.route('/api/students/search/<int:student_no>', methods=['GET'])
def search_student(student_no):
    student = table.find_one({"no": student_no}, {'_id': 0})
    if student:
        return jsonify(student), 200
    else:
        return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)
