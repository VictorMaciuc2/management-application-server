class FeedbackService:
    def __init__(self, report_repo, report_session_repo, skills_repo):
        self.__report_repo = report_repo
        self.__report_session_repo = report_session_repo
        self.__skills_repo = skills_repo

    def getAllSkills(self):
        return self.__skills_repo.getAll()

    def getAllReportSessions(self):
        pass  # TODO

    def getAllReportSessionsForUser(self, userId):
        pass

    def getAllReportSessionsForProject(self, userId):
        pass

    def addReportSession(self, reportSession):
        pass

    def removeReportSessions(self, projectId, startDate, endDate):
        pass  # Returns int

    def addReport(self, sessionId, report):
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
