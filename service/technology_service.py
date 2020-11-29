class TechnologyService:
    def __init__(self, __repo):
        self.__repo = __repo

    def getAll(self):
        return self.__repo.getAll()

    def getOne(self, id):
        tech = self.__repo.getOne(id)
        if tech is None:
            raise ValueError("The technology with the given ID does not exist.")
        return tech

    def add(self, project):
        tech = self.__repo.getOne(project.get_id())
        if tech is not None:
            raise ValueError("A technology with the given ID already exists.")
        return self.__repo.add(tech)

    def remove(self, id):
        tech = self.__repo.getOne(id)
        if tech is None:
            raise ValueError("The technology with the given ID does not exist.")
        self.__repo.remove(tech)

    def update(self, project):
        tech = self.__repo.getOne(project.get_id())
        if tech is None:
            raise ValueError("The technology with the given ID does not exist.")
        return self.__repo.update(tech)
