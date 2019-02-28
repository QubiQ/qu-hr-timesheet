# Copyright 2019 Joan Segui <joan.segui@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    @api.multi
    @api.constrains('date', 'user_id')
    def restriction_imputation_day(self):
        for sel in self:
            employeesLogged = sel.env.user.employee_ids
            if employeesLogged and employeesLogged[0].check_timesheet_day:
                if fields.Date.from_string(sel.date) < (fields.Date.from_string(fields.Date.today()) - timedelta(days=employeesLogged[0].timesheet_days_back)):
                    raise ValidationError(_("The indicated date is higher than the allowed one, consult a superior action to be able to do it."))
