import mongoengine as me


class User(me.Document):
    name = me.StringField()
    flow_subscriptions = me.ListField(blank=True)
    meta = {
        'collections': 'users',
        'indexes': [
            {'fields': ['name'], 'unique': True}
        ],
    }
