def open_file(file):
  file = open('file.csv','r')
  data = []
  #readlines
  for string in file:
    data.append(map(strip, string.split(',')))
  file.close()
  return data

def str_to_dict(data):
  dataset = []
  keys = data.pop(0)
  #[dict(zip(keys, row)) for row in data]
  for i in data:
    d = dict(zip(keys,i))
    d['resource'],d['count']=int(d['resource']),int(d['count'])
    dataset.append(d)
  return dataset

def filter_id(dataset,id):
  return list(filter(lambda k: k['stuff_id']==id, dataset))

def filter_resource(dataset, resource):
  return list(filter(lambda k: k['resource']==resource, dataset))

def sort_data(dataset):
  return sorted(dataset, key=lambda k: int(k['data'][-2:]))
