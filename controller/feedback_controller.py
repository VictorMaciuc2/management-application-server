from flask import Blueprint
from flask import jsonify, request

from controller.mapper import Mapper
from repository.report_repository import ReportRepository
from repository.report_session_repository import ReportSessionRepository
from repository.skill_repository import SkillRepository
from service.feedback_service import FeedbackService

feedback_service = FeedbackService(ReportRepository(), ReportSessionRepository(), SkillRepository())

feedback = Blueprint('feedback', __name__)
__base_path = '/feedback'
__report_sessions_path = __base_path + '/sessions'
__skills_path = __base_path + '/skills'


@feedback.route(__skills_path, methods=['GET'])
def get_all_skills():
    return jsonify([Mapper.get_instance().skill_to_json(x) for x in feedback_service.getAllSkills()])


@feedback.route(__report_sessions_path, methods=['GET'])
def get_report_sessions():
    user_id = request.args.get('userid')
    project_id = request.args.get('projectid')
    if user_id is None and project_id is None:
        return jsonify(
            [Mapper.get_instance().report_session_to_json(x) for x in feedback_service.getAllReportSessions()])

    if user_id is not None:
        return jsonify([Mapper.get_instance().report_session_to_json(x) for x in
                        feedback_service.getAllReportSessionsForUser(user_id)])

    if project_id is not None:
        return jsonify(feedback_service.getAllReportSessionsForProject(project_id))


@feedback.route(__report_sessions_path, methods=['POST'])
def add_report_sessions():
    project_id = request.json['project_id']
    start_date = Mapper.get_instance().json_to_date_time(request.json['start_date'])
    end_date = Mapper.get_instance().json_to_date_time(request.json['end_date'])
    count = feedback_service.addReportSession(project_id, start_date, end_date)
    return jsonify(added=count)


# Va sterge doar report session-urile necompletate
@feedback.route(__report_sessions_path, methods=['DELETE'])
def delete_report_sessions():
    project_id = request.args.get('projectid')
    start_date = Mapper.get_instance().json_to_date_time(request.args.get('startdate'))
    end_date = Mapper.get_instance().json_to_date_time(request.args.get('enddate'))
    count = feedback_service.removeReportSessions(project_id, start_date, end_date)
    return jsonify(removed=count)


@feedback.route(__base_path, methods=['POST'])
def add_reports():
    report_session_id = request.args.get('sessionid')
    count = 0
    for report in Mapper.get_instance().json_to_reports(request.json):
        try:
            feedback_service.addReport(report_session_id, report)
            count += 1
        except ValueError:
            continue
    return jsonify(added=count)
