import pandas

def read_in():
    dataset = pandas.read_csv("./signed_6.csv", sep=',', delimiter=None, header='infer')
    return dataset

def main():
    dataset = read_in()
    list = dataset.values.tolist()
    print(list[0])


if __name__ == "__main__":
    main()