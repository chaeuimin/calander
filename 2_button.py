from tkinter import *

root = Tk()
root.title('Nado GUI')

btn1 = Button(root, text='버튼1')
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text='버튼2')  # 버튼 텍스트가 늘어나도 넓이가 더 넓어지는게 가능
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text='버튼3')
btn3.pack()

btn4 = Button(root, width=10, height=3, text='버튼4') # width,height는 고정된크기 텍스트가 많아져도 클자가 잘릴지언정 고정됨
btn4.pack()

btn5 = Button(root, fg='red',bg='yellow', padx=10, pady=5, text='버튼5')
btn5.pack()

photo =PhotoImage(file="gui_baisic/check.png")
btn6 = Button(root, image=photo)
btn6.pack()

root.mainloop()