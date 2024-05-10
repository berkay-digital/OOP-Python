import numpy as np


def main():
    print(np.__version__)
    print(np.array([1, 2, 3]))
    print("Hello World!")
    print(np.zeros((3, 3, 3)))
    print(np.ones((3, 3, 3)))
    print(np.random.random((3, 3, 3)))
    print(np.random.randint(0, 10, (3, 3, 3)))

    a = np.array([1,2,4,8])
    b = a.reshape((2,2))
    print(b)
    print(a.sum())
    print(a.min())
    print(a.max())
    print(a.mean())
    print(a.std())
    print(a.argmax())



if __name__ == "__main__":
    main()
