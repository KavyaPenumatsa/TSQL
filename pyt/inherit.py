class employee:
    num_employee=0
    raise_amount=1.04
    def __init__(self,first,last,sal):
        self.first=first
        self.last=last
        self.sal=sal
        self.email=first + '.' + last + '@company.com'
        employee.num_employee+=1
    def fullname (self):
        return '{} {}' .format(self.first,self.last)
    def apply_raise(self):
        self.sal=int(self.sal* raise_amount)

class developer(employee):
    raise_amount=1.10
    def __init__(self,first,last,sal,prog_lang):
        super().__init__(first,last,sal)
        self.prog_lang=prog_lang
emp_1=developer('kavya','p',100000,'python')
print(emp_1.prog_lang)
