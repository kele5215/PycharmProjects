# _*_ coding:UTF8 _*_


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 魔法函数，给类加可迭代类型
    def __getitem__(self, item):
        return self.employee[item]

    def __str__(self):
        return ",".join(self.employee)

    def __repr__(self):
        return "*".join(self.employee)


company = Company(['11', '22', '33'])

# print(len(company))

for em in company:
    print(em)

# for em in company.employee:
#     print("bu yong mo fa : " + em)

# 可以切片和获取长度
company1 = company[:2]
print(len(company1))

for em in company1:
    print("qie pian :" + em)

company = Company(['Derek', 'Tom', 'Jack'])

print(company)
