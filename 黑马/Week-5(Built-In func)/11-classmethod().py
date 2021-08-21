###################   11.classmethod()
'''
Converts a method into a class method
'''

class Person:
  name = 'Person 1'
  age = 20

  @classmethod         # here you can put your values
  def samle(cls, gpa): # class method
    print(gpa)

  def get_age(self): # instance method
    return self.age

p = Person()

# you can call the class method in 2 ways: 

Person.samle()
# or
p.samle
