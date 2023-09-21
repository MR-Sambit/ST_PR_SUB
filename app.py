from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['CYBER']  # Replace with your database name
collection = db['CYBER']       # Replace with your collection name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects', methods=['POST'])
def submit_project():
    # Retrieve form data
    student_name = request.form.get('studentName')
    print(student_name)
    project_title = request.form.get('projectTitle')
    project_description = request.form.get('projectDescription')
    project_file = request.files.get('projectFile')
    github_link = request.form.get('githubLink')

    # Save the project file to a specific location (you might want to modify this based on your needs)
    project_file.save(f'uploads/{project_file.filename}')

    # Create a document to be inserted into MongoDB
    project_data = {
        'student_name': student_name,
        'project_title': project_title,
        'project_description': project_description,
        'project_file_path': f'uploads/{project_file.filename}',
        'github_link': github_link if github_link else None
    }

    # Insert the data into the MongoDB collection
    collection.insert_one(project_data)

    return jsonify({'message': 'Project submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
