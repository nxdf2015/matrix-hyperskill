from numbers import Number
from operator import mul
from functools import partial
def SameSize(f):

    def wrapper(self,other):

         if self.shape == other.shape:
            return f(self, other)
         else:
             return "The operation cannot be performed."
    return wrapper



def to_number(x):
    if round(float(x))==float(x):
        return int(float(x))
    else:
        return float(x)




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
        self.mat=[]
        for i in range(n_row):
            row=input().split(" ")
            if len(row) < n_column:
                raise Exception()
            try:
                self.mat.append(list(map(to_number,row)))
            except Exception as e:
                print("exception",e)
                return False
        return True

    @SameSize
    def __add__(self, other):
       matrice = Matrice(* self.shape)
       matrice.rows = [list(map(lambda x,y : x+y , row,other.mat[i])) for i,row in enumerate(self.mat) ]
       return matrice

    def __rmul__(self, other):
        if isinstance(other,Number):
            mult = partial(mul,other)
            new_rows = [ list(map(mult,row)) for row in self.mat]
            return Matrice.create(new_rows)

    def __mul__(self,other):
        if isinstance(other,Number):
            return other * self

    def __iter__(self):
        return iter(self.mat)

    def transpose(self):
        rows = [ [row[i] for row in self.mat] for i in range(self.shape[1])]
        return Matrice.create(rows)

    def product(self,row,col):
        return sum([ x * y for x,y in zip(row,col)])

    def __matmul__(self, other):
        rows = [ [ self.product(row,col) for col in other.transpose() ]for row in self.mat]
        return Matrice.create(rows)


    def __str__(self):
       return "\n".join([" ".join((map(str,row)))for row in self.mat])


def get_matrice(msg):
    row,col =list(map(int,input(f"Enter size of {msg}: ").split(" ")))
    print(f"Enter {msg} matrix: ")
    mat = Matrice(row,col)
    mat.set_rows()

    return mat

def menu():
    while True:
        print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit")
        choice=int(input())


        if choice==0:
            break
        mat1=get_matrice("first matrix")
        if choice == 1 or choice == 3:
            mat2=get_matrice("second matrix")
            if choice == 1:
                result= mat1 + mat2
            else:
                result= mat1 @ mat2
        else:
            c=to_number(input("Enter constant:"))
            result =  mat1 * c
        print("The result is:")
        print(result)
        print()



menu()
