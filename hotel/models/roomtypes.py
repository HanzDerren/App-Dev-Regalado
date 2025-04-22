from odoo import models, fields

class RoomType(models.Model):
    _name = 'hotel.roomtypes'
    _description = 'Hotel Room Type Master List'
    _order = "name"

    name = fields.Char(string="Room Type Name", required=True)
    description = fields.Char(string="Room Type Description")

    photo_bed = fields.Image(string="Bed Photo")
    photo_restroom = fields.Image(string="Restroom Photo")

    room_ids = fields.One2many('hotel.rooms', 'roomtype_id', string="Rooms")
    daily_charge_ids = fields.One2many('hotel.dailycharges', 'roomtype_id', string="Daily Charges")


class DailyCharge(models.Model):
    _name = 'hotel.dailycharges'
    _description = 'Hotel Room Type Daily Charges List'

    charge_id = fields.Many2one('hotel.charges', string="Charge Title", required=True)
    amount = fields.Float(string="Daily Amount", digits=(10, 2))
    roomtype_id = fields.Many2one('hotel.roomtypes', string="Room Type", ondelete='cascade')
