from Model import Assignment, Employee, Job
from db import session, engine
from sqlalchemy import create_engine
from sqlalchemy import text

# create an engine
engine = create_engine('sqlite:///example.db')

# create a configured "Session" class v
# Session = sessionmaker(bind=engine)

# create a Session
# session = Session()

'''
Query all employee records from the employee table
And query employee with condition, emp_num > 101
'''
# employees = session.query(Employee).all()

# for employee in employees:
#     print(employee.emp_lname, employee.emp_fname, employee.emp_hiredate)

# print(employees.emp_fname)

# employees = session.query(Employee).filter(Employee.emp_num > 101).all()
# for employee in employees:
#     print(employee.emp_lname, employee.emp_fname, employee.emp_hiredate)


'''
Join employee with job
'''
# employees = session.query(Employee, Job).filter(Employee.job_code == Job.job_code).all()
# for employee in employees:
#     print(employee.Employee.emp_lname, employee.Employee.emp_fname, employee.Job.job_description)

'''
Insert new employee record
'''
# employee = Employee(emp_num=999, emp_lname="Doe", emp_fname="John", emp_initial="D", emp_hiredate="2020-01-01")
# session.add(employee)
# session.commit()

'''
Update employee record

'''
# employee = session.query(Employee).filter(Employee.emp_num == 999).first()
# employee.job_code = 510
# session.commit()

'''
Delete employee record
'''
# employee = session.query(Employee).filter(Employee.emp_num == 999).first()
# session.delete(employee)
# session.commit()

'''
Query assigment where assign_date is larger than 2010-01-01
'''
assignments = session.query (Assignment) .filter(
Assignment.assign_date > "2010-03-22") .all()
for assignment in assignments: 
    print(assignment.assign_num, assignment.assign_date, assignment.proj_num, assignment.emp_num,
assignment.assign_job, assignment.assign_hours, assignment.assign_charge)