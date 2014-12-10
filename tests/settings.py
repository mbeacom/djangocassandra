SECRET_KEY = "foo"

DATABASES = {
    'default': {
        'ENGINE': 'djangocassandra.db.backends.cassandra',
        'DEFAULT_KEYSPACE': 'test',
        'CONTACT_POINTS': ('localhost',),
        'PORT': 9042,
        'KEYSPACES': {
            'test': {
                'replication_factor': 1,
                'replication_strategy': 'SimpleStrategy'
            }
        }
    }
}
