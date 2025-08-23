from flask import Blueprint, jsonify
from backend.models import Resource, Course

bp = Blueprint('btech1', __name__, url_prefix='/btech1')

# Get all resources for B.Tech Year 1
@bp.route('/resources', methods=['GET'])
def get_btech1_resources():
    # Assuming IT B.Tech courses
    courses = Course.query.filter_by(name='B.Tech', year=1).all()
    all_resources = []
    for course in courses:
        resources = Resource.query.filter_by(course_id=course.id).all()
        for res in resources:
            all_resources.append({
                "title": res.title,
                "type": res.type,
                "link": res.link,
                "semester": course.semester
            })
    return jsonify(all_resources)
