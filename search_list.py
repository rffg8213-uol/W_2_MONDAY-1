def get_ordered_list(lst=None):
    if lst is None:
        user_input = input("Enter a list of integers separated by commas: ")
        lst = [int(x.strip()) for x in user_input.split(",")]
    return sorted(lst)

if __name__ == '__main__':
    # Test the function locally
    print(get_ordered_list())