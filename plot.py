import matplotlib.pyplot as plt

def open_file(file):
  data = []
  for string in file:
    data.append(string.strip('\n').split(','))
  file.close()
  return data

def str_to_dict(data):
  dataset = []
  keys = data.pop(0)
  for i in data:
    d = dict(zip(keys,i))
    d['resource'],d['count'],d['staff_id']=int(d['resource']),int(d['count']),int(d['staff_id'])
    dataset.append(d)
  return dataset

def filters(dataset,val,key):
  return list(filter(lambda k: str(val) in str(k[key]), dataset))

def sort_data(dataset):
  return sorted(dataset, key=lambda k: k['date'].split('-'))

def plotting(data, x_ax, y_ax, title):
  x,y = [],[]
  sorted_data = sort_data(data)
  for i in sorted_data:
      x.append(i[x_ax])
      y.append(int(i[y_ax]))
  plt.title(title)
  plt.plot(x,y,marker='o')
  plt.show()

def plot1(data,resource):
  filtered_resource = filters(data, resource,'resource')
  sorted_resource = sort_data(filtered_resource)
  newlist=[{k: v for k, v in dic.items() if k=='date' or k=='count'} for dic in sorted_resource]
  plotting(newlist, 'date', 'count', 'resource '+str(resource))

def plot2(data,resource,staff_id):
  filtered_resource = filters(data,resource, 'resource')
  staffs=[]
  for i in filtered_resource:
    if not i['staff_id'] in staffs:
      staffs.append(i['staff_id'])
      filtered_staff = filters(filtered_resource, i['staff_id'],'staff_id')
      sorted_staff = sort_data(filtered_staff)
      newlist=[{k: v for k, v in dic.items() if k=='date' or k=='count'} for dic in sorted_staff]
      plotting(newlist,'date','count',str(i['staff_id'])+' staff_id ')

def main():
  file = open('plot.txt','r')
  data = open_file(file)
  data = str_to_dict(data)
  plot1(data,1)
  plot2(data,1,4)

if __name__=='__main__':
    main()