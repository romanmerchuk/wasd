class person:
    name ="roman"
    age =12
    def get(self):
        print(self.name,self.age)

    def checkAge(self):
        if self.age > 18:
            print('Повнолітня людина')

        else:
            print('Error')
a=person()
a.get()