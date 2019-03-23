#!/usr/bin/python
from Tkinter import *
import tkMessageBox,Tkinter,comm
import util


class contact(util.window):
	def __init__(self):
		
		# Init
		util.window.__init__(self,"NGERA MESS APP | Computerized Reservation System | CONTACT US")

		# Top image
		canvas = Canvas(self.root,width = 600, height = 150, bg = 'white')
		canvas.pack(expand = YES, fill = BOTH)
		gif1 = PhotoImage(file = './data/3.gif')
		canvas.create_image(0, 0, image = gif1, anchor = NW)

		# Frame
		contact_frame = Frame(self.root, height = 265, width = 420, relief = FLAT, bd = 1)
		contact_frame.place(x=90,y=175)

		x,y = 70,20

		# Components
		Label(contact_frame, text="Ngeria Mess | computerized reservation system", font=("helvetica", 14)).place(x=x-60, y = y-10)
		Label(contact_frame, text="Contact us", font=("Calibri", 12)).place(x=x+100, y = y+20)
		Label(contact_frame, justify=LEFT, wraplength=350, text = "Reservation Queries:\n\tEmail: ngeriamess@admin.com\n\tTelephone: +254 712345678\n\tFacsimile : +254 712345678\n\tAddress: Ngeria Mess,Moi University-Kenya.").place(x=x-40, y = y+50)
		Label(contact_frame, justify=LEFT, wraplength=350, text = "Customer care:\n\tEmail: custcare@svs.com\n\tTelephone:+254 787654321\n\tFacsimile : 0787654321\n\tAddress: Ngeria Mess,Moi University-Kenya.").place(x=x-40, y = y+140)
		Button(self.root, text ="back", command=(lambda: self.root.destroy())).place(x=420,y=215)
		
		# run
		self.root.mainloop()

		
if __name__ == "__main__":
	contact()