my_dict = {'flashlight0': 'green', 'flashlight1': 'yellow', 'flashlight2': 'orange'}
print('Dict:', my_dict)
print('Existing value: ', my_dict['flashlight1'])
print('Not existing value:', my_dict.get('flashlight3', 'No such key exists'))
my_dict.update({'flashlight4': 'violet',
                'flashlight5': 'pink'})
a = my_dict.pop('flashlight4')
print('Deleted value: ', a)
print('Modified dictionary:', my_dict)

my_set = {1.6, 5.5, 4, 'chamomile', 'geranium', True, 'chamomile', 4}
print('Set: ', my_set)
my_set.update({3, False})
my_set.discard('chamomile')
print('Modified set: ', my_set)