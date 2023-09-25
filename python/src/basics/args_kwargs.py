def test_var_args(f_arg, *argv, **kwargs):
    print("[variable]")
    print("First argument:", f_arg)
    print("[*argv arguments]")
    for arg in argv:
        print("*argv arguments:", arg)

    print("[**kwargs arguments]")
    for key, value in kwargs.items():
        print(f"kwargs: {key} = {value}")

test_var_args('python', 'foo', 'bar', color="red", age=18)