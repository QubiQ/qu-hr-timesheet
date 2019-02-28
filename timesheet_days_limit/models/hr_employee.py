# Copyright 2019 Joan Segui <joan.segui@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, _


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    check_timesheet_day = fields.Boolean(
        string=_('Check day of the time sheet'),
        default=True,
        help=_("Allows to review the day of imputation of the hours")
    )
    timesheet_days_back = fields.Integer(
        string=_('Remaining days'),
        default=7,
        help=_("Days left until the imputation deadline")
    )
