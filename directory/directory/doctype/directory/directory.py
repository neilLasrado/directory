# -*- coding: utf-8 -*-
# Copyright (c) 2015, Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document
from frappe.utils import validate_email_add

class Directory(Document):
	def validate(self):
		validate_email_add(self.email_address.strip(), True)
		validate_email_add(self.s_email_address.strip(), True)