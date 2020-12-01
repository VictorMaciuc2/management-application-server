from flask import Blueprint
from flask import jsonify, request

from controller.mapper import Mapper
from repository.skill_repository import SkillRepository
from service.feedback_service import FeedbackService

feedback_service = FeedbackService(None, None, SkillRepository())

feedback = Blueprint('feedback', __name__)
__report_sessions_path = '/feedback/sessions'
__skills_path = '/feedback/skills'


# Get la report sessions by userid
# Post la un report

@feedback.route(__skills_path, methods=['GET'])
def get_all_skills():
    return jsonify([Mapper.get_instance().skill_to_json(x) for x in feedback_service.getAllSkills()])
