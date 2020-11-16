class DepartmentService:
    def __init__(self, __repo):
        self.__repo = __repo

    def add(self,department):
        departmentfound = self.__repo.getOne(department.get_id())
        if departmentfound != None :
            raise ValueError("Already exists a department with given id")
        return self.__repo.add(department)

    def getAll(self):
        departments =  self.__repo.getAll()
        return departments

    def getOne(self,id):
        department = self.__repo.getOne(id)
        if(department==None):
            raise ValueError("department with given id does not exist.")
        return department

    def remove(self,id):
        department = self.__repo.getOne(id)
        if (department == None):
            raise ValueError("department with given id does not exist.")
        self.__repo.remove(department)

    def update(self,department):
        departmentfound = self.__repo.getOne(department.get_id())
        if (departmentfound == None):
            raise ValueError("department with given id does not exist.")

        self.__repo.update(department)

        return department