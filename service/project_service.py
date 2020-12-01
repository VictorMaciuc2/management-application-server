class ProjectService:
    def __init__(self, __repo, project_technology_repo, user_project_repo, technology_service, client_service):
        self.__project_repo = __repo
        self.__project_tech_repo = project_technology_repo
        self.__user_project_repo = user_project_repo
        self.__tech_service = technology_service
        self.__client_service = client_service

    def getAllProjects(self):
        return self.__project_repo.getAll()

    def getOneProject(self, id):
        project = self.__project_repo.getOne(id)
        if project is None:
            raise ValueError("The project with the given ID does not exist.")
        return project

    def addProject(self, project):
        p = self.__project_repo.getOne(project.get_id())
        if p is not None:
            raise ValueError("A project with the given ID already exists.")
        self.__client_service.getOne(project.get_client_id())  # Throws ValueError if client does not exist
        return self.__project_repo.add(project)

    def removeProject(self, id):
        project = self.__project_repo.getOne(id)
        if project is None:
            raise ValueError("The project with the given ID does not exist.")
        self.__project_repo.remove(project)

    def updateProject(self, project):
        p = self.__project_repo.getOne(project.get_id())
        if p is None:
            raise ValueError("The project with the given ID does not exist.")
        if p.get_client_id() != project.get_client_id():
            self.__client_service.getOne(project.get_client_id())  # Throws ValueError if client does not exist
        return self.__project_repo.update(project)

    def assign_tech_to_project(self, projectId, tech):
        from domain.project_technology import Project_Technology
        try:
            self.__tech_service.getOne(tech.get_id())
        except ValueError:
            self.__tech_service.add(tech)  # Daca technologia nu exista o adaug

        self.__project_tech_repo.add(Project_Technology(projectId, tech.get_id()))
        return tech

    def unassign_tech_from_project(self, projectId, techId):
        pt = self.__project_tech_repo.getOne(projectId, techId)
        if pt is None:
            raise ValueError("Technology was not assigned to project")

        self.__project_tech_repo.remove(pt)

        if not self.__project_tech_repo.getAllForTechnology(techId):  # Lista goala
            self.__tech_service.remove(techId)

    def getUsersForProject(self, projectId):
        return self.__user_project_repo.getAllForProject(projectId)  # TODO

    def getTechnologiesForProject(self, projectId):
        return [self.__tech_service.getOne(x.get_technology_id()) for x in self.__project_tech_repo.getAllForProject(projectId)]

    def getProjectsForUser(self, userId):
        return self.__user_project_repo.getAllForUser(userId)  # TODO

    def getProjectsForTechnology(self, techId):
        return [self.getOneProject(x.get_project_id()) for x in self.__project_tech_repo.getAllForTechnology(techId)]
