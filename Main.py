from tkinter import *
import tkinter
import sqlite3
from email.message import EmailMessage
from tkinter import messagebox  
import pyautogui #pip install pyautogui
import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
import os
import cv2
from tkinter import * 
from tkinter.ttk import *
from PIL import Image
import numpy as np
from PIL import Image
from PIL import Image, ImageFilter
import smtplib
from email.message import EmailMessage
import webbrowser
from PIL import ImageTk, Image

window = Tk()
window.title("Login or Signup or Share Page")
window.iconbitmap(r'E:\Numpy\login.ico')
window.geometry("910x650")



attachments = []

def login():

	def login_database():
		conn = sqlite3.connect("1.db")
		cur = conn.cursor()
		cur.execute("SELECT * FROM test WHERE email=? AND password=?",(e1.get(),e2.get()))
		row = cur.fetchall()
		conn.close()
		print(row)
		if row!=[]:
			user_name = row[0][1]
			# loggedin_window = Tk()
			# loggedin_window.geometry('400x400')

			# l1 = Label(loggedin_window, text='\n[+] Logged In with : '+user_name)
			# l1.pack()

			#Screenshot Code
			def UploadAction():
			    filename = filedialog.askopenfilename()
			    global fp
			    fp=filename.replace("/", "//")
				#print(fp)

			def screenshot():
				root.withdraw()
				dt=datetime.now()
				filename=int(dt.strftime("%Y%m%d%H%M%S"))
				filename='E:\\Numpy\\ScreenshotData/{}.png'.format(filename)
				time.sleep(1)
				img=pyautogui.screenshot(filename)
				img.show()
				root.deiconify()

			def grey(event=None):
				print(fp)
				#im = np.array(Image.open("E:\\PythonProject\\shiva.jpg"))
				im = np.array(Image.open(fp))
				im_i = 255 - im
				Image.fromarray(im_i).save('E:\\Numpy\\Image\\Grey.jpg')

			def Black_white():
				im = np.array(Image.open(fp).convert('L')) #you can pass multiple arguments in single line
				gr_im= Image.fromarray(im).save('E:\\Numpy\\Image\\Black White.png')

			def red():
				im = np.array(Image.open(fp))
				im_R = im.copy()
				im_R[:, :, (1, 2)] = 0
				pil_img = Image.fromarray(im_R)
				pil_img.save('E:\\Numpy\\Image\\Red.jpg')

			def green():
				im = np.array(Image.open(fp))
				im_G = im.copy()
				im_G[:, :, (0, 2)] = 0
				pil_img = Image.fromarray(im_G)
				pil_img.save('E:\\Numpy\\Image\\Green.jpg')

			def blue():
				im = np.array(Image.open(fp))
				im_B = im.copy()
				im_B[:, :, (0, 1)] = 0
				pil_img = Image.fromarray(im_B)
				pil_img.save('E:\\Numpy\\Image\\Blue.jpg')

			def color_reduction1():
				im = np.array(Image.open(fp))
				im_32 = im // 32 * 32
				Image.fromarray(im_32).save('E:\\Numpy\\Image\\color_reduction1.jpg')

			def color_reduction2():
				im = np.array(Image.open(fp))
				im_64 = im // 64 * 64
				Image.fromarray(im_64).save('E:\\Numpy\\Image\\color_reduction2.jpg')

			def color_reduction3():
				im = np.array(Image.open(fp))
				im_128 = im // 128 * 128
				Image.fromarray(im_128).save('E:\\Numpy\\Image\\color_reduction3.jpg')

			def paste_with_slice():
				src = np.array(Image.open(fp).resize((128, 128)))
				dst = np.array(Image.open(fp).resize((256, 256)))
				dst_copy = dst.copy()
				dst_copy[64:192, 64:192] = src
				Image.fromarray(dst_copy).save('E:\\Numpy\\Image\\paste_with_slice.jpg')

			def rotate_clockwise_90():
				img = cv2.imread(fp)
				img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
				cv2.imwrite('E:\\Numpy\\Image\\rotate_clockwise_90.jpg', img_rotate_90_clockwise)

			def rotate_clockwise_270():
				img = cv2.imread(fp)
				img_rotate_90_counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
				cv2.imwrite('E:\\Numpy\\Image\\rotate_clockwise_270.jpg', img_rotate_90_counterclockwise)

			def rotate_clockwise_180():
				img = cv2.imread(fp)
				img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
				cv2.imwrite('E:\\Numpy\\Image\\rotate_clockwise_180.jpg', img_rotate_180)

			def rotate_normal():
				im = np.array(Image.open(fp))
				Image.fromarray(im).save('E:\\Numpy\\Image\\rotate_normal.jpg')

			def red_green_blue():
				im_gray = np.array(Image.open(fp).convert('L'))
				im_bool = im_gray > 128
				im_dst = np.empty((*im_gray.shape, 3))
				r, g, b = 255, 128, 32
				im_dst[:, :, 0] = im_bool * r
				im_dst[:, :, 1] = im_bool * g
				im_dst[:, :, 2] = im_bool * b
				Image.fromarray(np.uint8(im_dst)).save('E:\\Numpy\\Image\\red_green_blue.jpg')

			def blur():
				OriImage = Image.open(fp)
				OriImage.show()

				blurImage = OriImage.filter(ImageFilter.BLUR)
				blurImage.show()
				#Save blurImage
				blurImage.save('E:\\Numpy\\Image\\BlurImage.jpg')

			def box_blur():
				#Open existing image
				OriImage = Image.open(fp)
				OriImage.show()
				#Applying BoxBlur filter
				boxImage = OriImage.filter(ImageFilter.BoxBlur(5))
				boxImage.show()
				#Save Boxblur image
				boxImage.save('E:\\Numpy\\Image\\BlurImageBox.jpg')

			def curve_blur():
				OriImage = Image.open(fp)
				OriImage.show()
				gaussImage = OriImage.filter(ImageFilter.GaussianBlur(5))
				gaussImage.show()
				gaussImage.save('E:\\Numpy\\Image\\BlurImageCurve.jpg')


			def grey_black():
				im = cv2.imread(fp)
				im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
				th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)
				cv2.imwrite('E:\\Numpy\\Image\\grey_black.jpg', im_gray_th_otsu)

			login_window.destroy()
			root = tk.Tk()
			root.geometry("600x1000")
			root.title("PLAY WITH IMAGES....")


			l1 = Label(root, text='\n[+] Logged In with : '+user_name)
			l1.pack()



			#line
			canvas_width = 500
			canvas_height = 40
			w = Canvas(root, 
			           width=canvas_width,
			           height=canvas_height)
			w.pack()
			y = int(canvas_height / 2)
			w.create_line(0, y, canvas_width, y, fill="#476042")


			my_label=Label(root, text="SCREENSHOT", width=25, background="pink",font=('bold',16))
			my_label.configure(anchor=CENTER)
			my_label.pack(pady=10)
			my_button1=tk.Button(root, text="TAKE SCREENSHOT",width=20, command=screenshot,font=('bold',10),bg='lightgreen')
			my_button1.pack()
			my_button2=tk.Button(root, text="QUIT",width=20,command=quit,font=('bold',10),bg='skyblue')
			my_button2.pack()

			# canvas_width = 500
			# canvas_height = 40
			# w = Canvas(root, width=canvas_width,height=canvas_height)
			# w.pack()
			# y = int(canvas_height / 2)
			# w.create_line(0, y, canvas_width, y, fill="#476042")

			# #Email
			# button = tk.Button(root, text='Email Your Image', width=20, bg='red',fg='white', command=EmailAttach,font=('bold',10))
			# button.pack() 


			canvas_width = 500
			canvas_height = 40
			w = Canvas(root, width=canvas_width,height=canvas_height)
			w.pack()
			y = int(canvas_height / 2)
			w.create_line(0, y, canvas_width, y, fill="#476042")

			my_label=Label(root, text="IMAGE PROCESSING", width=25, background="yellow",font=('Helvtica',15))
			my_label.configure(anchor=CENTER)
			my_label.pack()
			button = tk.Button(root, text='Select Image from Galary.', command=UploadAction, fg='white', bg='blue',width=25, font=('Helvtica'))
			button.pack(pady=10)

			button = tk.Button(root, text='GREY',width=20, bg='grey',fg='white',command=grey,font=('bold',10))
			button.pack()
			#button.pack(pady=10)

			button = tk.Button(root, text='BLACK_WHITE', bg='black',fg='white',width=20, command=Black_white,font=('bold',10))
			button.pack() 

			button = tk.Button(root, text='RED', width=20, bg='red',fg='white',command=red,font=('bold',10))
			button.pack() 

			button = tk.Button(root, text='GREEN', width=20, bg='green',fg='white',command=green,font=('bold',10))
			button.pack()  

			button = tk.Button(root, text='BLUE', width=20,bg='blue',fg='white',command=blue,font=('bold',10))
			button.pack() 
			button = tk.Button(root, text='RED_GREEN_BLUE', bg='lime',fg='white',width=20, command=red_green_blue,font=('bold',10))
			button.pack()

			button = tk.Button(root, text='COLOR_REDUCTION1', bg='maroon',fg='white',width=20, command=color_reduction1,font=('bold',10))
			button.pack() 

			button = tk.Button(root, text='COLOR_REDUCTION2', bg='orange',fg='white',width=20, command=color_reduction2,font=('bold',10))
			button.pack()
			button = tk.Button(root, text='COLOR_REDUCTION#',bg='brown',fg='white', width=20, command=color_reduction3,font=('bold',10))
			button.pack()
			button = tk.Button(root, text='GREY_BLACK', bg='teal',fg='white',width=20, command=grey_black,font=('bold',10))
			button.pack()
			button = tk.Button(root, text='PASTE_WITH_SLICE',bg='violet',fg='white', width=20, command=paste_with_slice,font=('bold',10))
			button.pack()

			button = tk.Button(root, text='ROTATE_90',bg='silver',fg='black', width=20, command=rotate_clockwise_90,font=('bold',10))
			button.pack()
			# button = tk.Button(root, text='ROTATE_270', bg='gold',fg='black',width=20, command=rotate_clockwise_270,font=('bold',10))
			# button.pack()
			button = tk.Button(root, text='ROTATE_180', width=20, bg='orchid',command=rotate_clockwise_180,font=('bold',10))
			button.pack()
			button = tk.Button(root, text='ROTATENORMAL', width=20, bg='wheat',command=rotate_normal,font=('bold',10))
			button.pack()

			button = tk.Button(root, text='BLUR', width=20, bg='crimson',command=blur,font=('bold',10))
			button.pack()
			button = tk.Button(root, text='BOXBLUR', width=20, bg='navy',fg='white',command=box_blur,font=('bold',10))
			button.pack()
			button = tk.Button(root, text='CURVEBLUR', width=20, bg='coral',fg='black',command=curve_blur,font=('bold',10))
			button.pack()


			root.mainloop()


			#l3.config(text="UserName Found with the name: "+user_name)
		else:
			l3.config(text="UserName Not Found")

	window.destroy()
	login_window = Tk()
	login_window.title("Login Page")
	login_window.iconbitmap(r'E:\Numpy\login.ico')
	login_window.geometry("650x350")

	label = Label(login_window, text="Login", width=36, background="#3944BC",foreground="white" ,font=('bold',20))
	label.configure(anchor="center")
	label.grid(row=1, rowspan = 3, columnspan = 5)

	l1 = Label(login_window, text="Email :- ", font="times 20")
	l1.grid(row=4, column=1)
	l2 = Label(login_window, text="Password :- ", font="times 20")
	l2.grid(row=5, column=1)
	l3 = Label(login_window, font="times 20")
	l3.grid(row=8, column=2)

	email_text = StringVar()
	e1 = Entry(login_window, textvariable=email_text)
	e1.grid(row=4, column=2)
	password_text = StringVar()
	e2 = Entry(login_window,show="*", textvariable=password_text)
	e2.grid(row=5, column=2)

	b1=Button(login_window, text="login", width=20, command=login_database)
	b1.grid(row=8, column=2)

	login_window.mainloop()


attachments = []
def EmailAttach():

	def attachFile():
		filename = filedialog.askopenfilename(initialdir='C:/',title='Select a file')
		attachments.append(filename)
		#notif.config(fg='green', text='Attached ' + str(len(attachments)) + ' files')
		messagebox.showinfo("Attached", str(len(attachments))+" Files Attached.")  

		
		filename = attachments[0]
		filetype = filename.split('.')
		filetype = filetype[1]
		if filetype=="jpg" or filetype=="JPG" or filetype=="png" or filetype=="PNG":
			print("Image Detected")
		else:
			print("Document Detected")

	def send():
		try:
			msg = EmailMessage()
			username = temp_username.get()
			password = temp_password.get()
			to = temp_receiver.get()
			subject = temp_subject.get()
			body = temp_body.get()
			msg['subject'] = subject
			msg['from'] = username
			msg['to'] = to
			msg.set_content(body)

			filename = attachments[0]
			filetype = filename.split('.')
			filetype = filetype[1]
			if filetype=="jpg" or filetype=="JPG" or filetype=="png" or filetype=="PNG":
				import imghdr
				with open(filename, 'rb') as f:
					file_data = f.read()
					image_type = imghdr.what(filename)
				msg.add_attachment(file_data, maintype='image', subtype=image_type, filename=f.name)

			else:
				with open(filename, 'rb') as f:
					file_data = f.read()
				msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=f.name)

			if username=="" or password=="" or to=="" or subject=="" or body=="":
				#notif.config(text='All fields are required', fg="red")
				messagebox.showerror("Error", "All fields are required")
				return
			else:
				finalMessage = 'Subject: {}\n\n{}'.format(subject, body)
				server = smtplib.SMTP('smtp.gmail.com',587)
				server.starttls()
				server.login(username, password)
				server.send_message(msg)
				messagebox.showinfo("Sent", "Email has been sent")
				#notif.config(text='Email has been sent', fg='green')
		except error as e:
			print("error")
			messagebox.showerror("Error", "Error Sending email")
			#notif.config(text="Error Sending email", fg="red")


	def reset():
		usernameEntry.delete(0, 'end')
		passwordEntry.delete(0, 'end')
		receiverEntry.delete(0, 'end')
		subjectEntry.delete(0, 'end')
		bodyEntry.delete(0, 'end')



	attachments = []
	window.destroy()
	master = Tk()
	master.title('Custom Python Email App')

	l1 = Label(master, text="Custom Email App", font=("Calibri",15))
	l1.grid(row=0, sticky=N)
	l2 = Label(master, text="Use the form below to send an email", font=("Calibri",11))
	l2.grid(row=1, sticky=W, padx=5)
	l3 = Label(master, text="Email", font=("Calibri",11))
	l3.grid(row=2, sticky=W, padx=5)
	l4 = Label(master, text="Password", font=("Calibri",11))
	l4.grid(row=3, sticky=W, padx=5)
	l5 = Label(master, text="To", font=("Calibri",11))
	l5.grid(row=4, sticky=W, padx=5)
	l6 = Label(master, text="Subject", font=("Calibri",11))
	l6.grid(row=5, sticky=W, padx=5)
	l7 = Label(master, text="Body", font=("Calibri",11))
	l7.grid(row=6, sticky=W, padx=5)
	#notif = Label(master, text="", font=("Calibri",11))
	#notif.grid(row=7, sticky=S, padx=5)

	#Storage
	temp_username = StringVar()
	temp_password = StringVar()
	temp_receiver = StringVar()
	temp_subject = StringVar()
	temp_body = StringVar()

	#Entries
	usernameEntry = Entry(master, textvariable=temp_username)
	usernameEntry.grid(row=2, column=0, )
	passwordEntry = Entry(master, show="*" ,textvariable=temp_password)
	passwordEntry.grid(row=3, column=0)
	receiverEntry = Entry(master, textvariable=temp_receiver)
	receiverEntry.grid(row=4, column=0)
	subjectEntry = Entry(master, textvariable=temp_subject)
	subjectEntry.grid(row=5, column=0)
	bodyEntry = Entry(master, textvariable=temp_body)
	bodyEntry.grid(row=6, column=0)

	# b3 = Button(master, text="Attachment", command=attachFile)
	# b3.grid(row=7, sticky=W)
	b1 = Button(master, text="Send", command=send)
	b1.grid(row=8, sticky=W, pady=10, padx=5)
	b2 = Button(master, text="Reset", command=reset)
	b2.grid(row=8, sticky=W, padx=110, pady=40)
	b3 = Button(master, text="Attachment", command=attachFile)
	b3.grid(row=8, sticky=W, padx=210, pady=40)









def signup():

	def signup_database():
		conn = sqlite3.connect("1.db")
		cur = conn.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, name text, email text, password text)")
		cur.execute("INSERT INTO test Values(NULL, ?, ?, ?)", (e1.get(), e2.get(), e3.get()))
		l4 = Label(signup_window, text="Account Created", font="times 15")
		l4.grid(row=8, column=2)

		b3 = Button(signup_window, text="Login Here", width=10,command=login)
		b3.grid(row=9, column=2)


		conn.commit()
		conn.close()

	#window.destroy()
	signup_window = Tk()
	signup_window.geometry("650x350")
	signup_window.title("Signup Page")
	signup_window.iconbitmap(r'E:\Numpy\login.ico')
	

	label = Label(signup_window, text="Login", width=36, background="#3944BC",foreground="white" ,font=('bold',20))
	label.configure(anchor="center")
	label.grid(row=1, rowspan = 3, columnspan = 5)

	l1 = Label(signup_window, text="UserName :- ", font="times 20")
	l1.grid(row=4, column=1)
	l2 = Label(signup_window, text="Email :- ", font="times 20")
	l2.grid(row=5, column=1)
	l3 = Label(signup_window, text="Password :- ", font="times 20")
	l3.grid(row=6, column=1)

	name_text = StringVar()
	e1 = Entry(signup_window, textvariable=name_text)
	e1.grid(row=4, column=2)
	email_text = StringVar()
	e2 = Entry(signup_window, textvariable=email_text)
	e2.grid(row=5, column=2)
	password_text = StringVar()
	e3 = Entry(signup_window, show="*", textvariable=password_text)
	e3.grid(row=6, column=2)

	b1 = Button(signup_window, text="Login", width=20,command=signup_database)
	b1.grid(row=11, column=2)

	signup_window.mainloop()

new = 1
url = "https://web.whatsapp.com/"
def WhatsappAttach():
	webbrowser.open(url,new=new)


photo = ImageTk.PhotoImage(Image.open("LoginHeader2.jpg"))
tkinter.Label(window, image=photo).grid(rowspan = 3, columnspan = 5, row =0,column = 0)

label=Label(window, text="Login or Signup or Share", width=51, background="#3944BC",foreground="white" ,font=('bold',20))
label.configure(anchor="center")
label.grid(row=4, rowspan = 3, columnspan = 5)

label1 = Label(window, text="Welcome to Play with Images Projects. ", font=(15))
label1.grid(row=8, column=0)
label2 = Label(window, text="Here you can take Screenshot of window and filter the images into the green, blue, red, etc colors. ", font=(7))
label2.grid(row=9, column=0)

canvas_width = 910
canvas_height = 20
w = Canvas(window, width=canvas_width,height=canvas_height)
w.grid(row=10, column=0)
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="red")

label3 = Label(window, text="If you have already member then Login Here, ", font=("Courier", 15))
label3.grid(row=11, column=0)

b1 = Button(window, text="Login", command=login)
b1.grid(row=12, column=0)

canvas_width = 910
canvas_height = 20
w = Canvas(window, width=canvas_width,height=canvas_height)
w.grid(row=13, column=0)
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="blue")

label4 = Label(window, text="If you are not member, Then Signup Here, ", font=("Courier", 15))
label4.grid(row=14, column=0)

b2 = Button(window, text="Signup", command=signup)
b2.grid(row=15, column=0)

canvas_width = 910
canvas_height = 50
w = Canvas(window, width=canvas_width,height=canvas_height)
w.grid(row=17, column=0)
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="red")


label5 = Label(window, text="OR ", font=("Courier", 25))
label5.grid(row=18, column=0)
label6 = Label(window, text="Share your file with, ", font=("Courier", 15))
label6.grid(row=19, column=0)

b3 = Button(window, text="Email", width=20, command=EmailAttach)
b3.grid(row=20, column=0)

b4 = Button(window, text="Whatsapp", width=20, command=WhatsappAttach)
b4.grid(row=21, column=0)

canvas_width = 910
canvas_height = 50
w = Canvas(window, width=canvas_width,height=canvas_height)
w.grid(row=22, column=0)
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="blue")



window.mainloop()