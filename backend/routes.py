from flask import Blueprint, request, jsonify
from database import db
from models import Task
from flask_cors import CORS

main = Blueprint('main', __name__)
CORS(main)

@main.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([
        {
            'id': t.id,
            'name': t.name,
            'category': t.category,
            'description': t.description,
            'deadline': t.deadline,
            'priority': t.priority,
            'completed': t.completed
        } for t in tasks
    ])

@main.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    new_task = Task(
        name=data['name'],
        category=data.get('category'),
        description=data.get('description'),
        deadline=data.get('deadline'),
        priority=data.get('priority')
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added!"}), 201

@main.route('/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = True
        db.session.commit()
        return jsonify({"message": "Task completed!"})
    return jsonify({"message": "Task not found!"}), 404
