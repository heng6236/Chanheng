# Copyright (c) 2021, Z1 and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class CourseTime(Document):
	self.full_time = f'{self.start_time or ""} {self.end_time or ""}'
