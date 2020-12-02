class FeedbackService:
    def __init__(self, report_repo, report_session_repo, skills_repo, project_service):
        self.__report_repo = report_repo
        self.__report_session_repo = report_session_repo
        self.__skills_repo = skills_repo
        self.__project_service = project_service

    def getAllSkills(self):
        return self.__skills_repo.getAll()

    def getAllReportSessions(self):
        return self.__report_session_repo.getAll()

    def getAllReportSessionsForUser(self, userId):
        return self.__report_session_repo.getAllForUser(userId)

    def getAllReportSessionsForProject(self, projectId):
        rs = self.__report_session_repo.getAllForProject(projectId)

        dictionar = {}
        for x in rs:
            tup = (x.get_project_id(), x.get_start_date(), x.get_end_date())
            if tup not in dictionar:
                dictionar[tup] = (0, 1)
            else:
                dictionar[tup][1] += 1
            if x.get_was_completed() is True:
                dictionar[tup][0] += 1

        out = []
        for key in dictionar.keys():
            out.append({'projectId': key[0], 'start_date': key[1], 'end_date': key[2], 'completed': dictionar[key][0],
                        'total': dictionar[key][1]})
        return out

    def addReportSessions(self, projectId, startDate, endDate):
        from domain.report_session import ReportSession
        count = 0
        for user in self.__project_service.getUsersForProject(projectId):
            self.__report_session_repo.add(ReportSession(0, projectId, user.get_id(), startDate, endDate, False))
            count += 1
        return count

    def removeReportSessions(self, projectId, startDate, endDate):
        sessions = self.__report_session_repo.getAllForProject(projectId)
        count = 0
        for x in sessions:
            if x.get_start_date() == startDate and x.get_end_date() == endDate and x.get_was_completed() is False:
                self.__report_session_repo.remove(x)
                count += 1
        return count

    def addReports(self, sessionId, report):
        pass

    # Apelata doar manual
    def populateSkills(self):
        from domain.skill import Skill
        self.__skills_repo.add(Skill(1, 'Completes the work thoroughly and with care'))
        self.__skills_repo.add(Skill(2, 'Understands the assigned role and responsibilities'))
        self.__skills_repo.add(Skill(3, 'Delivers consistently to agreed time-frames and specifications'))
        self.__skills_repo.add(Skill(4, 'Communicates in a professional and responsive manner'))
        self.__skills_repo.add(Skill(5, 'Is motivated by the work he/she is doing'))
        self.__skills_repo.add(Skill(6, 'Is adaptable to new types of assignments'))
        self.__skills_repo.add(Skill(7, 'How would you rate overall performance?'))
        self.__skills_repo.add(Skill(8, 'How would you rate employee Work From Home(WFH) performance?'))
