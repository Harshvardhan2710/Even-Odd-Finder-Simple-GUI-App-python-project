from tkinter import *
root = Tk()
root.title("Even Odd Finder by harsh")
root.geometry("500x500+100+50")
f = ("Times new roman", 30, "bold")

def check():
	try:
		n = int(ent_num.get())
		if n % 2 == 0:
			res = "Even"
		else:
			res = "Odd"
		lab_ans.configure(text=res)
	except ValueError:
		lab_ans.configure(text="u shoud enter integer ony")
lab_num = Label(root, text="Enter Integer", font=f)
ent_num = Entry(root, font=f)
btn_find = Button(root, text="Find Even/Odd", font=f,command=check)
lab_ans = Label(root,font=f)

lab_num.pack(pady=20) 
ent_num.pack(pady=20)
btn_find.pack(pady=20)
lab_ans.pack(pady=20)

root.mainloop()
