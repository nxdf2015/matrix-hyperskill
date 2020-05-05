from numbers import Number
from operator import mul
from functools import partial
def SameSize(f):

    def wrapper(self,other):

         if self.shape == other.shape:
            return f(self, other)
         else:
             return "ERROR"
    return wrapper






class Matrice:
    def __init__(self,rows,columns):
        self.shape=(rows,columns)
        self.mat=[]

    @classmethod
    def create(cls,rows):
        matrice = cls(len(rows),len(rows[0]))
        matrice.mat=rows
        return matrice
     
    @property
    def rows(self):
        return self.mat

    @rows.setter
    def rows(self,rows):
        self.mat=rows

    def set_rows(self):
        n_row,n_column=self.shape
        for i in range(n_row):
            row=input().split(" ")
            try:
                self.mat.append(list(map(int,row)))
            except:
                 return False
        return True

    @SameSize
    def __add__(self, other):
       rows = [list(map(lambda x,y : x+y , row,other.mat[i])) for i,row in enumerate(self.mat) ]
       return Matrice.create(rows)

    def __rmul__(self, other):
        if isinstance(other,Number):
            mult = partial(mul,other)
            new_rows = [ list(map(mult,row)) for row in self.mat]
            return Matrice.create(new_rows)

    def __mul__(self,other):
        if isinstance(other,Number):
            return other * self

    def __str__(self):
       return "\n".join([" ".join((map(str,row)))for row in self.mat])



def get_matrice():
    n,m = map(int, input().split(" "))
    matrice = Matrice(n,m)
    matrice.set_rows()

    return matrice

mat=get_matrice()
n=int(input())

print(mat* n)

