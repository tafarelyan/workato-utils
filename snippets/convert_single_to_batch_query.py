def convert_single_to_batch_query(data, query_type='query', batch_size=50):
    return {
        'queries': [
            {
                'query': '%s { %s }' % (query_type, ''.join([
                    '''
                    n%d: card(id: %s) {
                        id
                        title
                    }
                    ''' % (index, row['id'])
                    for index, row in enumerate(data[i:i+batch_size], start=1)
                ]))
            }
            for i in range(0, len(data), batch_size)
        ]
    }
