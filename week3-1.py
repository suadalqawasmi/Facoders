''''اكتبي لعبة تطبع اسم اللعبة أولاً
 Numbers from 1 to 10
ثم تطلب من المستخدم أن يحزر الرقم
"Guess the number: "
إذا المستخدم لم يدخل الرقم الصحيح ستبقى اللعبة تسأله للأبد، إذا قام بإدخال الرقم الصحيح، يظهر للمستخدم:
"Great! You did it!"
لا تنسي أن تقومي بتخزين رقم من اختيارك ليكون هو الرقم الصحيح وتخزينه في متغير.
'''

x=6

print("Numbers from 1 to 10")
number =int(input("Guess the number: "))

if number >=1 and number <=10 :
    if number == x :
        print("Great!you did it!")
