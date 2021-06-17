# Copyright 2019 Joan Segui <joan.segui@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    check_timesheet_day = fields.Boolean(
        string='Check day of the time sheet',
        default=True,
        help="Allows to review the day of imputation of the hours"
    )
    timesheet_days_back = fields.Integer(
        string='Remaining days',
        default=7,
        help="Days left until the imputation deadline"
    )
