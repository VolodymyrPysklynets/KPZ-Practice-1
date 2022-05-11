def download_csv(urlpath):
    import requests
    import numpy as np
    import csv

    response = requests.get(urlpath)

    with open("originalUserData.csv", 'wb') as f:
        f.write(response.content)

    with open("originalUserData.csv") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        data_read = [row for row in reader]

    del data_read[-1]

    arr = np.asarray(data_read)
    with open('originalUserData.csv', 'w') as f:
        mywriter = csv.writer(f, delimiter=',')
        mywriter.writerows(arr)

    print('Completed!')
