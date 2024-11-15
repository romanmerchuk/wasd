class person:
    newName ="roman"
    newage =12
    def get(self):
        print(self.newName,self.newage)

    def checkAge(self):
        if self.newage > 18:
            print('Повнолітня людина')

        else:
            print('Error')
a=person()
a.get()