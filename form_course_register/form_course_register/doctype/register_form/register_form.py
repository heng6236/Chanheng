# Copyright (c) 2021, Z1 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RegisterForm(Document):
	def before_save(self):
		self.full_name = f'{self.first_name or ""} {self.last_name or ""}'
		data = frappe.db.sql(f"""SELECT 
									`course_price`,
									`course_name`
								FROM 
									`tabCourse List` 
								WHERE `name` = '{self.course_list}'
								""")
		self.course_price = data[0][0]