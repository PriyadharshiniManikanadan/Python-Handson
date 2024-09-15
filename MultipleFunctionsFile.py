class MultipleFunctions:
    def Subfields():
        lists = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are: ")
        for items in lists:
            print(items)

    def OddEven():
        num = int(input("Enter a number:"))
        if (num%2)==1:
            print(num, "is Odd Number")
            number="OddNum"
        else:
            print(num,"is Even number")
            number="EvenNum"

    def Eligible():
        Gender=input("Your Gender: ")
        Age=int(input('Your age: '))
        if Gender== "male":
            if Age >= 21: 
                print("Eligible")
                Marriage='Eligible'
            else:
                print("NOT Eligible")
                Marriage= 'NOT Eligible'
                return Marriage
        else:
            if Age >= 18: 
                print("Eligible")
                Marriage='Eligible'
            else:
                print("NOT Eligible")
                Marriage= 'NOT Eligible'
                return Marriage

    def Percentage():
        sub1 = int(input("Subject1 = "))
        sub2 = int(input("Subject2 = "))
        sub3 = int(input("Subject3 = "))
        sub4 = int(input("Subject4 = "))
        sub5 = int(input("Subject5 = "))
        Total = sub1+sub2+sub3+sub4+sub5
        print("Total:", Total)
        Percentage = print("Percentage = ", (Total/5))
        return Percentage

    def triangle():
        height = int(input("Height : "))
        breadth = int(input("Breadth : "))
        print("Area formula: (Height*Breadth)/2")
        AreaofTriangle = print("Area of Triangle = ", (height*breadth)/2)
        Triangle = AreaofTriangle
    
        height1 = int(input("Height1 : "))
        height2 = int(input("Height2 : "))
        breadth = int(input("Breadth : "))
        print("Perimeter formula: Height1+Height2+Breadth")
        PerimeterofTriangle = print("Perimeter of Triangle: ", height1+height2+breadth)
        Triangle = PerimeterofTriangle
        return Triangle
