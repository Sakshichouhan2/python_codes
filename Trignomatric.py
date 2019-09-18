def main():
        import math
        trig = input("Do You Want To Calculate Sine,Cosine,Tangent?")

        if tring =='sin' or tring == 'Sine': 
                a = int(input("what is the angel measure?"))
                result = math.sin(math.radians(a))
                print('The ans is'+str(result))
                main()
        elif tring == 'cos' or tring == 'Cosine':
                a = int(input("what is the angel measure?"))
                result = math.cos(math.radians(a))
                print('The ans is'+str(result))
                main()
        elif tring == 'tan' or tring == 'Tangent':
                a = int(input("what is the angel measure?"))
                result = math.tan(math.radians(a))
                print('The ans is'+str(result))
                main()
        else:
                print('I Do Not Understand')
                main()
        main()
