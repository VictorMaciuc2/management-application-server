class DepartmentService:

    def __init__(self, __repo):
        self.__repo = __repo

    def add(self,department):
        '''
        :param department: Department
        :return:
        raises value error if department already exists
        '''
        departmentfound = self.__repo.getOne(self.__repo,department.get_id())
        if (departmentfound != None):
            raise ValueError("Already exists a department with given id")
        self.__repo.add(self.__repo,department)

    def getAll(self):
        '''
        :return: lists of departments
        '''
        departments =  self.__repo.getAll(self.__repo)
        return departments

    def getOne(self,id):
        '''
        :param id: int
        :return: Department
         raises value error if id does not exist
        '''
        department = self.__repo.getOne(self.__repo,id)
        if(department==None):
            raise ValueError("Department with given id does not exist.")
        return department

    def remove(self,id):
        '''
        removes department by id
        :param id: int
        :return:
        raise value error if id does not exist.
        '''
        department = self.__repo.getOne(self.__repo, id)
        if (department == None):
            raise ValueError("Department with given id does not exist.")
        self.__repo.remove(self.__repo,department)

    def update(self,department):
        '''
        updates department
        :param Department: department
        :return:
        raise value error if id does not exist.
        '''
        departmentfound = self.__repo.getOne(self.__repo, department.get_id())
        if (departmentfound == None):
            raise ValueError("Department with given id does not exist.")

        self.__repo.update(self.__repo,department)