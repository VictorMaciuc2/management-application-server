class ProjectService:
    def __init__(self, __repo):
        self.__repo = __repo

    def getAll(self):
        return self.__repo.getAll()

    def getOne(self, id):
        project = self.__repo.getOne(id)
        if project is None:
            raise ValueError("The project with the given ID does not exist.")
        return project

    def add(self, project):
        p = self.__repo.getOne(project.get_id())
        if p is not None:
            raise ValueError("A project with the given ID already exists.")
        return self.__repo.add(project)

    def remove(self, id):
        project = self.__repo.getOne(id)
        if project is None:
            raise ValueError("The project with the given ID does not exist.")
        self.__repo.remove(project)

    def update(self, project):
        p = self.__repo.getOne(project.get_id())
        if p is None:
            raise ValueError("The project with the given ID does not exist.")
        return self.__repo.update(project)
