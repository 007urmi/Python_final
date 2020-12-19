
from Question import Question
from System import System

s= System()

q = s.addQuestion("DBMS","In the relational model, sardinality is termed as:\nA. A number of tuples\nB.A number of attributes\nC.A number of tables\nD. A number of constraints", "A")
q = s.addQuestion("DBMS","The view of total database content is:\nA.Conceptual view\nB.Internal view\nC.External view\nD.Physical view", "A")
q = s.addQuestion("DBMS","Key to represent relationship between tables is called:\na.Primary key\nB.Secondary key\nC.Foreign key\nD.None of these","C")
q = s.addQuestion("DBMS","The _______ clause is used to list the attributes desired in the result of a query:\nA.Where\nB.Select\nC.From\nD.Distinct","B")

#s.display()
s.runTest()