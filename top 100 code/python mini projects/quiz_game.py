

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name':'Jhon', 'age' : 22}

student_info(*courses, **info)