from controller import db
from domain.Department import Department

class DepartmentRepository:

    def getAll(self):
        '''
        :return: list of departments
        '''
        departments = Department.query.all()
        return departments

    def getOne(self,id):
        '''
        :param id: int
        :return: Department
        '''
        department = Department.query.get(id)
        return department

    def add(self,Department):
        '''
        :param Department: Department
        :return:
        '''
        db.session.add(Department)
        db.session.commit()

    def remove(self,department):
        '''
        :param Department: Department
        :return:
        '''
        db.session.delete(department)
        db.session.commit()

    def update(self,department):
        '''
        :param department: Department
        :return:
        '''
        departmentfound = Department.query.get(department.get_id())
        departmentfound.set_name(department.get_name())
        departmentfound.set_description(department.get_description())
        db.session.commit()