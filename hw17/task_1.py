from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base



Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subjects = relationship('StudentSubject', back_populates='student')

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship('StudentSubject', back_populates='subject')

class StudentSubject(Base):
    __tablename__ = 'student_subjects'

    id = Column(Integer, primary_key=True) 
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))

    student = relationship('Student', back_populates='subjects')
    subject = relationship('Subject', back_populates='students')

engine = create_engine('postgresql://yaroslav:password@localhost:5432/postgres')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

english = Subject(name='English')
student1 = Student(name='Alex', subjects=[StudentSubject(subject=english)])
student2 = Student(name='Maria', subjects=[StudentSubject(subject=english)])
session.add_all([student1, student2])
session.commit()

visited_english = session.query(Student.name).\
    join(StudentSubject, Student.id == StudentSubject.student_id).\
    join(Subject, Subject.id == StudentSubject.subject_id).\
    filter(Subject.name == 'English').all()

for student in visited_english:
    print(student[0])

session.close()
