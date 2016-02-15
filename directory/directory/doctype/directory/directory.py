# -*- coding: utf-8 -*-
# Copyright (c) 2015, Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document
from frappe.utils import validate_email_add
import frappe
import re

class Directory(Document):
	def validate(self):
		if self.email_address:
			validate_email_add(self.email_address.strip(), True)
		if self.residential_tel:
			validate_mobile(self.residential_tel)
		if self.office_tel:
			validate_mobile(self.office_tel)
		if self.mobile:
			validate_mobile(self.mobile)
		
		if self.is_directory:
			if self.s_email_address:
				validate_email_add(self.s_email_address.strip(), True)
			if self.s_residential_number:
				validate_mobile(self.s_residential_number)
			if self.s_office_number:
				validate_mobile(self.s_office_number)
			if self.s_mobile_number:
				validate_mobile(self.s_mobile_number)

			for d in self.bod:
				if d.email_address:
					validate_email_add(d.email_address.strip(), True)
	
				if d.mobile_number:
					validate_mobile(d.mobile_number)


def validate_mobile(value):
	rule = re.compile(r'^[0-9]*$')
	
	if not rule.search(value):
		frappe.throw("Invalid mobile number - {0}".format(value))