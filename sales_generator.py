import datetime
import random
import math

def generate_power(n):
    return [10 + 2 ** x for x in range(n)]

def generate_square(n):
    return [10 + x ** 2 for x in range(n)]

def generate_sin(n):
    data = [i * 3.1415 / n for i in range(n)]
    return [int(10 + 40 * math.sin(x)) for x in data]

def generate_date(n):
    return [(datetime.datetime(2020, 1, 1) + datetime.timedelta(days=30 * i)).strftime('%Y-%m') for i in range(n)]

def generate_file(filename, num_months, num_resource, num_staff):
    months = generate_date(num_months) * num_resource * num_staff
    resources=[str(random.randint(0,num_resource-1)+1) for _ in enumerate(months)]
    staff_id=[str(random.randint(0,num_staff-1)+1) for _ in enumerate(months)]
    if random.randint(0,2)==0:
      count=generate_power(len(months))
    elif random.randint(0,2)==1:
      count=generate_square(len(months))
    else:
      count=generate_sin(len(months))
    elements = list(zip(months, resources, staff_id, [str(i) for i in count]))
    random.shuffle(elements)
    f = open(filename, 'w')
    f.write('date,resource,staff_id,count\n')
    f.write('\n'.join([','.join(elem) for elem in elements]))
    f.write('\n')
    f.close()


def main():
    filename = 'plot.txt'
    num_month = 2
    num_resource =2
    num_staff = 4
    generate_file(filename, num_month, num_resource, num_staff)

if __name__ == '__main__':
    main()