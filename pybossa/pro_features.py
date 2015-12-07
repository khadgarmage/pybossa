# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2015 SciFabric LTD.
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.


class ProFeatureHandler(object):

    def __init__(self, config):
        self.config = config

    def auditlog_enabled_for(self, user):
        if not self.config.get('auditlog'):
            return True
        return user.is_authenticated() and (user.admin or user.pro)

    def webhooks_enabled_for(self, user):
        if not self.config.get('webhooks'):
            return True
        return user.is_authenticated() and (user.admin or user.pro)

    def autoimporter_enabled_for(self, user):
        if not self.config.get('autoimporter'):
            return True
        return user.is_authenticated() and (user.admin or user.pro)

    def only_for_pro(self, feature):
        return self.config.get(feature)
