from numbers import Number
from operator import mul
from functools import partial

def ValidAdd(f):

    def wrapper(self,other):

         if self.shape == other.shape:
            return f(self, other)
         else:
             return "The operation cannot be performed."
    return wrapper

def ValidProduct(f):
    def wrapper(self,other):
        if  self.shape[1] == other.shape[0]:
           return  f(self,other)
        else:
            return "The operation cannot be performed"
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

    @ValidAdd
    def __add__(self, other):
       matrice = Matrice(* self.shape)
       matrice.rows = [list(map(lambda x,y : x+y , row,other.mat[i])) for i,row in enumerate(self) ]
       return matrice

    def __rmul__(self, other):
        if isinstance(other,Number):
            mult = partial(mul,other)
            new_rows = [ list(map(mult,row)) for row in self]
            return Matrice.create(new_rows)

    def __mul__(self,other):
        if isinstance(other,Number):
            return other * self

    def __iter__(self):
        return iter(self.mat)

    def transposeHorizontal(self):
        rows = self.mat[::-1]
        return Matrice.create(rows)

    def transposeVertical(self):
        return  self.transpose().transposeHorizontal().transpose()


    def transposeSide(self):
        rows =[ [row[i]for row in self ][::-1] for i in range(self.shape[1]-1,-1,-1)]
        return Matrice.create(rows)

    def transpose(self):
        rows = [ [row[i] for row in self] for i in range(self.shape[1])]
        return Matrice.create(rows)

    def product(self,row,col):
        return sum([ x * y for x,y in zip(row,col)])

    def removeLine(self,index):
        rows = self.mat[:index]+self.mat[index+1:]
        return Matrice.create(rows)

    def removeColumn(self,index):
        return  self.transpose().removeLine(index).transpose()

    def minor(self,i,j):
        return self.copy().removeColumn(j).removeLine(i).det()

    def copy(self):
        return Matrice.create(self.mat)

    def elem(self,i,j):
        return self.mat[i][j]

    def det(self):
        if self.shape==(1,1):
            return self.mat[0][0]

        row,col = self.shape
        v = 0
        for i in range(0,col):
            v +=  (-1 ) ** i  * self.elem(0,i) * self.minor(0,i)
        return v




    @ValidProduct
    def __matmul__(self, other):

        rows = [ [ self.product(row,col) for col in other.transpose() ]for row in self]
        return Matrice.create(rows)


    def __str__(self):
       return "\n".join([" ".join((map(str,row)))for row in self])


def get_matrice(msg):
    mat=False
    invalid=True
    while not mat or invalid:
        try:
            row,col =list(map(int,input(f"Enter size of {msg}: ").split(" ")))
            invalid=False
        except:
            invalid=True
        print(f"Enter {msg} matrix: ")
        mat = Matrice(row,col)
        mat.set_rows()
    return mat



def menu():
    while True:
        print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n0. Exit")
        choice=int(input())


        if choice==0:
            break

        if choice == 1 or choice == 3:
            mat1=get_matrice("first matrix")
            mat2=get_matrice("second matrix")
            if choice == 1:
                result= mat1 + mat2
            else:
                result= mat1 @ mat2
        elif choice==4:
            print("""1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line""")
            selection=int(input())
            mat1=get_matrice("matrix")
            if selection==1:
                result=mat1.transpose()
            elif selection==2:
                result=mat1.transposeSide()
            elif selection==3:
                result=mat1.transposeVertical()
            else:
                result=mat1.transposeHorizontal()
        elif choice ==5:
            mat1=get_matrice("matrix")
            result=mat1.det()
            # print(mat1)
            # print("++++++++++++")
            # print("line 1",mat1.removeLine(1))
            # print("+++++++++++++")
            # print("col 1",mat1.removeColumn(1))

        elif choice== 2:
            mat1=get_matrice("matrix")
            c=to_number(input("Enter constant:"))
            result =  mat1 * c
        print("The result is:")
        print(result)
        print()



menu()
