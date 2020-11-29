class ProjectService:
    def __init__(self, __repo, technology_service, project_technology_repo, client_service):
        self.__project_repo = __repo
        self.__tech_service = technology_service
        self.__project_tech_repo = project_technology_repo
        self.__client_service = client_service

    def getAll(self):
        return self.__project_repo.getAll()

    def getOne(self, id):
        project = self.__project_repo.getOne(id)
        if project is None:
            raise ValueError("The project with the given ID does not exist.")
        return project

    def add(self, project):
        p = self.__project_repo.getOne(project.get_id())
        if p is not None:
            raise ValueError("A project with the given ID already exists.")
        return self.__project_repo.add(project)

    def remove(self, id):
        project = self.__project_repo.getOne(id)
        if project is None:
            raise ValueError("The project with the given ID does not exist.")
        self.__project_repo.remove(project)

    def update(self, project):
        p = self.__project_repo.getOne(project.get_id())
        if p is None:
            raise ValueError("The project with the given ID does not exist.")
        return self.__project_repo.update(project)
