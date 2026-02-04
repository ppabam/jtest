def main():
    for i in range(2, 10):
        print(f"--- {i}단 ---")
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        print()

if __name__ == "__main__":
    main()
