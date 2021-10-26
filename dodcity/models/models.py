# -*- coding: utf-8 -*-

from odoo import models, fields, api


class player(models.Model):
    _name = 'dodcity.player'
    _description = 'Dodo player'

    name = fields.Char()


class habitat(models.Model):
    _name = 'dodcity.habitat'
    _descripcion = 'habitat'
    valor = fields.Integer()
    porcentajemejora = fields.Float()
    maxdodos = fields.Integer()

    name = fields.Char()


class comedor(models.Model):
    _name = 'dodcity.comedor'
    _descripcion = 'comedor'
    valor = fields.Float()
    mejora = fields.Integer()

    name = fields.Char()
    


